import os
import warnings
import sys
import joblib

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
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

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse,mae, r2

if __name__== "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(42)


    data = pd.read_csv("data/flights.csv")


    # Feature engineering (same as training)
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

    # Load trained pipeline
    
    model = joblib.load("flight_price_pipeline.pkl")

    # Run predictions on test data
   
    y_pred = model.predict(X_test)

    # Evaluate metrics
    rmse, mae, r2 = eval_metrics(y_test, y_pred)

    print(f"RMSE: {rmse}")
    print(f"MAE: {mae}")
    print(f"R2: {r2}")

  
    # Log with MLflow
   
    with mlflow.start_run():
        mlflow.log_param("model_type", "RandomForestRegressor_Pipeline")
        mlflow.log_param("train_rows", X_train.shape[0])
        mlflow.log_param("test_rows", X_test.shape[0])
        
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        # Log the pipeline itself
        #mlflow.sklearn.log_model(model, "model")

        # Set remote tracking for Dagshub
        remote_server_uri = "https://dagshub.com/aatkameraj1425/MLFlow_Voyage_Analytics.mlflow"
        
        mlflow.set_tracking_uri(remote_server_uri)

        # log the model

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        if tracking_url_type_store != "file":
            mlflow.sklearn.log_model(model, "model", registered_model_name="FlightPriceModel")
        else:
            mlflow.sklearn.log_model(model, "model")    