# Candela Automotives - Final Deliverable

This document summarizes the modernization and analytics transformation applied to the `Candela-Automotives` project, evolving it from a legacy CLI operations system into a professional decision-support dashboard suitable for AI Strategy and Business Intelligence demonstrations.

## 1. Architecture Summary
The repository has been refactored to support a modular, decoupled architecture, while preserving the legacy system's original files. The new analytical dashboard is organized as follows:
- **`app.py`**: The main Streamlit entry point routing to individual dashboard modules.
- **`dashboard/`**: Contains reusable UI components and shared text blocks to enforce a clean, corporate visual layout.
- **`analytics/`**: Houses the core business logic, separated into functional domains:
  - `anomalies.py`: Outlier detection using IQR and z-scores.
  - `clustering.py`: KMeans segmentation for campaign data.
  - `forecasting.py`: Random Forest regression for future trend predictions.
  - `insights.py`: Plain-English automated business interpretations.
  - `kpis.py`: Revenue, profit, and growth metric calculations.
  - `regression.py`: Linear and polynomial regression tools.
  - `trends.py`: Moving average and period-over-period growth calculators.
- **`data/`**: Manages stable data loading, preprocessing, and the unified `DatasetBundle` to serve cleaned DataFrames to the UI without touching disk repeatedly.
- **`reports/`**: Houses the detailed `BUG_FIX_LOG.md` tracking all historical defect resolutions.

## 2. Files Created
- `app.py`
- `requirements.txt`
- `SETUP.md`
- `analytics/__init__.py`, `analytics/anomalies.py`, `analytics/clustering.py`, `analytics/forecasting.py`, `analytics/insights.py`, `analytics/kpis.py`, `analytics/regression.py`, `analytics/trends.py`
- `dashboard/__init__.py`, `dashboard/components.py`, `dashboard/text_blocks.py`
- `data/__init__.py`, `data/loader.py`, `data/preprocessing.py`, `data/repositories.py`
- `reports/BUG_FIX_LOG.md`
- Tracking docs: `../PROJECT_AUDIT.md`, `../PROGRESS.md`, `../TODO.md`, `../CURRENT_STATE.md`

## 3. Files Modified
- `MARKETING/Marketing.py`: Migrated to safe relative package imports and robust file pathing.
- `MARKETING/__init__.py`: Created to establish package context.
- `Plms/plma.py`: Migrated to safe relative package imports and robust file pathing.
- `Plms/__init__.py`: Created to establish package context.
- `HR_software.py`: Removed unsafe `eval` usage and repaired flawed SQL queries.
- `Finance_software.py`: Corrected broken pricing update SQL statements and ensured commits.
- `purchase_software.py`: Fixed SQL syntax referencing non-existent legacy schema columns.

## 4. Bugs Fixed
- **Module Resolution**: Added `__init__.py` files and replaced brittle working-directory dependent imports with package-relative imports, preventing `ModuleNotFoundError` crashes.
- **Data Pathing**: Replaced hardcoded string paths for CSV assets with dynamic `pathlib.Path` resolutions, ensuring data loads reliably regardless of terminal launch location.
- **Security & Parsing**: Replaced unsafe `eval(input())` statements in HR workflows with safe `ast.literal_eval` via robust helper functions.
- **SQL Integrity**: Repaired multiple malformed SQL statements (missing columns in `INSERT` operations, incorrect boolean logic in `SET` clauses, referencing ghost columns like `MATERIALS`).
- **UI Stability**: Added defensive empty-dataframe checks throughout all `app.py` pages and `analytics` functions. The dashboard now gracefully intercepts missing data scenarios and displays recruiter-friendly warnings instead of generating `IndexError` or `ValueError` crashes.

## 5. Features Added
- **Streamlit Analytics Dashboard**: A comprehensive web UI serving multiple distinct analytical views.
- **Dataset Explorer**: Features schema visualization, missing value summaries, descriptive statistics, and a dynamic correlation heatmap for numeric data.
- **Business KPI Engine**: Calculates macro metrics (Total Revenue, Margin, Target Gaps, MoM Growth) across available datasets.
- **Trend Analysis**: Visualizes sales performance against targets using moving averages and growth rate overlays.
- **Regression Analysis**: Evaluates linear and polynomial fits to highlight structural growth direction vs. short-term variance.
- **Campaign Clustering**: Uses KMeans to automatically segment marketing influencers by scale, spend, and reach.
- **Random Forest Forecasting**: Predicts next-period sales trends and extracts feature importance (e.g., highlighting profit margins or historical targets) driving the model's logic.
- **Business Experiment Simulator**: Allows users to tweak hypothetical reach-improvements on historical marketing deals to model potential efficiency gains vs. the channel median.
- **Automated Insights Generation**: Translates raw data (like regression R² or clustering labels) into plain-English management recommendations, highlighting risks and actionable opportunities.

## 6. Run Instructions
To run the modern analytics dashboard:

1. Ensure you have Python 3.9+ installed.
2. Open a terminal and navigate to the project directory:
   ```bash
   cd Candela-Automotives
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```
5. The dashboard will automatically open in your default web browser (typically at `http://localhost:8501`).

## 7. Future Improvements
- **Environment Variable Configuration**: Migrate the legacy hardcoded MySQL credentials to a secure `.env` file structure via `python-dotenv`.
- **Live Database Integration**: Transition the new dashboard analytics pages from offline CSV assets to live querying of the initialized MySQL schema, enabling real-time operations tracking.
- **Expanded Unit Testing**: Add a `tests/` directory with `pytest` coverage specifically targeting the `analytics/` math helpers to guarantee stability during future model enhancements.
- **Unified CI/CD**: Implement GitHub Actions to lint code (PEP8) and automatically run the test suite on new pull requests.
