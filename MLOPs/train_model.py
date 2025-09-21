import***REMOVED***os
import***REMOVED***warnings
import***REMOVED***pandas***REMOVED***as***REMOVED***pd
import***REMOVED***numpy***REMOVED***as***REMOVED***np
from***REMOVED***sklearn.model_selection***REMOVED***import***REMOVED***train_test_split
from***REMOVED***sklearn.ensemble***REMOVED***import***REMOVED***RandomForestRegressor
from***REMOVED***sklearn.pipeline***REMOVED***import***REMOVED***Pipeline
from***REMOVED***sklearn.compose***REMOVED***import***REMOVED***ColumnTransformer
from***REMOVED***sklearn.preprocessing***REMOVED***import***REMOVED***OneHotEncoder
import***REMOVED***joblib
import***REMOVED***logging

#***REMOVED***Logging
logging.basicConfig(level=logging.INFO)
logger***REMOVED***=***REMOVED***logging.getLogger(__name__)

warnings.filterwarnings("ignore")
np.random.seed(42)

#***REMOVED***Paths
DATA_PATH***REMOVED***=***REMOVED***"../data/flights.csv"
MODEL_DIR***REMOVED***=***REMOVED***"../models"
MODEL_FILE***REMOVED***=***REMOVED***"flight_price_rf_model.pkl"

def***REMOVED***flight_price_prediction_model():
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Load***REMOVED***data
***REMOVED******REMOVED******REMOVED******REMOVED***data***REMOVED***=***REMOVED***pd.read_csv(DATA_PATH)

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Feature***REMOVED***engineering
***REMOVED******REMOVED******REMOVED******REMOVED***data['date']***REMOVED***=***REMOVED***pd.to_datetime(data['date'])
***REMOVED******REMOVED******REMOVED******REMOVED***data['year']***REMOVED***=***REMOVED***data['date'].dt.year
***REMOVED******REMOVED******REMOVED******REMOVED***data['month']***REMOVED***=***REMOVED***data['date'].dt.month
***REMOVED******REMOVED******REMOVED******REMOVED***data['day']***REMOVED***=***REMOVED***data['date'].dt.day
***REMOVED******REMOVED******REMOVED******REMOVED***data['day_of_week']***REMOVED***=***REMOVED***data['date'].dt.dayofweek
***REMOVED******REMOVED******REMOVED******REMOVED***data['is_weekend']***REMOVED***=***REMOVED***data['day_of_week'].isin([5,6]).astype(int)
***REMOVED******REMOVED******REMOVED******REMOVED***data***REMOVED***=***REMOVED***data.drop(columns=['date',***REMOVED***'travelCode',***REMOVED***'userCode'],***REMOVED***errors='ignore')

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Separate***REMOVED***features/target
***REMOVED******REMOVED******REMOVED******REMOVED***X***REMOVED***=***REMOVED***data.drop(columns=['price'])
***REMOVED******REMOVED******REMOVED******REMOVED***y***REMOVED***=***REMOVED***data['price']

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Categorical***REMOVED***and***REMOVED***numerical***REMOVED***columns
***REMOVED******REMOVED******REMOVED******REMOVED***categorical_cols***REMOVED***=***REMOVED***['from',***REMOVED***'to',***REMOVED***'flightType',***REMOVED***'agency']
***REMOVED******REMOVED******REMOVED******REMOVED***numeric_cols***REMOVED***=***REMOVED***['time',***REMOVED***'distance',***REMOVED***'day',***REMOVED***'month',***REMOVED***'year',***REMOVED***'day_of_week']

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Preprocessing***REMOVED***pipelines
***REMOVED******REMOVED******REMOVED******REMOVED***preprocessor***REMOVED***=***REMOVED***ColumnTransformer(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***transformers=[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('cat',***REMOVED***OneHotEncoder(handle_unknown='ignore'),***REMOVED***categorical_cols),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('num',***REMOVED***'passthrough',***REMOVED***numeric_cols)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED***)

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Model***REMOVED***pipeline
***REMOVED******REMOVED******REMOVED******REMOVED***model***REMOVED***=***REMOVED***Pipeline(steps=[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('preprocessor',***REMOVED***preprocessor),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('regressor',***REMOVED***RandomForestRegressor(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***n_estimators=200,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***max_depth=15,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***min_samples_split=10,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***random_state=42,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***n_jobs=-1
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***))
***REMOVED******REMOVED******REMOVED******REMOVED***])

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Train/test***REMOVED***split
***REMOVED******REMOVED******REMOVED******REMOVED***X_train,***REMOVED***X_test,***REMOVED***y_train,***REMOVED***y_test***REMOVED***=***REMOVED***train_test_split(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***X,***REMOVED***y,***REMOVED***test_size=0.2,***REMOVED***random_state=42
***REMOVED******REMOVED******REMOVED******REMOVED***)

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Train***REMOVED***model
***REMOVED******REMOVED******REMOVED******REMOVED***model.fit(X_train,***REMOVED***y_train)
***REMOVED******REMOVED******REMOVED******REMOVED***logger.info(f"Model***REMOVED***trained***REMOVED***on***REMOVED***{X_train.shape[0]}***REMOVED***rows.")

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Save***REMOVED***model
***REMOVED******REMOVED******REMOVED******REMOVED***os.makedirs(MODEL_DIR,***REMOVED***exist_ok=True)
***REMOVED******REMOVED******REMOVED******REMOVED***model_path***REMOVED***=***REMOVED***os.path.join(MODEL_DIR,***REMOVED***MODEL_FILE)
***REMOVED******REMOVED******REMOVED******REMOVED***joblib.dump(model,***REMOVED***model_path)
***REMOVED******REMOVED******REMOVED******REMOVED***logger.info(f"Model***REMOVED***saved***REMOVED***at***REMOVED***{model_path}")

***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***model,***REMOVED***X_test,***REMOVED***y_test

if***REMOVED***__name__***REMOVED***==***REMOVED***"__main__":
***REMOVED******REMOVED******REMOVED******REMOVED***flight_price_prediction_model()

