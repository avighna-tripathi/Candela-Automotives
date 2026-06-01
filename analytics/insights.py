"""Plain-English insight generation helpers."""

from __future__ import annotations

import pandas as pd


def summarize_sales_direction(latest_growth_pct: float) -> str:
    """Convert a numeric growth signal into business language."""
    if latest_growth_pct > 10:
        return "Sales are accelerating strongly, which suggests momentum worth protecting and scaling."
    if latest_growth_pct > 0:
        return "Sales are improving modestly, indicating a stable but still optimizable growth pattern."
    if latest_growth_pct == 0:
        return "Sales are flat, which points to a need for renewed demand-generation experiments."
    return "Sales are contracting, which raises short-term revenue risk and warrants immediate diagnosis."


def build_sales_insight_block(frame: pd.DataFrame) -> list[str]:
    """Generate plain-English insights from the sales dataset."""
    if frame.empty:
        return [
            "No sales data is currently available to generate insights.",
            "Please ensure the sales history dataset is loaded and valid."
        ]
    
    latest = frame.iloc[-1]
    previous = frame.iloc[-2] if len(frame) > 1 else latest
    growth_pct = (
        ((latest["sales_million_usd"] - previous["sales_million_usd"]) / previous["sales_million_usd"]) * 100
        if previous["sales_million_usd"]
        else 0.0
    )
    return [
        summarize_sales_direction(growth_pct),
        (
            f"Latest observed sales are ${latest['sales_million_usd']:,.1f}M against a target of "
            f"${latest['target_sales_million_usd']:,.1f}M."
        ),
        (
            "If the target gap remains negative, management should review demand generation, "
            "channel mix, and model pricing strategy before the next planning cycle."
        ),
    ]


def build_campaign_recommendations(bundle: dict[str, pd.DataFrame]) -> list[str]:
    """Generate high-level marketing recommendations from campaign datasets."""
    recommendations: list[str] = []
    for name, frame in bundle.items():
        numeric_columns = frame.select_dtypes(include="number")
        if numeric_columns.empty:
            continue
        avg_spend = numeric_columns.iloc[:, -1].mean()
        recommendations.append(
            f"{name.replace('_', ' ').title()} has an average quantified deal value of {avg_spend:,.1f}, "
            "which can be used to benchmark future partnership negotiations."
        )
    return recommendations


def build_management_recommendations(sales: pd.DataFrame) -> dict[str, list[str]]:
    """Generate consulting-style recommendations from the sales dataset."""
    if sales.empty:
        return {
            "Key Findings": ["No sales data is available to analyze."],
            "Risks": ["Missing or malformed sales history prevents operational planning."],
            "Opportunities": ["Restore or repair the sales dataset to unlock deeper analytics."],
            "Suggested Actions": ["Investigate the data pipeline or source files for recent failures."]
        }

    latest = sales.iloc[-1]
    gap = latest["sales_million_usd"] - latest["target_sales_million_usd"]

    findings = [
        f"Latest visible sales are ${latest['sales_million_usd']:,.1f}M.",
        f"Latest visible profit margin is {latest['profit_percentage']:,.1f}%.",
    ]
    risks = [
        "Legacy source systems contain data quality inconsistencies that can distort operational planning.",
        "Small historical sample size limits the confidence of any forecast or segmentation model.",
    ]
    opportunities = [
        "Marketing datasets can be used to benchmark spend efficiency across channels.",
        "Sales trend monitoring can support earlier pricing and demand-generation interventions.",
    ]
    actions = [
        "Standardize the source data pipeline before expanding model complexity.",
        "Review under-target periods and test targeted campaigns or pricing changes on weaker demand windows.",
    ]

    if gap < 0:
        risks.append("The latest observed sales trail target, indicating revenue execution risk.")
        actions.append("Prioritize rapid diagnosis of the target gap and reallocate spend toward higher-reach channels.")
    else:
        opportunities.append("The latest period meets or exceeds target, which creates room to scale proven demand levers.")
        actions.append("Protect the strongest-performing channels and monitor whether current momentum is sustainable.")

    return {
        "Key Findings": findings,
        "Risks": risks,
        "Opportunities": opportunities,
        "Suggested Actions": actions,
    }
