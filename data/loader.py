"""Low-level file loaders for repository datasets."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def read_csv(path: Path) -> pd.DataFrame:
    """Read a CSV file with consistent defaults."""
    return pd.read_csv(path)
