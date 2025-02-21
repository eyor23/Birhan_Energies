```markdown

Prepared by Eyor Getachew (@eyor23)
# Brent Oil Price Event Impact Analysis

This project analyzes the impact of significant events on Brent oil price changes over the past decade. It uses time series analysis, econometric modeling, and statistical techniques to identify key events, quantify their effects on price fluctuations, and provide data-driven insights for investors, policymakers, and energy companies.

## Project Overview

The volatility of oil prices makes it challenging for stakeholders to make informed decisions. This project aims to provide clarity by:

* Identifying key events that have significantly impacted Brent oil prices.
* Measuring the magnitude and direction of these impacts.
* Generating actionable insights to guide investment strategies, policy development, and operational planning.

## Data

The project uses historical Brent oil price data and a curated dataset of significant events (geopolitical events, economic events, OPEC decisions, supply disruptions, etc.) over the past decade.

## Methodology

The analysis employs a combination of techniques:

* **Exploratory Data Analysis (EDA):**  Visualizing price changes, calculating descriptive statistics, and examining autocorrelation and volatility.
* **Event Study Methodology:**  Quantifying the abnormal returns in oil prices around specific event dates.
* **Regression Analysis:**  Modeling the relationship between price changes and event indicators.
* **ARIMAX Modeling:** Incorporating event indicators as exogenous variables in ARIMA models to account for both autocorrelation and event impacts.
* **GARCH Modeling:** Modeling the volatility of price changes, which is crucial for oil price analysis.

## Project Structure


brent_oil_analysis/
├── data/              # Contains the raw and processed data
│   ├── BrentOilPrices.csv
│   └── change_points.csv
├── notebooks/         # Jupyter notebooks for data exploration and modeling
│   ├── eda.ipynb
│   ├── event_study.ipynb
│   ├── regression_analysis.ipynb
│   ├── arimax_modeling.ipynb
│   └── garch_modeling.ipynb
├── scripts/           # Python scripts for data processing and model building (if any)
│   └── process_data.py
├── dashboard/        # Flask and React code for the interactive dashboard
│   ├── backend/
│   │   └── app.py
│   └── frontend/
│   │   └── ...
├── requirements.txt  # List of required Python packages
└── README.md         # This file


## Requirements

To run the analysis, you will need the following Python packages:


pandas
numpy
matplotlib
statsmodels
scikit-learn
warnings
ruptures


You can install these packages using pip:

```bash
pip install -r requirements.txt

For the dashboard, you will need Node.js and npm (or yarn) to install the React dependencies.

## Running the Analysis

1. Clone the repository: `git clone [repository URL]`
2. Navigate to the project directory: `cd brent_oil_analysis`
3. Install the Python requirements: `pip install -r requirements.txt`
4. Run the Jupyter notebooks in the `notebooks/` directory to perform the analysis.


## Contributing


## License


```
