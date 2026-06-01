"""Trend-oriented analytics helpers."""

from __future__ import annotations

import pandas as pd


def add_growth_features(
    frame: pd.DataFrame,
    value_column: str,
    periods: int = 1,
) -> pd.DataFrame:
    """Add simple change and growth-rate columns to a time-ordered dataset."""
    output = frame.copy()
    output[f"{value_column}_change"] = output[value_column].diff(periods=periods)
    output[f"{value_column}_growth_pct"] = output[value_column].pct_change(periods=periods) * 100
    output[f"{value_column}_moving_avg"] = output[value_column].rolling(window=3, min_periods=1).mean()
    return output
