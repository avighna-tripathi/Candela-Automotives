"""Repository-aware dataset loaders."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import sqlite3

from data.loader import read_csv
from data.preprocessing import clean_currency_column, clean_sales_history

BASE_DIR = Path(__file__).resolve().parents[1]
LEGACY_ROOT = BASE_DIR
MARKETING_DIR = LEGACY_ROOT / "MARKETING"
PLMS_DIR = LEGACY_ROOT / "Plms"


@dataclass(frozen=True)
class DatasetAsset:
    """A named dataframe with context for UI rendering."""

    name: str
    description: str
    frame: pd.DataFrame


@dataclass
class DatasetBundle:
    """A collection wrapper for dashboard datasets."""

    datasets: dict[str, DatasetAsset]

    def dataset_names(self) -> list[str]:
        return list(self.datasets)

    def get(self, name: str) -> DatasetAsset:
        return self.datasets.get(name)

    def catalog_frame(self) -> pd.DataFrame:
        rows = [
            {
                "dataset": asset.name,
                "rows": asset.frame.shape[0],
                "columns": asset.frame.shape[1],
                "description": asset.description,
            }
            for asset in self.datasets.values()
        ]
        return pd.DataFrame(rows)


def _load_sales_history() -> DatasetAsset:
    frame = read_csv(PLMS_DIR / "sales.csv")
    cleaned = clean_sales_history(frame)
    return DatasetAsset(
        name="sales_history",
        description="Legacy PLMS yearly sales and profit history cleaned for analytics.",
        frame=cleaned,
    )


def _load_youtube_campaigns() -> DatasetAsset:
    frame = read_csv(MARKETING_DIR / "Youtubers.csv")
    frame.columns = [
        "youtuber",
        "subscribers",
        "contract_start",
        "contract_end",
        "average_views",
        "marketing_type",
        "amount_usd",
    ]
    frame["subscribers"] = pd.to_numeric(
        frame["subscribers"].astype(str).str.replace(",", "", regex=False).str.strip(),
        errors="coerce",
    )
    frame["average_views"] = pd.to_numeric(
        frame["average_views"].astype(str).str.replace(",", "", regex=False).str.strip(),
        errors="coerce",
    )
    frame["amount_usd"] = clean_currency_column(frame["amount_usd"])
    return DatasetAsset(
        name="youtube_campaigns",
        description="Influencer-style YouTube promotion deals from the marketing module.",
        frame=frame,
    )


def _load_social_media_campaigns() -> DatasetAsset:
    frame = read_csv(MARKETING_DIR / "socmed.csv")
    frame.columns = [
        "name",
        "platform",
        "followers",
        "contract_start",
        "contract_end",
        "amount_usd",
    ]
    frame["followers"] = pd.to_numeric(frame["followers"], errors="coerce")
    frame["amount_usd"] = clean_currency_column(frame["amount_usd"])
    return DatasetAsset(
        name="social_media_campaigns",
        description="Social platform influencer records from the marketing module.",
        frame=frame,
    )


def _load_news_magazine_campaigns() -> DatasetAsset:
    frame = read_csv(MARKETING_DIR / "newsmag.csv")
    frame.columns = [
        "name",
        "publication_type",
        "contract_start",
        "contract_end",
        "ads_per_month",
        "front_page_placements",
        "amount_usd",
    ]
    frame["ads_per_month"] = pd.to_numeric(frame["ads_per_month"], errors="coerce")
    frame["front_page_placements"] = pd.to_numeric(frame["front_page_placements"], errors="coerce")
    frame["amount_usd"] = clean_currency_column(frame["amount_usd"])
    return DatasetAsset(
        name="news_magazine_campaigns",
        description="Print-media marketing contracts from the legacy marketing module.",
        frame=frame,
    )


def _load_tv_radio_campaigns() -> DatasetAsset:
    frame = read_csv(MARKETING_DIR / "tvrad.csv")
    frame.columns = [
        "name",
        "broadcast_type",
        "contract_start",
        "contract_end",
        "ad_length_seconds",
        "broadcasts_per_day",
        "amount_usd",
    ]
    frame["ad_length_seconds"] = pd.to_numeric(frame["ad_length_seconds"], errors="coerce")
    frame["broadcasts_per_day"] = pd.to_numeric(frame["broadcasts_per_day"], errors="coerce")
    frame["amount_usd"] = clean_currency_column(frame["amount_usd"])
    return DatasetAsset(
        name="tv_radio_campaigns",
        description="Television and radio contract records from the marketing module.",
        frame=frame,
    )


def _fetch_sqlite_table(table_name: str, fallback_description: str) -> DatasetAsset:
    """Fetch a table from the local candela.db SQLite database with graceful failure."""
    try:
        connection = sqlite3.connect(LEGACY_ROOT / "candela.db")
        # For sqlite, read_sql is fully supported
        frame = pd.read_sql(f"SELECT * FROM {table_name}", con=connection)
        connection.close()
        return DatasetAsset(
            name=f"sqlite_{table_name}",
            description=f"Live operational data from SQLite table: {table_name}.",
            frame=frame,
        )
    except Exception as e:
        return DatasetAsset(
            name=f"sqlite_{table_name}",
            description=f"⚠️ {fallback_description} (SQLite Connection Failed: {e})",
            frame=pd.DataFrame(),
        )


def load_repository_bundle() -> DatasetBundle:
    """Load all reusable repository datasets needed by the dashboard."""
    datasets = {
        asset.name: asset
        for asset in [
            _load_sales_history(),
            _load_youtube_campaigns(),
            _load_social_media_campaigns(),
            _load_news_magazine_campaigns(),
            _load_tv_radio_campaigns(),
            _fetch_sqlite_table("employee", "Employee records could not be loaded."),
            _fetch_sqlite_table("departments", "Department records could not be loaded."),
            _fetch_sqlite_table("catalog", "Vehicle catalog could not be loaded."),
        ]
    }
    return DatasetBundle(datasets=datasets)
