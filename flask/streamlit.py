import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data (replace with your file paths)
historical_prices = pd.read_csv(r'C:\Users\user\Desktop\Kifiya\Birhan_Energies\data\Brent Oil Futures Historical Data.csv')
model_predictions = pd.read_csv(r'C:\Users\user\Desktop\Kifiya\Birhan_Energies\data\model_predictions.csv')
#garch_volatility = pd.read_csv(r'C:\Users\user\Desktop\Kifiya\Birhan_Energies\data\garch_volatility.csv')
#event_data = pd.read_csv(r'C:\Users\user\Desktop\Kifiya\Birhan_Energies\data\event_data.csv')

# Model metrics
model_metrics = {"ARIMA_RMSE": 0.0226, "ARIMAX_RMSE": 0.0180, "LSTM_RMSE": 0.0227, "GARCH_Volatility_RMSE": 0.00075}

# Streamlit app
st.title("Brent Oil Dashboard")

# Historical Prices Chart
st.subheader("Historical Prices")
fig1, ax1 = plt.subplots()
ax1.plot(historical_prices['Open'])
st.pyplot(fig1)

# Model Predictions Chart
st.subheader("Model Predictions")
fig2, ax2 = plt.subplots()
if 'Actual' in model_predictions.columns:
    ax2.plot(model_predictions['Actual'], label='Actual')
ax2.plot(model_predictions['ARIMA'], label='ARIMA')
ax2.plot(model_predictions['ARIMAX'], label='ARIMAX')
ax2.legend()
st.pyplot(fig2)



# Model Metrics
st.subheader("Model Metrics")
for metric, value in model_metrics.items():
    st.write(f"{metric}: {value}")