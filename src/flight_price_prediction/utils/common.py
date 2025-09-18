import***REMOVED***os
from***REMOVED***box.exceptions***REMOVED***import***REMOVED***BoxValueError
import***REMOVED***yaml
import***REMOVED***json
import***REMOVED***joblib
from***REMOVED***ensure***REMOVED***import***REMOVED***ensure_annotations
from***REMOVED***box***REMOVED***import***REMOVED***ConfigBox
from***REMOVED***pathlib***REMOVED***import***REMOVED***Path
from***REMOVED***typing***REMOVED***import***REMOVED***Any
import***REMOVED***pandas***REMOVED***as***REMOVED***pd

from***REMOVED***flight_price_prediction***REMOVED***import***REMOVED***logger



@ensure_annotations
def***REMOVED***read_yaml(path_to_yaml:***REMOVED***Path)***REMOVED***->***REMOVED***ConfigBox:
***REMOVED******REMOVED******REMOVED******REMOVED***"""reads***REMOVED***yaml***REMOVED***file***REMOVED***and***REMOVED***returns

***REMOVED******REMOVED******REMOVED******REMOVED***Args:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***path_to_yaml***REMOVED***(str):***REMOVED***path***REMOVED***like***REMOVED***input

***REMOVED******REMOVED******REMOVED******REMOVED***Raises:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***ValueError:***REMOVED***if***REMOVED***yaml***REMOVED***file***REMOVED***is***REMOVED***empty
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***e:***REMOVED***empty***REMOVED***file

***REMOVED******REMOVED******REMOVED******REMOVED***Returns:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***ConfigBox:***REMOVED***ConfigBox***REMOVED***type
***REMOVED******REMOVED******REMOVED******REMOVED***"""
***REMOVED******REMOVED******REMOVED******REMOVED***try:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***with***REMOVED***open(path_to_yaml)***REMOVED***as***REMOVED***yaml_file:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***content***REMOVED***=***REMOVED***yaml.safe_load(yaml_file)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***logger.info(f"yaml***REMOVED***file:***REMOVED***{path_to_yaml}***REMOVED***loaded***REMOVED***successfully")
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***ConfigBox(content)
***REMOVED******REMOVED******REMOVED******REMOVED***except***REMOVED***BoxValueError:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise***REMOVED***ValueError("yaml***REMOVED***file***REMOVED***is***REMOVED***empty")
***REMOVED******REMOVED******REMOVED******REMOVED***except***REMOVED***Exception***REMOVED***as***REMOVED***e:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise***REMOVED***e
***REMOVED******REMOVED******REMOVED******REMOVED***


@ensure_annotations
def***REMOVED***create_directories(path_to_directories:***REMOVED***list,***REMOVED***verbose=True):
***REMOVED******REMOVED******REMOVED******REMOVED***"""create***REMOVED***list***REMOVED***of***REMOVED***directories

***REMOVED******REMOVED******REMOVED******REMOVED***Args:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***path_to_directories***REMOVED***(list):***REMOVED***list***REMOVED***of***REMOVED***path***REMOVED***of***REMOVED***directories
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***ignore_log***REMOVED***(bool,***REMOVED***optional):***REMOVED***ignore***REMOVED***if***REMOVED***multiple***REMOVED***dirs***REMOVED***is***REMOVED***to***REMOVED***be***REMOVED***created.***REMOVED***Defaults***REMOVED***to***REMOVED***False.
***REMOVED******REMOVED******REMOVED******REMOVED***"""
***REMOVED******REMOVED******REMOVED******REMOVED***for***REMOVED***path***REMOVED***in***REMOVED***path_to_directories:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***os.makedirs(path,***REMOVED***exist_ok=True)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if***REMOVED***verbose:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***logger.info(f"created***REMOVED***directory***REMOVED***at:***REMOVED***{path}")


@ensure_annotations
def***REMOVED***save_json(path:***REMOVED***Path,***REMOVED***data:***REMOVED***dict):
***REMOVED******REMOVED******REMOVED******REMOVED***"""save***REMOVED***json***REMOVED***data

***REMOVED******REMOVED******REMOVED******REMOVED***Args:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***path***REMOVED***(Path):***REMOVED***path***REMOVED***to***REMOVED***json***REMOVED***file
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***data***REMOVED***(dict):***REMOVED***data***REMOVED***to***REMOVED***be***REMOVED***saved***REMOVED***in***REMOVED***json***REMOVED***file
***REMOVED******REMOVED******REMOVED******REMOVED***"""
***REMOVED******REMOVED******REMOVED******REMOVED***with***REMOVED***open(path,***REMOVED***"w")***REMOVED***as***REMOVED***f:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***json.dump(data,***REMOVED***f,***REMOVED***indent=4)

***REMOVED******REMOVED******REMOVED******REMOVED***logger.info(f"json***REMOVED***file***REMOVED***saved***REMOVED***at:***REMOVED***{path}")




@ensure_annotations
def***REMOVED***load_json(path:***REMOVED***Path)***REMOVED***->***REMOVED***ConfigBox:
***REMOVED******REMOVED******REMOVED******REMOVED***"""load***REMOVED***json***REMOVED***files***REMOVED***data

***REMOVED******REMOVED******REMOVED******REMOVED***Args:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***path***REMOVED***(Path):***REMOVED***path***REMOVED***to***REMOVED***json***REMOVED***file

***REMOVED******REMOVED******REMOVED******REMOVED***Returns:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***ConfigBox:***REMOVED***data***REMOVED***as***REMOVED***class***REMOVED***attributes***REMOVED***instead***REMOVED***of***REMOVED***dict
***REMOVED******REMOVED******REMOVED******REMOVED***"""
***REMOVED******REMOVED******REMOVED******REMOVED***with***REMOVED***open(path)***REMOVED***as***REMOVED***f:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***content***REMOVED***=***REMOVED***json.load(f)

***REMOVED******REMOVED******REMOVED******REMOVED***logger.info(f"json***REMOVED***file***REMOVED***loaded***REMOVED***succesfully***REMOVED***from:***REMOVED***{path}")
***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***ConfigBox(content)


@ensure_annotations
def***REMOVED***save_bin(data:***REMOVED***Any,***REMOVED***path:***REMOVED***Path):
***REMOVED******REMOVED******REMOVED******REMOVED***"""save***REMOVED***binary***REMOVED***file

***REMOVED******REMOVED******REMOVED******REMOVED***Args:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***data***REMOVED***(Any):***REMOVED***data***REMOVED***to***REMOVED***be***REMOVED***saved***REMOVED***as***REMOVED***binary
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***path***REMOVED***(Path):***REMOVED***path***REMOVED***to***REMOVED***binary***REMOVED***file
***REMOVED******REMOVED******REMOVED******REMOVED***"""
***REMOVED******REMOVED******REMOVED******REMOVED***joblib.dump(value=data,***REMOVED***filename=path)
***REMOVED******REMOVED******REMOVED******REMOVED***logger.info(f"binary***REMOVED***file***REMOVED***saved***REMOVED***at:***REMOVED***{path}")


@ensure_annotations
def***REMOVED***load_bin(path:***REMOVED***Path)***REMOVED***->***REMOVED***Any:
***REMOVED******REMOVED******REMOVED******REMOVED***"""load***REMOVED***binary***REMOVED***data

***REMOVED******REMOVED******REMOVED******REMOVED***Args:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***path***REMOVED***(Path):***REMOVED***path***REMOVED***to***REMOVED***binary***REMOVED***file

***REMOVED******REMOVED******REMOVED******REMOVED***Returns:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***Any:***REMOVED***object***REMOVED***stored***REMOVED***in***REMOVED***the***REMOVED***file
***REMOVED******REMOVED******REMOVED******REMOVED***"""
***REMOVED******REMOVED******REMOVED******REMOVED***data***REMOVED***=***REMOVED***joblib.load(path)
***REMOVED******REMOVED******REMOVED******REMOVED***logger.info(f"binary***REMOVED***file***REMOVED***loaded***REMOVED***from:***REMOVED***{path}")
***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***data

@ensure_annotations
def***REMOVED***get_size(path:***REMOVED***Path)***REMOVED***->***REMOVED***str:
***REMOVED******REMOVED******REMOVED******REMOVED***"""Get***REMOVED***file***REMOVED***size***REMOVED***in***REMOVED***KB***REMOVED***(useful***REMOVED***for***REMOVED***debugging***REMOVED***model***REMOVED***size)"""
***REMOVED******REMOVED******REMOVED******REMOVED***size_in_kb***REMOVED***=***REMOVED***round(os.path.getsize(path)/1024)
***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***f"~***REMOVED***{size_in_kb}***REMOVED***KB"

@ensure_annotations

def***REMOVED***prepare_features(data:dict,***REMOVED***feature_order:list)***REMOVED***->***REMOVED***pd.DataFrame:

***REMOVED******REMOVED******REMOVED******REMOVED***df***REMOVED***=***REMOVED***pd.DataFrame([data])
***REMOVED******REMOVED******REMOVED******REMOVED***df***REMOVED***=***REMOVED***df[feature_order]
***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***df

@ensure_annotations

def***REMOVED***read_data(path:Path)***REMOVED***->***REMOVED***pd.DataFrame:***REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***df***REMOVED***=***REMOVED***pd.read_csv(path)
***REMOVED******REMOVED******REMOVED******REMOVED***logger.info(f"data***REMOVED***read***REMOVED***successfully***REMOVED***from***REMOVED***{path}***REMOVED***and***REMOVED***shape***REMOVED***of***REMOVED***data***REMOVED***is***REMOVED***{df.shape}")
***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***df

@ensure_annotations

def***REMOVED***predict_price(model,***REMOVED***features:***REMOVED***pd.DataFrame)***REMOVED***->***REMOVED***float:
***REMOVED******REMOVED******REMOVED******REMOVED***prediction***REMOVED***=***REMOVED***model.predict(features)[0]
***REMOVED******REMOVED******REMOVED******REMOVED***logger.info(f"Prediction***REMOVED***made:***REMOVED***{prediction}")
***REMOVED******REMOVED******REMOVED******REMOVED***return***REMOVED***prediction
