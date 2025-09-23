from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import os
from flask_cors import CORS, cross_origin
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Get model path
MODEL_PATH = "models/RandomForest_flight_model.pkl"

# Load model
model = joblib.load(MODEL_PATH)

REQUIRED_FIELDS = ["from", "to", "flightType", "agency", "time", "distance", "year", "month", "day", "day_of_week"]

def parse_and_engineer(payload: dict) -> pd.DataFrame:
    # Basic validation
    missing = [f for f in REQUIRED_FIELDS if f not in payload]
    if missing:
        raise ValueError(f"Missing fields: {missing}")

    # Parse/convert
    def parse_numeric(value):
        if isinstance(value, (int, float)):
            return float(value)
        value = str(value).strip()
        if ":" in value:  # handle HH:MM
            h, m = map(int, value.split(":"))
            return h + m / 60.0
        return float(value)

    try:
        time_val = parse_numeric(payload["time"])
        dist_val = parse_numeric(payload["distance"])
    except Exception:
        raise ValueError("`time` and `distance` must be int, float, numeric string, or HH:MM format.")

    row = {
        "from": payload["from"],
        "to": payload["to"],
        "flightType": payload["flightType"],
        "agency": payload["agency"],
        "time": time_val,
        "distance": dist_val,
        "year": int(payload["year"]),
        "month": int(payload["month"]),
        "day": int(payload["day"]),
        "day_of_week": int(payload["day_of_week"])
    }
    return pd.DataFrame([row])

# Routes

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "model_loaded": MODEL_PATH})

@app.route("/predict", methods=["GET", "POST"])
def predict():
    try:
        if request.method == "POST":
            # Expect JSON body
            payload = request.get_json(force=True)
        else:
            # Expect query parameters
            from_ = request.args.get("from")
            to = request.args.get("to")
            distance = request.args.get("distance")
            flightType = request.args.get("flightType")
            agency = request.args.get("agency")
            time = request.args.get("time")
            year = request.args.get("year")
            month = request.args.get("month")
            day = request.args.get("day")
            day_of_week = request.args.get("day_of_week")

            if not all([from_, to, distance, flightType, agency, time, year, month, day, day_of_week]):
                return jsonify({"error": "Missing one or more required query parameters."}), 400

            payload = {
                "from": from_,
                "to": to,
                "flightType": flightType,
                "agency": agency,
                "time": time,
                "distance": distance,
                "year": year,
                "month": month,
                "day": day,
                "day_of_week": day_of_week
            }

        # Process input
        X = parse_and_engineer(payload)
        feature_order = REQUIRED_FIELDS
        X = X[feature_order]

        pred = float(model.predict(X)[0])
        return jsonify({"predicted_price": round(pred, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/predict-batch", methods=["POST"])
def predict_batch():
    try:
        data = request.get_json(force=True)
        records = data.get("records", [])
        if not isinstance(records, list) or len(records) == 0:
            return jsonify({"error": "`records` must be a non-empty list"}), 400

        frames = [parse_and_engineer(r) for r in records]
        X = pd.concat(frames, ignore_index=True)
        preds = model.predict(X).tolist()
        preds = [round(float(p), 2) for p in preds]
        return jsonify({"predicted_prices": preds})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
