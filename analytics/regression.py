"""Regression helpers for dashboard modeling."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class RegressionResult:
    """Display-ready regression output."""

    model_name: str
    r2: float
    mae: float
    rmse: float
    actual: pd.DataFrame
    business_summary: str


def _metrics(actual: np.ndarray, predicted: np.ndarray) -> tuple[float, float, float]:
    residuals = actual - predicted
    mae = float(np.mean(np.abs(residuals)))
    rmse = float(np.sqrt(np.mean(np.square(residuals))))
    ss_res = float(np.sum(np.square(residuals)))
    ss_tot = float(np.sum(np.square(actual - np.mean(actual))))
    r2 = 1 - ss_res / ss_tot if ss_tot else 0.0
    return r2, mae, rmse


def run_sales_regression(
    frame: pd.DataFrame,
    polynomial_degree: int = 2,
) -> list[RegressionResult]:
    """Run linear and polynomial regression over the sales history dataset."""
    working = frame.dropna(subset=["year", "sales_million_usd"]).copy()
    if len(working) < 3:
        return []

    x = working["year"].to_numpy(dtype=float)
    y = working["sales_million_usd"].to_numpy(dtype=float)
    results: list[RegressionResult] = []

    linear_coefficients = np.polyfit(x, y, deg=1)
    linear_predictions = np.polyval(linear_coefficients, x)
    r2, mae, rmse = _metrics(y, linear_predictions)
    results.append(
        RegressionResult(
            model_name="Linear Regression",
            r2=r2,
            mae=mae,
            rmse=rmse,
            actual=pd.DataFrame(
                {"year": working["year"], "actual": y, "predicted": linear_predictions}
            ),
            business_summary=(
                "The linear fit shows the baseline direction of long-term sales movement and "
                "is useful for explaining whether the business is structurally growing or plateauing."
            ),
        )
    )

    if len(working) > polynomial_degree:
        poly_coefficients = np.polyfit(x, y, deg=polynomial_degree)
        poly_predictions = np.polyval(poly_coefficients, x)
        r2, mae, rmse = _metrics(y, poly_predictions)
        results.append(
            RegressionResult(
                model_name=f"Polynomial Regression (degree {polynomial_degree})",
                r2=r2,
                mae=mae,
                rmse=rmse,
                actual=pd.DataFrame(
                    {"year": working["year"], "actual": y, "predicted": poly_predictions}
                ),
                business_summary=(
                    "The polynomial fit captures curvature in the sales pattern and is useful "
                    "when growth has accelerated or slowed unevenly over time."
                ),
            )
        )

    return results
