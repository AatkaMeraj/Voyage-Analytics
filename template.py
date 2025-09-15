import***REMOVED***os
from***REMOVED***pathlib***REMOVED***import***REMOVED***Path
import***REMOVED***logging

logging.basicConfig(level=logging.INFO,***REMOVED***format='[%(asctime)s]:***REMOVED***%(message)s')

project_name=***REMOVED***"flight_price_prediction"

list_of_files=***REMOVED***[
***REMOVED******REMOVED******REMOVED******REMOVED***f"src/{project_name}/__init__.py",
***REMOVED******REMOVED******REMOVED******REMOVED***f"src/{project_name}/components/__init__.py",
***REMOVED******REMOVED******REMOVED******REMOVED***f"src/{project_name}/utils/__init__.py",
***REMOVED******REMOVED******REMOVED******REMOVED***f"src/{project_name}/config/__init__.py",
***REMOVED******REMOVED******REMOVED******REMOVED***f"src/{project_name}/config/configuration.py",
***REMOVED******REMOVED******REMOVED******REMOVED***f"src/{project_name}/pipeline/__init__.py",
***REMOVED******REMOVED******REMOVED******REMOVED***f"src/{project_name}/entity/__init__.py",***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***f"src/{project_name}/constants/__init__.py",

***REMOVED******REMOVED******REMOVED******REMOVED***"config/config.yaml",
***REMOVED******REMOVED******REMOVED******REMOVED***"dvc.yaml",
***REMOVED******REMOVED******REMOVED******REMOVED***"params.yaml",
***REMOVED******REMOVED******REMOVED******REMOVED***"requirements.txt",
***REMOVED******REMOVED******REMOVED******REMOVED***"setup.py",
***REMOVED******REMOVED******REMOVED******REMOVED***"research/trials.ipynb",
***REMOVED******REMOVED******REMOVED******REMOVED***"README.md",
***REMOVED******REMOVED******REMOVED******REMOVED***"requirements.txt",
***REMOVED******REMOVED******REMOVED******REMOVED***"templates/index.html"
]

for***REMOVED***filepath***REMOVED***in***REMOVED***list_of_files:
***REMOVED******REMOVED******REMOVED******REMOVED***filepath=***REMOVED***Path(filepath)
***REMOVED******REMOVED******REMOVED******REMOVED***filedir,***REMOVED***filename=***REMOVED***os.path.split(filepath)

***REMOVED******REMOVED******REMOVED******REMOVED***if***REMOVED***filedir***REMOVED***!=***REMOVED***"":
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***os.makedirs(filedir,***REMOVED***exist_ok=***REMOVED***True)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***logging.info(f"Creating***REMOVED***directory:***REMOVED***{filedir}***REMOVED***for***REMOVED***file:***REMOVED***{filename}")

***REMOVED******REMOVED******REMOVED******REMOVED***if***REMOVED***(not***REMOVED***os.path.exists(filepath))***REMOVED***or***REMOVED***(os.path.getsize(filepath)***REMOVED***==***REMOVED***0):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***with***REMOVED***open(filepath,***REMOVED***"w")***REMOVED***as***REMOVED***fp:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***pass
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***logging.info(f"Creating***REMOVED***file:***REMOVED***{filepath}")
***REMOVED******REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***logging.info(f"File{filename}already***REMOVED***exists")