"""Clustering helpers for campaign segmentation."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class ClusteringSummary:
    """Cluster results with business framing."""

    cluster_count: int
    notes: str
    frame: pd.DataFrame | None = None


def run_campaign_clustering(frame: pd.DataFrame, numeric_columns: list[str]) -> ClusteringSummary:
    """Run KMeans clustering on a campaign dataset when feasible."""
    working = frame[numeric_columns].dropna().copy()
    if len(working) < 3 or len(numeric_columns) < 2:
        return ClusteringSummary(
            cluster_count=0,
            notes="The selected dataset does not have enough clean numeric rows for clustering.",
            frame=None,
        )

    try:
        from sklearn.cluster import KMeans
    except ImportError:
        return ClusteringSummary(
            cluster_count=0,
            notes="scikit-learn is not installed yet, so KMeans clustering cannot run.",
            frame=None,
        )

    cluster_count = min(3, len(working))
    model = KMeans(n_clusters=cluster_count, n_init=10, random_state=42)
    labels = model.fit_predict(working)
    result = frame.loc[working.index].copy()
    result["cluster"] = labels

    return ClusteringSummary(
        cluster_count=cluster_count,
        notes=(
            "Clusters separate campaign entities by scale and spend, which helps identify "
            "premium, mid-tier, and efficient-reach partnership groups."
        ),
        frame=result,
    )
