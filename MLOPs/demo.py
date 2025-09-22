import***REMOVED***os
import***REMOVED***warnings
import***REMOVED***sys
import***REMOVED***joblib

import***REMOVED***pandas***REMOVED***as***REMOVED***pd
import***REMOVED***numpy***REMOVED***as***REMOVED***np
from***REMOVED***sklearn.metrics***REMOVED***import***REMOVED***mean_squared_error,***REMOVED***mean_absolute_error,***REMOVED***r2_score
from***REMOVED***sklearn.model_selection***REMOVED***import***REMOVED***train_test_split

from***REMOVED***urllib.parse***REMOVED***import***REMOVED***urlparse
import***REMOVED***mlflow

import***REMOVED***mlflow.sklearn
import***REMOVED***dagshub
import***REMOVED***logging

#***REMOVED***Initialize***REMOVED***Dagshub***REMOVED***and***REMOVED***MLflow
dagshub.init(repo_owner='aatkameraj1425',***REMOVED***repo_name='MLFlow_Voyage_Analytics',***REMOVED***mlflow=True)

logging.basicConfig(level=logging.WARN)
logger***REMOVED***=***REMOVED***logging.getLogger(__name__)***REMOVED******REMOVED***

warnings.filterwarnings("ignore")
np.random.seed(42)

#***REMOVED***Paths
DATA_PATH***REMOVED***=***REMOVED***"../data/flights.csv"
MODEL_DIR***REMOVED***=***REMOVED***"../models"

def***REMOVED***eval_metrics(actual,***REMOVED***pred):
***REMOVED******REMOVED******REMOVED******REMOVED***rmse***REMOVED***=***REMOVED***np.sqrt(mean_squared_error(actual,***REMOVED***pred))
***REMOVED******REMOVED******REMOVED******REMOVED***mae***REMOVED***=***REMOVED***mean_absolute_error(actual,***REMOVED***pred)
***REMOVED******REMOVED******REMOVED******REMOVED***r2***REMOVED***=***REMOVED***r2_score(actual,***REMOVED***pred)
***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***rmse,mae,***REMOVED***r2

if***REMOVED***__name__==***REMOVED***"__main__":

***REMOVED******REMOVED******REMOVED******REMOVED***data***REMOVED***=***REMOVED***pd.read_csv(DATA_PATH)
***REMOVED******REMOVED******REMOVED***

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Feature***REMOVED***engineering***REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***data['date']***REMOVED***=***REMOVED***pd.to_datetime(data['date'])
***REMOVED******REMOVED******REMOVED******REMOVED***data['year']***REMOVED***=***REMOVED***data['date'].dt.year
***REMOVED******REMOVED******REMOVED******REMOVED***data['month']***REMOVED***=***REMOVED***data['date'].dt.month
***REMOVED******REMOVED******REMOVED******REMOVED***data['day']***REMOVED***=***REMOVED***data['date'].dt.day
***REMOVED******REMOVED******REMOVED******REMOVED***data['day_of_week']***REMOVED***=***REMOVED***data['date'].dt.dayofweek
***REMOVED******REMOVED******REMOVED******REMOVED***data['is_weekend']***REMOVED***=***REMOVED***data['day_of_week'].isin([5,6]).astype(int)
***REMOVED******REMOVED******REMOVED******REMOVED***data***REMOVED***=***REMOVED***data.drop(columns=['date',***REMOVED***'travelCode',***REMOVED***'userCode'],***REMOVED***errors='ignore')

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Split***REMOVED***features/target
***REMOVED******REMOVED******REMOVED******REMOVED***X***REMOVED***=***REMOVED***data.drop(columns=['price'])
***REMOVED******REMOVED******REMOVED******REMOVED***y***REMOVED***=***REMOVED***data['price']

***REMOVED******REMOVED******REMOVED******REMOVED***X_train,***REMOVED***X_test,***REMOVED***y_train,***REMOVED***y_test***REMOVED***=***REMOVED***train_test_split(
***REMOVED******REMOVED******REMOVED******REMOVED***X,***REMOVED***y,***REMOVED***test_size=0.2,***REMOVED***random_state=42
***REMOVED******REMOVED******REMOVED******REMOVED***)

***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***model_files={***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***"RandomForest":***REMOVED***"RandomForest_flight_model.pkl",
***REMOVED******REMOVED******REMOVED******REMOVED***"GradientBoost":***REMOVED***"GradientBoost_flight_model.pkl",
***REMOVED******REMOVED******REMOVED******REMOVED***"XGBoost":***REMOVED***"XGBoost_flight_model.pkl",
***REMOVED******REMOVED******REMOVED******REMOVED***"LinearRegression":***REMOVED***"LinearRegression_flight_model.pkl"
***REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***loop***REMOVED***through***REMOVED***models
***REMOVED******REMOVED******REMOVED******REMOVED***for***REMOVED***model_name,***REMOVED***model_file***REMOVED***in***REMOVED***model_files.items():
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***model_path***REMOVED***=***REMOVED***os.path.join(MODEL_DIR,***REMOVED***model_file)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if***REMOVED***not***REMOVED***os.path.exists(model_path):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***logger.warning(f"Model***REMOVED***file***REMOVED***{model_path}***REMOVED***not***REMOVED***found,***REMOVED***skipping...")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***continue

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***model***REMOVED***=***REMOVED***joblib.load(model_path)

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Run***REMOVED***predictions***REMOVED***on***REMOVED***test***REMOVED***data
***REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***y_pred***REMOVED***=***REMOVED***model.predict(X_test)

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Evaluate***REMOVED***metrics
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***rmse,***REMOVED***mae,***REMOVED***r2***REMOVED***=***REMOVED***eval_metrics(y_test,***REMOVED***y_pred)

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***print(f"\nModel:***REMOVED***{model_name}")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***print(f"RMSE:***REMOVED***{rmse}")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***print(f"MAE:***REMOVED***{mae}")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***print(f"R2:***REMOVED***{r2}")

***REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Log***REMOVED***with***REMOVED***MLflow
***REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***with***REMOVED***mlflow.start_run():
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***mlflow.log_param("model_type",***REMOVED***model_name)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***mlflow.log_param("train_rows",***REMOVED***X_train.shape[0])
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***mlflow.log_param("test_rows",***REMOVED***X_test.shape[0])
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***mlflow.log_param("features",***REMOVED***X.shape[1])
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***mlflow.log_metric("rmse",***REMOVED***rmse)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***mlflow.log_metric("mae",***REMOVED***mae)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***mlflow.log_metric("r2",***REMOVED***r2)

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Set***REMOVED***remote***REMOVED***tracking
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***remote_server_uri***REMOVED***=***REMOVED***"https://dagshub.com/aatkameraj1425/MLFlow_Voyage_Analytics.mlflow"
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***mlflow.set_tracking_uri(remote_server_uri)

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***log***REMOVED***the***REMOVED***model

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***tracking_url_type_store***REMOVED***=***REMOVED***urlparse(mlflow.get_tracking_uri()).scheme
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if***REMOVED***tracking_url_type_store***REMOVED***!=***REMOVED***"file":
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***mlflow.sklearn.log_model(model,***REMOVED***"model",***REMOVED***registered_model_name="model")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***mlflow.sklearn.log_model(model,***REMOVED***"model")***REMOVED******REMOVED***

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***logger.info("All***REMOVED***models***REMOVED***evaluated***REMOVED***and***REMOVED***logged***REMOVED***successfully.")***REMOVED******REMOVED***