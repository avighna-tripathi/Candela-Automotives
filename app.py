"""Streamlit entry point for the Candela analytics dashboard."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from analytics.anomalies import detect_anomalies
from analytics.clustering import run_campaign_clustering
from analytics.forecasting import run_sales_forecast
from analytics.insights import (
    build_campaign_recommendations,
    build_management_recommendations,
    build_sales_insight_block,
)
from analytics.kpis import build_overview_metrics, calculate_sales_kpis
from analytics.regression import run_sales_regression
from analytics.trends import add_growth_features
from dashboard.components import render_dataset_preview, render_header, render_status_panel
from dashboard.text_blocks import (
    APP_SUBTITLE,
    APP_TITLE,
    EXECUTIVE_NOTE,
    PAGE_DESCRIPTIONS,
)
from data.repositories import DatasetBundle, load_repository_bundle


def render_overview(bundle: DatasetBundle) -> None:
    """Render the first dashboard page with high-level repository metrics."""
    metrics = build_overview_metrics(bundle)
    render_header(APP_TITLE, APP_SUBTITLE)

    columns = st.columns(4)
    for column, metric in zip(columns, metrics, strict=False):
        with column:
            st.metric(metric.label, metric.value, metric.delta)

    sales_kpis = calculate_sales_kpis(bundle.get("sales_history").frame)
    st.markdown("### Quick Business KPIs")
    kpi_a, kpi_b, kpi_c = st.columns(3)
    kpi_a.metric("Total Revenue", f"${sales_kpis['revenue_million_usd']:,.1f}M")
    kpi_b.metric("Total Profit", f"${sales_kpis['profit_million_usd']:,.1f}M")
    kpi_c.metric("Latest Target Gap", f"${sales_kpis['latest_target_gap_million_usd']:,.1f}M")

    st.markdown("### Executive Context")
    st.write(EXECUTIVE_NOTE)

    st.markdown("### Available Analysis Modules")
    render_status_panel(PAGE_DESCRIPTIONS)

    st.markdown("### Loaded Datasets")
    render_dataset_preview(bundle.catalog_frame())


def render_dataset_explorer(bundle: DatasetBundle) -> None:
    """Render a simple dataset explorer backed by the cleaned repository bundle."""
    st.title("Dataset Explorer")
    dataset_name = st.selectbox("Select a dataset", bundle.dataset_names())
    dataset = bundle.get(dataset_name)

    st.write(dataset.description)
    left, right, extra = st.columns(3)
    left.metric("Rows", dataset.frame.shape[0])
    right.metric("Columns", dataset.frame.shape[1])
    extra.metric("Null Values", int(dataset.frame.isna().sum().sum()))

    st.markdown("### Schema")
    schema = dataset.frame.dtypes.astype(str).rename("dtype").reset_index().rename(columns={"index": "column"})
    st.dataframe(schema, use_container_width=True)

    st.markdown("### Sample Rows")
    st.dataframe(dataset.frame.head(10), use_container_width=True)

    st.markdown("### Summary Statistics")
    numeric_frame = dataset.frame.select_dtypes(include="number")
    if numeric_frame.empty:
        st.info("This dataset has no numeric columns available for summary statistics yet.")
    else:
        st.dataframe(numeric_frame.describe().transpose(), use_container_width=True)
        if len(numeric_frame.columns) > 1 and len(numeric_frame) > 0:
            st.markdown("### Correlation Matrix")
            st.dataframe(numeric_frame.corr().style.background_gradient(cmap="coolwarm", axis=None), use_container_width=True)


def render_trend_analysis(bundle: DatasetBundle) -> None:
    """Render sales trend analytics and business commentary."""
    st.title("Trend Analysis")
    sales = add_growth_features(bundle.get("sales_history").frame, "sales_million_usd")

    if sales.empty:
        st.warning("Not enough data to analyze sales trends.")
        return

    st.line_chart(
        sales.set_index("year")[["sales_million_usd", "target_sales_million_usd", "sales_million_usd_moving_avg"]]
    )
    st.bar_chart(sales.set_index("year")[["target_gap_million_usd"]])

    latest = sales.iloc[-1]
    st.markdown("### Business Interpretation")
    
    gap_val = latest.get('target_gap_million_usd')
    gap_str = f"${gap_val:,.1f}M" if pd.notna(gap_val) else "Unknown"
    
    st.write(
        f"Sales closed at ${latest['sales_million_usd']:,.1f}M in {int(latest['year'])}, "
        f"with a target gap of {gap_str}."
    )
    for insight in build_sales_insight_block(sales):
        st.markdown(f"- {insight}")


def render_regression_analysis(bundle: DatasetBundle) -> None:
    """Render regression analysis over the cleaned sales history."""
    st.title("Regression Analysis")
    if st.button("Run Regression"):
        results = run_sales_regression(bundle.get("sales_history").frame)
        if not results:
            st.warning("Not enough clean sales data is available to run regression.")
            return

        for result in results:
            st.markdown(f"### {result.model_name}")
            left, middle, right = st.columns(3)
            left.metric("R2", f"{result.r2:.3f}")
            middle.metric("MAE", f"{result.mae:.2f}")
            right.metric("RMSE", f"{result.rmse:.2f}")
            st.line_chart(result.actual.set_index("year")[["actual", "predicted"]])
            st.write(result.business_summary)
    else:
        st.info("Use the button above to evaluate linear and polynomial sales patterns.")


def render_clustering_analysis(bundle: DatasetBundle) -> None:
    """Render campaign clustering analysis."""
    st.title("Clustering Analysis")
    options = {
        "youtube_campaigns": ["subscribers", "average_views", "amount_usd"],
        "social_media_campaigns": ["followers", "amount_usd"],
        "news_magazine_campaigns": ["ads_per_month", "front_page_placements", "amount_usd"],
        "tv_radio_campaigns": ["ad_length_seconds", "broadcasts_per_day", "amount_usd"],
    }
    dataset_name = st.selectbox("Select a dataset for clustering", list(options))

    if st.button("Run Clustering"):
        summary = run_campaign_clustering(bundle.get(dataset_name).frame, options[dataset_name])
        if summary.frame is None:
            st.warning(summary.notes)
            return
        st.metric("Cluster Count", summary.cluster_count)
        st.write(summary.notes)
        st.dataframe(summary.frame, use_container_width=True)
    else:
        st.info("Choose a campaign dataset and run clustering to explore partner segments.")


def render_forecasting(bundle: DatasetBundle) -> None:
    """Render random-forest-based sales forecasting."""
    st.title("Forecasting & Prediction")
    if st.button("Predict Future Trends"):
        summary = run_sales_forecast(bundle.get("sales_history").frame)
        st.metric("Model", summary.model_name, f"Train score {summary.score:.3f}")
        st.write(summary.outlook)
        if summary.prediction_frame is not None:
            st.dataframe(summary.prediction_frame, use_container_width=True)
        if summary.feature_importance is not None:
            st.markdown("### Feature Importance")
            st.bar_chart(summary.feature_importance.set_index("feature"))
            lead_feature = summary.feature_importance.iloc[0]["feature"]
            st.write(
                f"The model currently relies most on `{lead_feature}`, which suggests that management "
                "should monitor that driver closely when planning future sales outcomes."
            )
    else:
        st.info("Run the forecast to generate a directionally useful next-period sales estimate.")


def render_insights_summary(bundle: DatasetBundle) -> None:
    """Render a combined insight summary page."""
    st.title("Insights Summary")
    sales = bundle.get("sales_history").frame
    st.markdown("### Sales Insights")
    for insight in build_sales_insight_block(sales):
        st.markdown(f"- {insight}")

    st.markdown("### Marketing Recommendations")
    campaign_bundle = {
        name: bundle.get(name).frame
        for name in [
            "youtube_campaigns",
            "social_media_campaigns",
            "news_magazine_campaigns",
            "tv_radio_campaigns",
        ]
    }
    for recommendation in build_campaign_recommendations(campaign_bundle):
        st.markdown(f"- {recommendation}")


def render_business_experiments(bundle: DatasetBundle) -> None:
    """Render experiment ideas, comparisons, and anomaly checks."""
    st.title("Business Insights & Experiments")
    st.markdown("### Suggested Experiments")
    st.markdown(
        "- Compare high-spend YouTube partnerships against mid-spend social media deals on estimated audience reach."
    )
    st.markdown(
        "- Test whether higher front-page print placements meaningfully outperform baseline magazine frequency."
    )
    st.markdown(
        "- Compare broadcast intensity in TV/radio deals against spend to identify diminishing returns."
    )

    st.markdown("### Segment Comparison")
    tv_radio = bundle.get("tv_radio_campaigns").frame
    comparison = tv_radio.groupby("broadcast_type", dropna=False)["amount_usd"].agg(["count", "mean", "max"])
    st.dataframe(comparison, use_container_width=True)

    st.markdown("### Experiment Simulator")
    youtube_base = bundle.get("youtube_campaigns").frame
    if youtube_base.empty:
        st.warning("Not enough data to simulate experiments.")
    else:
        youtube = youtube_base.copy()
        youtube["estimated_efficiency"] = youtube["average_views"] / youtube["amount_usd"]
        baseline_val = youtube["estimated_efficiency"].median()
        baseline = float(baseline_val) if not pd.isna(baseline_val) else 0.0
        
        valid_creators = youtube["youtuber"].dropna().tolist()
        if not valid_creators:
            st.warning("No valid partners available for simulation.")
        else:
            selected_creator = st.selectbox(
                "Select a YouTube partner for simulation",
                valid_creators,
            )
            improvement_pct = st.slider(
                "Assumed reach improvement (%)",
                min_value=-20,
                max_value=50,
                value=10,
                step=5,
            )
            selected_row = youtube.loc[youtube["youtuber"] == selected_creator].iloc[0]
            projected_efficiency = selected_row["estimated_efficiency"] * (1 + improvement_pct / 100)
            delta_vs_baseline = projected_efficiency - baseline
            st.write(
                f"If `{selected_creator}` improves estimated reach efficiency by {improvement_pct}%, the projected "
                f"efficiency becomes {projected_efficiency:,.1f} views per dollar."
            )
            if delta_vs_baseline > 0:
                st.success(
                    f"This is {delta_vs_baseline:,.1f} views per dollar above the channel median, which suggests the experiment could outperform the baseline mix."
                )
            else:
                st.warning(
                    f"This remains {abs(delta_vs_baseline):,.1f} views per dollar below the channel median, so management should be careful before scaling spend."
                )

    st.markdown("### Anomaly Detection")
    sales_anomalies = detect_anomalies(bundle.get("sales_history").frame, "sales_million_usd")
    st.write(sales_anomalies.explanation)
    st.metric("Anomalous Sales Periods", sales_anomalies.count)
    if sales_anomalies.count:
        st.dataframe(sales_anomalies.frame, use_container_width=True)
    else:
        st.info("No strong sales anomalies were detected in the current cleaned series.")


def render_executive_summary(bundle: DatasetBundle) -> None:
    """Render a recruiter-friendly executive summary."""
    st.title("Executive Summary")
    sales = bundle.get("sales_history").frame

    st.write(
        "Candela Automotives has been refactored from a legacy operations system into a decision-support "
        "analytics prototype focused on sales trends, marketing performance, and business recommendations."
    )

    if sales.empty:
        st.warning("Not enough sales data to generate an executive summary.")
    else:
        latest = sales.iloc[-1]
        best_year = sales.loc[sales["sales_million_usd"].idxmax()]

        st.markdown(
            f"- Latest observed sales: ${latest['sales_million_usd']:,.1f}M in {int(latest['year'])}"
        )
        st.markdown(
            f"- Best historical sales year in the current dataset: {int(best_year['year'])} at ${best_year['sales_million_usd']:,.1f}M"
        )
        st.markdown(
            "- Key recommendation: prioritize channel-mix optimization and target-gap monitoring before scaling spend."
        )
        st.markdown(
            "- Key risk: the legacy repository contains operational data quality issues, so governance and validation remain essential."
        )

        st.markdown("### Management Recommendations")
        recommendations = build_management_recommendations(sales)
        for section, items in recommendations.items():
            st.markdown(f"**{section}**")
            for item in items:
                st.markdown(f"- {item}")


def render_hr_analytics(bundle: DatasetBundle) -> None:
    """Render HR and employee data from live MySQL database."""
    st.title("HR Analytics")
    employee_asset = bundle.get("sqlite_employee")
    dept_asset = bundle.get("sqlite_departments")

    if not employee_asset or employee_asset.frame.empty:
        st.warning("Employee records could not be loaded or are currently unavailable.")
        return

    st.success("Successfully connected to live SQLite backend.")
    employees = employee_asset.frame
    
    st.markdown("### Headcount Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Employees", len(employees))
    if 'SALARY' in employees.columns:
        col2.metric("Average Salary", f"${employees['SALARY'].mean():,.0f}")
        col3.metric("Max Salary", f"${employees['SALARY'].max():,.0f}")
    
    if 'DEPARTMENT' in employees.columns:
        st.markdown("### Department Distribution")
        dept_counts = employees['DEPARTMENT'].value_counts()
        st.bar_chart(dept_counts)
        
    st.markdown("### Employee Records")
    st.dataframe(employees, use_container_width=True)
    
    if dept_asset and not dept_asset.frame.empty:
        st.markdown("### Department Budgets")
        st.dataframe(dept_asset.frame, use_container_width=True)


def render_product_catalog(bundle: DatasetBundle) -> None:
    """Render product catalog from live SQLite database."""
    st.title("Product Catalog Explorer")
    catalog_asset = bundle.get("sqlite_catalog")
    
    if not catalog_asset or catalog_asset.frame.empty:
        st.warning("Catalog records could not be loaded or are currently unavailable.")
        return

    st.success("Successfully connected to live SQLite backend.")
    catalog = catalog_asset.frame
    
    st.markdown("### Active Vehicle Models")
    st.dataframe(catalog, use_container_width=True)
    
    if 'model' in catalog.columns and 'base_price' in catalog.columns:
        st.markdown("### Price Comparison")
        st.bar_chart(catalog.set_index("model")["base_price"])
        
        st.markdown("### Detailed Comparison")
        models = catalog["model"].tolist()
        if len(models) > 0:
            col1, col2 = st.columns(2)
            with col1:
                m1 = st.selectbox("Select Model 1", models, index=0)
                st.dataframe(catalog[catalog["model"] == m1].transpose(), use_container_width=True)
            with col2:
                m2 = st.selectbox("Select Model 2", models, index=min(1, len(models)-1))
                st.dataframe(catalog[catalog["model"] == m2].transpose(), use_container_width=True)


def main() -> None:
    """Run the Streamlit application."""
    st.set_page_config(
        page_title="Candela Automotives Analytics Hub",
        page_icon="CA",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    bundle = load_repository_bundle()

    pages = {
        "Overview": lambda: render_overview(bundle),
        "Dataset Explorer": lambda: render_dataset_explorer(bundle),
        "Trend Analysis": lambda: render_trend_analysis(bundle),
        "Regression Analysis": lambda: render_regression_analysis(bundle),
        "Clustering Analysis": lambda: render_clustering_analysis(bundle),
        "Forecasting & Prediction": lambda: render_forecasting(bundle),
        "Insights Summary": lambda: render_insights_summary(bundle),
        "Business Insights & Experiments": lambda: render_business_experiments(bundle),
        "Executive Summary": lambda: render_executive_summary(bundle),
        "HR Analytics (Live)": lambda: render_hr_analytics(bundle),
        "Product Catalog (Live)": lambda: render_product_catalog(bundle),
    }

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a dashboard section", list(pages))
    pages[page]()


if __name__ == "__main__":
    main()
