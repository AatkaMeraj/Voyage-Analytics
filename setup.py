import***REMOVED***setuptools

with***REMOVED***open("README.md",***REMOVED***"r",***REMOVED***encoding="utf-8")***REMOVED***as***REMOVED***f:
***REMOVED******REMOVED******REMOVED******REMOVED***long_description***REMOVED***=***REMOVED***f.read()


__version__***REMOVED***=***REMOVED***"0.0.0"

REPO_NAME***REMOVED***=***REMOVED***"Voyage-Analytics"
AUTHOR_USER_NAME***REMOVED***=***REMOVED***"AatkaMeraj"
AUTHOR_EMAIL***REMOVED***=***REMOVED***"aatkameraj1425@gmail.com"


setuptools.setup(***REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED***name***REMOVED***=***REMOVED***REPO_NAME,
***REMOVED******REMOVED******REMOVED******REMOVED***version***REMOVED***=***REMOVED***__version__,
***REMOVED******REMOVED******REMOVED******REMOVED***author***REMOVED***=***REMOVED***AUTHOR_USER_NAME,
***REMOVED******REMOVED******REMOVED******REMOVED***author_email***REMOVED***=***REMOVED***AUTHOR_EMAIL,
***REMOVED******REMOVED******REMOVED******REMOVED***description***REMOVED***=***REMOVED***"Python***REMOVED***package***REMOVED***for***REMOVED***Flight***REMOVED***Prediction***REMOVED***App",
***REMOVED******REMOVED******REMOVED******REMOVED***long_description***REMOVED***=***REMOVED***long_description,
***REMOVED******REMOVED******REMOVED******REMOVED***long_description_content_type***REMOVED***=***REMOVED***"text/markdown",
***REMOVED******REMOVED******REMOVED******REMOVED***url***REMOVED***=***REMOVED***f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
***REMOVED******REMOVED******REMOVED******REMOVED***project_urls***REMOVED***=***REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Bug***REMOVED***Tracker":***REMOVED***f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

***REMOVED******REMOVED******REMOVED******REMOVED***},
***REMOVED******REMOVED******REMOVED******REMOVED***package_dir***REMOVED***=***REMOVED***{"":***REMOVED***"src"},
***REMOVED******REMOVED******REMOVED******REMOVED***packages***REMOVED***=***REMOVED***setuptools.find_packages(where="src"),
***REMOVED******REMOVED******REMOVED******REMOVED***install_requires***REMOVED***=***REMOVED***[],

)

