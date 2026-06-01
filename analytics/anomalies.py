"""Anomaly detection helpers."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


def iqr_outlier_mask(series: pd.Series) -> pd.Series:
    """Flag outliers using the interquartile range rule."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return (series < lower) | (series > upper)


@dataclass(frozen=True)
class AnomalySummary:
    """Summary of anomalies detected in a numeric business series."""

    column: str
    count: int
    frame: pd.DataFrame
    explanation: str


def detect_anomalies(frame: pd.DataFrame, column: str) -> AnomalySummary:
    """Detect anomalies in a dataframe column using IQR and z-score style checks."""
    working = frame.copy()
    numeric = pd.to_numeric(working[column], errors="coerce")
    cleaned = working.loc[numeric.notna()].copy()
    cleaned[column] = numeric.loc[numeric.notna()]

    if cleaned.empty:
        return AnomalySummary(
            column=column,
            count=0,
            frame=cleaned,
            explanation="No usable numeric values are available for anomaly detection.",
        )

    cleaned["iqr_outlier"] = iqr_outlier_mask(cleaned[column])
    std = cleaned[column].std()
    if std and not pd.isna(std):
        cleaned["z_score"] = (cleaned[column] - cleaned[column].mean()) / std
        cleaned["z_outlier"] = cleaned["z_score"].abs() > 2
    else:
        cleaned["z_score"] = 0.0
        cleaned["z_outlier"] = False

    cleaned["anomaly_flag"] = cleaned["iqr_outlier"] | cleaned["z_outlier"]
    anomalies = cleaned.loc[cleaned["anomaly_flag"]].copy()
    return AnomalySummary(
        column=column,
        count=int(anomalies.shape[0]),
        frame=anomalies,
        explanation=(
            "Anomalies flag unusually high or low values that may represent demand spikes, "
            "underperformance, data quality issues, or one-off operational events."
        ),
    )
