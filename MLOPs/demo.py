import os
import warnings
import sys
import joblib

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import dagshub
import logging

# Initialize Dagshub and MLflow
dagshub.init(repo_owner='aatkameraj1425', repo_name='MLFlow_Voyage_Analytics', mlflow=True)

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

warnings.filterwarnings("ignore")
np.random.seed(42)

# Paths
DATA_PATH = "../data/flights.csv"
MODEL_DIR = "../models"

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

if __name__ == "__main__":
    data = pd.read_csv(DATA_PATH)

    # Feature engineering
    data['date'] = pd.to_datetime(data['date'])
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['day_of_week'] = data['date'].dt.dayofweek
    data['is_weekend'] = data['day_of_week'].isin([5,6]).astype(int)
    data = data.drop(columns=['date', 'travelCode', 'userCode'], errors='ignore')

    # Split features/target
    X = data.drop(columns=['price'])
    y = data['price']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model_files = {
        "RandomForest": "RandomForest_flight_model.pkl",
        "GradientBoost": "GradientBoost_flight_model.pkl",
        "XGBoost": "XGBoost_flight_model.pkl",
        "LinearRegression": "LinearRegression_flight_model.pkl"
    }

    # Loop through models
    for model_name, model_file in model_files.items():
        model_path = os.path.join(MODEL_DIR, model_file)
        if not os.path.exists(model_path):
            logger.warning(f"Model file {model_path} not found, skipping...")
            continue

        model = joblib.load(model_path)

        # Run predictions on test data
        y_pred = model.predict(X_test)

        # Evaluate metrics
        rmse, mae, r2 = eval_metrics(y_test, y_pred)

        print(f"\nModel: {model_name}")
        print(f"RMSE: {rmse}")
        print(f"MAE: {mae}")
        print(f"R2: {r2}")

        # Log with MLflow
        with mlflow.start_run():
            mlflow.log_param("model_type", model_name)
            mlflow.log_param("train_rows", X_train.shape[0])
            mlflow.log_param("test_rows", X_test.shape[0])
            mlflow.log_param("features", X.shape[1])

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # Set remote tracking
            remote_server_uri = "https://dagshub.com/aatkameraj1425/MLFlow_Voyage_Analytics.mlflow"
            mlflow.set_tracking_uri(remote_server_uri)

            # Log the model
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="model")
            else:
                mlflow.sklearn.log_model(model, "model")

    logger.info("All models evaluated and logged successfully.")
