"""Overview KPI builders."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from data.repositories import DatasetBundle


@dataclass(frozen=True)
class OverviewMetric:
    """Display-ready metric payload."""

    label: str
    value: str
    delta: str


def calculate_sales_kpis(sales: pd.DataFrame) -> dict[str, float]:
    """Calculate reusable business KPIs from the sales dataset."""
    working = sales.dropna(
        subset=["sales_million_usd", "profit_million_usd", "target_sales_million_usd"]
    ).copy()
    if working.empty:
        return {
            "revenue_million_usd": 0.0,
            "profit_million_usd": 0.0,
            "average_margin_pct": 0.0,
            "latest_sales_million_usd": 0.0,
            "latest_target_gap_million_usd": 0.0,
            "mom_like_growth_pct": 0.0,
        }

    latest = working.iloc[-1]
    previous = working.iloc[-2] if len(working) > 1 else latest
    growth_pct = (
        ((latest["sales_million_usd"] - previous["sales_million_usd"]) / previous["sales_million_usd"]) * 100
        if previous["sales_million_usd"]
        else 0.0
    )

    return {
        "revenue_million_usd": float(working["sales_million_usd"].sum()),
        "profit_million_usd": float(working["profit_million_usd"].sum()),
        "average_margin_pct": float(working["profit_percentage"].mean()),
        "latest_sales_million_usd": float(latest["sales_million_usd"]),
        "latest_target_gap_million_usd": float(
            latest["sales_million_usd"] - latest["target_sales_million_usd"]
        ),
        "mom_like_growth_pct": float(growth_pct),
    }


def build_overview_metrics(bundle: DatasetBundle) -> list[OverviewMetric]:
    """Build headline metrics from the loaded repository datasets."""
    sales = bundle.get("sales_history").frame
    total_rows = sum(dataset.frame.shape[0] for dataset in bundle.datasets.values())
    kpis = calculate_sales_kpis(sales)

    return [
        OverviewMetric("Datasets", str(len(bundle.datasets)), "Legacy + cleaned"),
        OverviewMetric("Total Records", f"{total_rows:,}", "Across reusable sources"),
        OverviewMetric("Analysis Modules", "9", "Spec-aligned pages"),
        OverviewMetric(
            "Latest Sales",
            f"${kpis['latest_sales_million_usd']:,.1f}M",
            f"Growth {kpis['mom_like_growth_pct']:,.1f}%",
        ),
    ]
