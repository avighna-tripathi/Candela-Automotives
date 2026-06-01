# Bug Fix Log

## Pending
- Phase 0 documented the initial defects and refactor risks.

## Phase 1 Foundation Work
- Added a clean modular application scaffold without removing or mutating the legacy CLI modules.
- Added package-safe `__init__.py` files for the new dashboard code.
- Added cleaned dataset loaders that use stable repository-relative paths instead of the legacy working-directory assumptions.
- Added defensive preprocessing for malformed numeric and currency fields in the existing CSV assets.

## Phase 2 Bug Fixes
- Added proper `__init__.py` files to the legacy `MARKETING` package tree and the `Plms` package to fix broken package discovery.
- Updated `MARKETING/Marketing.py` to use relative package imports instead of brittle top-level imports.
- Updated `Plms/plma.py` to use relative package imports instead of working-directory-dependent imports.
- Replaced hardcoded CSV filename access in legacy marketing and PLMS modules with repository-relative `Path` handling.
- Replaced unsafe `eval(input(...))` parsing in `HR_software.py` with `ast.literal_eval(...)` through a helper function.
- Fixed the HR employee insert statement to provide all required columns for the `employee` table.
- Fixed invalid HR update statements that used `AND` instead of comma-separated assignments in `SET` clauses.
- Corrected `NO_WARNING` references to `NO_WARNINGS` to match the seeded schema.
- Fixed the finance catalog price update to increase prices rather than decrease them and added the missing commit.
- Corrected multiple purchase/store SQL column references from nonexistent names such as `MATERIALS`, `QUANTITY`, and `UNIT_MEASURE` to the seeded schema names.

## Post-Fix Hardening
- Replaced the corrupted `R²` UI label in the dashboard regression page with a stable ASCII `R2` display to avoid encoding artifacts.
- Added anomaly detection and KPI utilities that handle missing numeric values defensively instead of assuming complete clean data.
- Added forecasting support for feature-importance display when the required ML dependency is installed, while still degrading gracefully when it is not.
- Installed and validated the missing runtime dependencies `scikit-learn`, `matplotlib`, and `mysql-connector-python`.
- Confirmed the forecasting module now returns feature-importance output after dependency installation.

## Phase 3 Hardening
- Added defensive `dataframe.empty` checks in `app.py` UI rendering components to prevent `IndexError` and `ValueError` crashes on incomplete data.
- Guarded `analytics/insights.py` generation functions to gracefully provide fallback insights when required data is missing.
- Added missing `import pandas as pd` to `app.py`.
- Safely added dynamic correlation heatmaps to the Dataset Explorer without breaking existing UI logic.
