import os
import warnings
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
import xgboost as xgb
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib
import logging

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

warnings.filterwarnings("ignore")
np.random.seed(42)

# Paths
DATA_PATH = "../data/flights.csv"
MODEL_DIR = "../models"

def flight_price_prediction_model():
    # Load data
    data = pd.read_csv(DATA_PATH)

    # Feature engineering
    data['date'] = pd.to_datetime(data['date'])
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['day_of_week'] = data['date'].dt.dayofweek
    data['is_weekend'] = data['day_of_week'].isin([5,6]).astype(int)
    data = data.drop(columns=['date', 'travelCode', 'userCode'], errors='ignore')

    # Separate features/target
    X = data.drop(columns=['price'])
    y = data['price']

    # Categorical and numerical columns
    categorical_cols = ['from', 'to', 'flightType', 'agency']
    numeric_cols = ['time', 'distance', 'day', 'month', 'year', 'day_of_week']

    # Preprocessing pipelines
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
            ('num', 'passthrough', numeric_cols)
        ]
    )

    # Define all models
    models = {
        "RandomForest": RandomForestRegressor(
            n_estimators=200,
            max_depth=15,
            min_samples_split=10,
            random_state=42,
            n_jobs=-1
        ),
        "GradientBoost": GradientBoostingRegressor(
            n_estimators=200,
            max_depth=5,
            random_state=42
        ),
        "XGBoost": xgb.XGBRegressor(
            n_estimators=200,
            max_depth=5,
            random_state=42,
            verbosity=0
        ),
        "LinearRegression": LinearRegression()
    }

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    trained_models = {}

    # Train, save, and log each model
    for name, estimator in models.items():
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', estimator)
        ])
        pipeline.fit(X_train, y_train)
        logger.info(f"{name} model trained on {X_train.shape[0]} rows.")

        # Save model
        os.makedirs(MODEL_DIR, exist_ok=True)
        model_path = os.path.join(MODEL_DIR, f"{name}_flight_model.pkl")
        joblib.dump(pipeline, model_path)
        logger.info(f"{name} model saved at {model_path}")

        trained_models[name] = (pipeline, X_test, y_test)

    return trained_models

if __name__ == "__main__":
    flight_price_prediction_model()
