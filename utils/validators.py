"""Validation helpers."""

from __future__ import annotations

import pandas as pd


def require_columns(frame: pd.DataFrame, columns: list[str]) -> list[str]:
    """Return a list of missing columns for validation workflows."""
    return [column for column in columns if column not in frame.columns]
