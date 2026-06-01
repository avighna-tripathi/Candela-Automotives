"""Chart preparation helpers."""

from __future__ import annotations

import pandas as pd


def sort_by_column(frame: pd.DataFrame, column: str) -> pd.DataFrame:
    """Return a sorted copy of a dataframe for chart rendering."""
    return frame.sort_values(column).reset_index(drop=True)
