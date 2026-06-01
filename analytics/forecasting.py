"""Forecasting helpers for future trend prediction."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class ForecastSummary:
    """Forecast output with business context."""

    model_name: str
    score: float
    outlook: str
    prediction_frame: pd.DataFrame | None = None
    feature_importance: pd.DataFrame | None = None


def run_sales_forecast(frame: pd.DataFrame) -> ForecastSummary:
    """Predict the next year of sales using a random forest regressor when available."""
    working = frame.dropna(
        subset=["year", "sales_million_usd", "profit_million_usd", "target_sales_million_usd"]
    ).copy()
    if len(working) < 5:
        return ForecastSummary(
            model_name="RandomForestRegressor",
            score=0.0,
            outlook="Not enough complete historical rows are available for a reliable forecast.",
            prediction_frame=None,
        )

    try:
        from sklearn.ensemble import RandomForestRegressor
    except ImportError:
        return ForecastSummary(
            model_name="RandomForestRegressor",
            score=0.0,
            outlook="scikit-learn is not installed yet, so random forest forecasting cannot run.",
            prediction_frame=None,
        )

    features = working[["year", "profit_million_usd", "target_sales_million_usd"]]
    target = working["sales_million_usd"]

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(features, target)
    score = float(model.score(features, target))

    latest = working.iloc[-1]
    next_year = int(latest["year"]) + 1
    forecast_features = pd.DataFrame(
        [
            {
                "year": next_year,
                "profit_million_usd": latest["profit_million_usd"],
                "target_sales_million_usd": latest["target_sales_million_usd"],
            }
        ]
    )
    prediction = float(model.predict(forecast_features)[0])
    prediction_frame = pd.DataFrame(
        [{"year": next_year, "predicted_sales_million_usd": prediction, "model_score": score}]
    )
    feature_importance = pd.DataFrame(
        {"feature": features.columns, "importance": model.feature_importances_}
    ).sort_values("importance", ascending=False, ignore_index=True)

    return ForecastSummary(
        model_name="RandomForestRegressor",
        score=score,
        prediction_frame=prediction_frame,
        feature_importance=feature_importance,
        outlook=(
            "The random forest forecast estimates the next sales period using recent performance "
            "and target context. Management should treat this as a directional planning aid rather "
            "than a guarantee."
        ),
    )
