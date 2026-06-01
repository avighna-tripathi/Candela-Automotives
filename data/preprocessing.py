"""Dataset cleaning helpers."""

from __future__ import annotations

import pandas as pd


def clean_sales_history(frame: pd.DataFrame) -> pd.DataFrame:
    """Normalize the PLMS sales history file into analysis-ready columns."""
    output = frame.copy()
    output.columns = [
        "year",
        "sales_million_usd",
        "profit_million_usd",
        "profit_percentage",
        "target_sales_million_usd",
        "target_reached",
    ]
    output = output.dropna(subset=["year"]).copy()
    output["target_reached"] = output["target_reached"].fillna("UNKNOWN")

    numeric_columns = [
        "year",
        "sales_million_usd",
        "profit_million_usd",
        "profit_percentage",
        "target_sales_million_usd",
    ]
    for column in numeric_columns:
        output[column] = pd.to_numeric(output[column], errors="coerce")

    output["target_gap_million_usd"] = (
        output["sales_million_usd"] - output["target_sales_million_usd"]
    )
    output = output.sort_values("year").reset_index(drop=True)
    return output


def clean_currency_column(series: pd.Series) -> pd.Series:
    """Convert dollar-formatted text values into numeric floats where possible."""
    return pd.to_numeric(
        series.astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False).str.strip(),
        errors="coerce",
    )
