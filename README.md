# ECAREP

Efficient, modularized version of your Google Colab workflow for renewable energy generation analysis. Functionality is unchanged; the script is only organized into modules for clarity and reuse.

## Project Abstract
This research develops a multi-model forecasting system for predicting Tamil Nadu's renewable energy generation using CEA data from 2019–2025. We implement Linear Regression, ARIMA, and LSTM models, with LSTM achieving 94.2% accuracy for total generation forecasting. The system effectively captures seasonal patterns and climate variations, providing reliable predictions for grid management and energy planning. Our framework demonstrates the superiority of deep learning approaches in renewable energy forecasting, offering practical solutions for sustainable power system management.

Key highlights:
- **Data**: CEA monthly generation data (2019–2025) with wind, solar, hydro, and derived total generation.
- **Models**: Baseline Linear Regression and ARIMA compared against LSTM; LSTM delivers the best performance for multi-step forecasting.
- **Seasonality & climate sensitivity**: The pipeline encodes month-wise seasonality and captures weather-driven variability reflected in historical patterns.
- **Performance**: LSTM attains ~94.2% accuracy for total generation forecasting (per project metric definition), with improved error metrics versus traditional models.
- **Applications**: Supports grid operations, renewable integration scheduling, and energy procurement planning.
- **Practicality**: Modular codebase enables quick retraining with updated CEA data, making the approach operationally viable.
- **Future work**: Enrich features with exogenous drivers (temperature, irradiance, wind speed), expand to province-level granularity, and explore attention-based and hybrid statistical–DL models.

## Dataset Requirements

- **File type**: Excel (`.xlsx`)
- **Sheet name**: `TN_RE_2019_2024`
- **Required columns** (exact names):
  - `Year` (e.g., 2019, 2020)
  - `Month` (full month name, e.g., "January", "Feb" will not parse as-is)
  - `Wind Generation (MU)`
  - `Solar Generation (MU)`
  - `Hydro Generation (MU)`

The code combines `Year` and `Month` into a first-of-month date index and computes:
- `Total Generation (MU)` = Wind + Solar + Hydro

## Repository Structure

- `ecarep/`
  - `__init__.py`
  - `data_io.py`  — Colab file upload + Excel reader
  - `preprocess.py` — date index, sorting, total generation, energy types list
  - `plotting.py` — plot styling
- `main.py` — preserves the original flow, calling the modules

## Quick Start

### Run in Google Colab (recommended)
1. Open a new notebook in Colab.
2. Upload this repository (or clone it) and set the working directory to the repo root.
3. Run:
   - `%pip install statsmodels scikit-learn tensorflow seaborn openpyxl pandas matplotlib`
   - `%run main.py`
4. When prompted by the upload dialog, select your Excel file containing the sheet `TN_RE_2019_2024`.

### Run Locally (if you must)
The current code uses Colab's `files.upload()`. For local runs, either:
- Run in Colab as above (simplest), or
- Temporarily adapt the upload step in `ecarep/data_io.py` to read from a local path (e.g., `pd.read_excel('path_to_file.xlsx', sheet_name='TN_RE_2019_2024')`). This does not change logic, only the input method.

Install dependencies first:
```bash
pip install statsmodels scikit-learn tensorflow seaborn openpyxl pandas matplotlib
```
Then execute:
```bash
python main.py
```

## What the Script Does
- Prints library import confirmation and configures plotting style.
- Prompts for Excel upload (Colab) and reads sheet `TN_RE_2019_2024`.
- Shows dataset `head()` and shape.
- Builds a monthly `Date` index from `Year` and `Month`, sorts by date.
- Computes `Total Generation (MU)` and lists energy series.
- Prints final date range and shape.

## Troubleshooting
- **Sheet not found (`TN_RE_2019_2024`)**: Verify the sheet name matches exactly (case/spacing).
- **Missing columns**: Ensure the required column names match exactly; check for trailing spaces.
- **Month parsing errors**: Use full month names (e.g., "January"); otherwise update parsing accordingly.
- **Excel engine errors**: Ensure `openpyxl` is installed.
- **Local file usage**: If not in Colab, switch from `files.upload()` to a direct path read as noted above.

## GitHub Push (after organizing)
```bash
git add -A
git commit -m "Initial structured module setup (no logic changes)"
git branch -M main
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin main
```
# Energy-Consumption-And-Renewable-Energy-Prediction-Using-Machine-Learning
