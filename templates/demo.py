import***REMOVED***os
import***REMOVED***sys
import***REMOVED***joblib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),***REMOVED***"..")))

from***REMOVED***src.flight_price_prediction***REMOVED***import***REMOVED***logger
from***REMOVED***src.flight_price_prediction.utils.common***REMOVED***import***REMOVED***load_bin,***REMOVED***prepare_features,***REMOVED***predict_price


if***REMOVED***__name__***REMOVED***==***REMOVED***"__main__":
***REMOVED******REMOVED******REMOVED******REMOVED***logger.info("Demo***REMOVED***script***REMOVED***is***REMOVED***running***REMOVED***successfully!")

BASE_DIR***REMOVED***=***REMOVED***os.path.dirname(os.path.abspath(__file__))
MODEL_PATH***REMOVED***=***REMOVED***os.path.join(BASE_DIR,***REMOVED***"..",***REMOVED***"artifacts",***REMOVED***"flight_price_rf_model.pkl")

model***REMOVED***=***REMOVED***joblib.load(MODEL_PATH)
logger.info(f"Model***REMOVED***loaded***REMOVED***from***REMOVED***{MODEL_PATH}")

#***REMOVED***Define***REMOVED***feature***REMOVED***order***REMOVED***as***REMOVED***used***REMOVED***during***REMOVED***training
FEATURE_ORDER***REMOVED***=***REMOVED***["from",***REMOVED***"to",***REMOVED***"flightType",***REMOVED***"agency",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"time",***REMOVED***"distance",***REMOVED***"year",***REMOVED***"month",***REMOVED***"day",***REMOVED***"day_of_week"]

if***REMOVED***__name__***REMOVED***==***REMOVED***"__main__":
***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***sample_input***REMOVED***=***REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"from":***REMOVED***"DEL",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"to":***REMOVED***"BOM",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"flightType":***REMOVED***"Economy",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"agency":***REMOVED***"AirIndia",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"time":***REMOVED***10.5,***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"year":***REMOVED***2023,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"month":***REMOVED***9,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"day":***REMOVED***12,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"day_of_week":***REMOVED***2***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***}

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Prepare***REMOVED***features***REMOVED***in***REMOVED***correct***REMOVED***order
***REMOVED******REMOVED******REMOVED******REMOVED***X***REMOVED***=***REMOVED***prepare_features(sample_input,***REMOVED***FEATURE_ORDER)

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Predict***REMOVED***price
***REMOVED******REMOVED******REMOVED******REMOVED***price***REMOVED***=***REMOVED***predict_price(model,***REMOVED***X)

***REMOVED******REMOVED******REMOVED******REMOVED***print(f"Predicted***REMOVED***Price***REMOVED***for***REMOVED***{sample_input['from']}***REMOVED***->***REMOVED***{sample_input['to']}:***REMOVED***{round(price,***REMOVED***2)}")