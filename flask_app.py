from***REMOVED***flask***REMOVED***import***REMOVED***Flask,***REMOVED***request,***REMOVED***jsonify,***REMOVED***render_template
import***REMOVED***pandas***REMOVED***as***REMOVED***pd
import***REMOVED***joblib
import***REMOVED***os
from***REMOVED***flask_cors***REMOVED***import***REMOVED***CORS,***REMOVED***cross_origin
from***REMOVED***datetime***REMOVED***import***REMOVED***datetime

app***REMOVED***=***REMOVED***Flask(__name__)
CORS(app)

#***REMOVED***get***REMOVED***model***REMOVED***path***REMOVED***
MODEL_PATH***REMOVED***=***REMOVED***"models/RandomForest_flight_model.pkl"

#***REMOVED***Load***REMOVED***model
model***REMOVED***=***REMOVED***joblib.load(MODEL_PATH)

REQUIRED_FIELDS***REMOVED***=***REMOVED***["from",***REMOVED***"to",***REMOVED***"flightType",***REMOVED***"agency",***REMOVED***"time",***REMOVED***"distance",***REMOVED***"year",***REMOVED***"month",***REMOVED***"day",***REMOVED***"day_of_week"]

def***REMOVED***parse_and_engineer(payload:***REMOVED***dict)***REMOVED***->***REMOVED***pd.DataFrame:

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Basic***REMOVED***validation
***REMOVED******REMOVED******REMOVED******REMOVED***missing***REMOVED***=***REMOVED***[f***REMOVED***for***REMOVED***f***REMOVED***in***REMOVED***REQUIRED_FIELDS***REMOVED***if***REMOVED***f***REMOVED***not***REMOVED***in***REMOVED***payload]
***REMOVED******REMOVED******REMOVED******REMOVED***if***REMOVED***missing:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise***REMOVED***ValueError(f"Missing***REMOVED***fields:***REMOVED***{missing}")

***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Parse/convert
***REMOVED******REMOVED******REMOVED******REMOVED***def***REMOVED***parse_numeric(value):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if***REMOVED***isinstance(value,***REMOVED***(int,***REMOVED***float)):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***float(value)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***value***REMOVED***=***REMOVED***str(value).strip()
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if***REMOVED***":"***REMOVED***in***REMOVED***value:***REMOVED******REMOVED***#***REMOVED***handle***REMOVED***HH:MM
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***h,***REMOVED***m***REMOVED***=***REMOVED***map(int,***REMOVED***value.split(":"))
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***h***REMOVED***+***REMOVED***m***REMOVED***/***REMOVED***60.0
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***float(value)

***REMOVED******REMOVED******REMOVED******REMOVED***try:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***time_val***REMOVED***=***REMOVED***parse_numeric(payload["time"])
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***dist_val***REMOVED***=***REMOVED***parse_numeric(payload["distance"])
***REMOVED******REMOVED******REMOVED******REMOVED***except***REMOVED***Exception:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise***REMOVED***ValueError("`time`***REMOVED***and***REMOVED***`distance`***REMOVED***must***REMOVED***be***REMOVED***int,***REMOVED***float,***REMOVED***numeric***REMOVED***string,***REMOVED***or***REMOVED***HH:MM***REMOVED***format.")


***REMOVED******REMOVED******REMOVED******REMOVED***row***REMOVED***=***REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"from":***REMOVED***payload["from"],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"to":***REMOVED***payload["to"],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"flightType":***REMOVED***payload["flightType"],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"agency":***REMOVED***payload["agency"],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"time":***REMOVED***time_val,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"distance":***REMOVED***dist_val,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"year":***REMOVED***int(payload["year"]),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"month":***REMOVED***int(payload["month"]),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"day":***REMOVED***int(payload["day"]),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"day_of_week":***REMOVED***int(payload["day_of_week"]),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***pd.DataFrame([row])


#***REMOVED***routes***REMOVED***


@app.route("/",***REMOVED***methods=["GET"])
def***REMOVED***home():
***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***render_template("index.html")


@app.route("/health",***REMOVED***methods=["GET"])
def***REMOVED***health():
***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***jsonify({"status":***REMOVED***"ok",***REMOVED***"model_loaded":***REMOVED***MODEL_PATH})



@app.route("/predict",***REMOVED***methods=["GET",***REMOVED***"POST"])
def***REMOVED***predict():
***REMOVED******REMOVED******REMOVED******REMOVED***try:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if***REMOVED***request.method***REMOVED***==***REMOVED***"POST":
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Expect***REMOVED***JSON***REMOVED***body
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***payload***REMOVED***=***REMOVED***request.get_json(force=True)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***else:***REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Expect***REMOVED***query***REMOVED***parameters
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***from_***REMOVED***=***REMOVED***request.args.get("from")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***to***REMOVED***=***REMOVED***request.args.get("to")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***distance***REMOVED***=***REMOVED***request.args.get("distance")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***flightType***REMOVED***=***REMOVED***request.args.get("flightType")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***agency***REMOVED***=***REMOVED***request.args.get("agency")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***time***REMOVED***=***REMOVED***request.args.get("time")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***year***REMOVED***=***REMOVED***request.args.get("year")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***month***REMOVED***=***REMOVED***request.args.get("month")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***day***REMOVED***=***REMOVED***request.args.get("day")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***day_of_week***REMOVED***=***REMOVED***request.args.get("day_of_week")

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if***REMOVED***not***REMOVED***all([from_,***REMOVED***to,***REMOVED***distance,***REMOVED***flightType,***REMOVED***agency,***REMOVED***time,***REMOVED***year,***REMOVED***month,***REMOVED***day,***REMOVED***day_of_week]):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***jsonify({"error":***REMOVED***"Missing***REMOVED***one***REMOVED***or***REMOVED***more***REMOVED***required***REMOVED***query***REMOVED***parameters."}),***REMOVED***400

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***payload***REMOVED***=***REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"from":***REMOVED***from_,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"to":***REMOVED***to,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"flightType":***REMOVED***flightType,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"agency":***REMOVED***agency,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"time":***REMOVED***time,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"distance":***REMOVED***distance,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"year":***REMOVED***year,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"month":***REMOVED***month,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"day":***REMOVED***day,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"day_of_week":***REMOVED***day_of_week
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***}

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED***Process***REMOVED***input
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***X***REMOVED***=***REMOVED***parse_and_engineer(payload)

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***feature_order***REMOVED***=***REMOVED***REQUIRED_FIELDS
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***X***REMOVED***=***REMOVED***X[feature_order]


***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***pred***REMOVED***=***REMOVED***float(model.predict(X)[0])

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***jsonify({"predicted_price":***REMOVED***round(pred,***REMOVED***2)})

***REMOVED******REMOVED******REMOVED******REMOVED***except***REMOVED***Exception***REMOVED***as***REMOVED***e:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***jsonify({"error":***REMOVED***str(e)}),***REMOVED***400


@app.route("/predict-batch",***REMOVED***methods=["POST"])
def***REMOVED***predict_batch():
***REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***try:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***data***REMOVED***=***REMOVED***request.get_json(force=True)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***records***REMOVED***=***REMOVED***data.get("records",***REMOVED***[])
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if***REMOVED***not***REMOVED***isinstance(records,***REMOVED***list)***REMOVED***or***REMOVED***len(records)***REMOVED***==***REMOVED***0:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***jsonify({"error":***REMOVED***"`records`***REMOVED***must***REMOVED***be***REMOVED***a***REMOVED***non-empty***REMOVED***list"}),***REMOVED***400

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***frames***REMOVED***=***REMOVED***[parse_and_engineer(r)***REMOVED***for***REMOVED***r***REMOVED***in***REMOVED***records]
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***X***REMOVED***=***REMOVED***pd.concat(frames,***REMOVED***ignore_index=True)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***preds***REMOVED***=***REMOVED***model.predict(X).tolist()
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***preds***REMOVED***=***REMOVED***[round(float(p),***REMOVED***2)***REMOVED***for***REMOVED***p***REMOVED***in***REMOVED***preds]
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***jsonify({"predicted_prices":***REMOVED***preds})
***REMOVED******REMOVED******REMOVED******REMOVED***except***REMOVED***Exception***REMOVED***as***REMOVED***e:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***jsonify({"error":***REMOVED***str(e)}),***REMOVED***400


if***REMOVED***__name__***REMOVED***==***REMOVED***"__main__":
***REMOVED******REMOVED******REMOVED******REMOVED***app.run(host="0.0.0.0",***REMOVED***port=5000,***REMOVED***debug=True)
