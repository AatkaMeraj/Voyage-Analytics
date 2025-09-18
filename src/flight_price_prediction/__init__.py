import***REMOVED***os
import***REMOVED***sys
import***REMOVED***logging

logging_str***REMOVED***=***REMOVED***"[%(asctime)s***REMOVED***:***REMOVED***%(levelname)s***REMOVED***:***REMOVED***%(module)s***REMOVED***:***REMOVED***%(message)s]"

log_dir***REMOVED***=***REMOVED***"logs"
log_filepath***REMOVED***=***REMOVED***os.path.join(log_dir,***REMOVED***"running_logs.log")
os.makedirs(log_dir,***REMOVED***exist_ok=True)

logging.basicConfig(
***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***level=logging.INFO,
***REMOVED******REMOVED******REMOVED******REMOVED***format=logging_str,
***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***handlers=[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***logging.FileHandler(log_filepath),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***logging.StreamHandler(sys.stdout)***REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***]
)

logger***REMOVED***=***REMOVED***logging.getLogger("flight_price_prediction")