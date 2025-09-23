import os
import sys
import joblib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.flight_price_prediction import logger
from src.flight_price_prediction.utils.common import load_bin, prepare_features, predict_price

if __name__ == "__main__":
    logger.info("Demo script is running successfully!")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH = os.path.join(BASE_DIR, "..", "artifacts", "flight_price_rf_model.pkl")

    model = joblib.load(MODEL_PATH)
    logger.info(f"Model loaded from {MODEL_PATH}")

    # Define feature order as used during training
    FEATURE_ORDER = [
        "from", "to", "flightType", "agency",
        "time", "distance", "year", "month", "day", "day_of_week"
    ]

    sample_input = {
        "from": "DEL",
        "to": "BOM",
        "flightType": "Economy",
        "agency": "AirIndia",
        "time": 10.5,
        "year": 2023,
        "month": 9,
        "day": 12,
        "day_of_week": 2
    }

    # Prepare features in correct order
    X = prepare_features(sample_input, FEATURE_ORDER)

    # Predict price
    price = predict_price(model, X)

    print(f"Predicted Price for {sample_input['from']} -> {sample_input['to']}: {round(price, 2)}")
