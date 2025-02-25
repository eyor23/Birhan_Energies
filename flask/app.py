from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

try:
    historical_prices = pd.read_csv(r'C:\Users\user\Desktop\Kifiya\Birhan_Energies\data\Brent Oil Futures Historical Data.csv')
    model_predictions = pd.read_csv(r'C:\Users\user\Desktop\Kifiya\Birhan_Energies\data\model_predictions.csv')
    garch_volatility = pd.read_csv(r'C:\Users\user\Desktop\Kifiya\Birhan_Energies\data\garch_volatility.csv')
    #event_data = pd.read_csv(r'C:\Users\user\Desktop\Kifiya\Birhan_Energies\data\event_data.csv')
    model_metrics = {"ARIMA_RMSE": 0.0226, "ARIMAX_RMSE": 0.0180, "LSTM_RMSE": 0.0227, "GARCH_Volatility_RMSE": 0.00075}
except FileNotFoundError:
    historical_prices = None
    model_predictions = None
    garch_volatility = None
    event_data = None
    model_metrics = None

@app.route('/')
def hello():
    return "Welcome to the Brent Oil Dashboard API!"

@app.route('/api/historical_prices', methods=['GET'])
def get_historical_prices():
    print(f"Historical prices data: {historical_prices.head()}") # Add this line
    if historical_prices is not None:
        return jsonify(historical_prices.to_dict(orient='records'))
    else:
        return jsonify({"error": "Historical prices data not available"}), 500

@app.route('/api/model_predictions', methods=['GET'])
def get_model_predictions():
    if model_predictions is not None:
        return jsonify(model_predictions.to_dict(orient='records'))
    else:
        return jsonify({"error": "Model predictions data not available"}), 500

@app.route('/api/garch_volatility', methods=['GET'])
def get_garch_volatility():
    if garch_volatility is not None:
        return jsonify(garch_volatility.to_dict(orient='records'))
    else:
        return jsonify({"error": "GARCH volatility data not available"}), 500


@app.route('/api/model_metrics', methods=['GET'])
def get_model_metrics():
    if model_metrics is not None:
        return jsonify(model_metrics)
    else:
        return jsonify({"error": "Model metrics data not available"}), 500

if __name__ == '__main__':
    app.run(debug=True)