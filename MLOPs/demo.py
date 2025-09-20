import***REMOVED***os
import***REMOVED***warnings
import***REMOVED***sys

import***REMOVED***pandas***REMOVED***as***REMOVED***pd
import***REMOVED***numpy***REMOVED***as***REMOVED***np
from***REMOVED***sklearn.metrics***REMOVED***import***REMOVED***mean_squared_error,***REMOVED***r2_score
from***REMOVED***sklearn.model_selection***REMOVED***import***REMOVED***train_test_split
from***REMOVED***sklearn.linear_model***REMOVED***import***REMOVED***ElasticNet
from***REMOVED***urllib.parse***REMOVED***import***REMOVED***urlparse
import***REMOVED***mlflow
from***REMOVED***mlflow.models.signature***REMOVED***import***REMOVED***infer_signature
import***REMOVED***mlflow.sklearn
import***REMOVED***dagshub
import***REMOVED***logging

logging.basicConfig(level=logging.WARN)
logger***REMOVED***=***REMOVED***logging.getLogger(__name__)***REMOVED******REMOVED******REMOVED******REMOVED***

def***REMOVED***eval_metrics(actual,***REMOVED***pred):
***REMOVED******REMOVED******REMOVED******REMOVED***rmse***REMOVED***=***REMOVED***np.sqrt(mean_squared_error(actual,***REMOVED***pred))
***REMOVED******REMOVED******REMOVED******REMOVED***mae***REMOVED***=***REMOVED***mean_absolute_error(actual,***REMOVED***pred)
***REMOVED******REMOVED******REMOVED******REMOVED***r2***REMOVED***=***REMOVED***r2_score(actual,***REMOVED***pred)
***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***rmse,mae,***REMOVED***r2