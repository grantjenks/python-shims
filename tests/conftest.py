import datetime
import importlib
import sys

# Force CPython to use the pure-Python implementation of the datetime module
# for testing. https://stackoverflow.com/a/62506055/232571
sys.modules["_datetime"] = None
importlib.reload(datetime)
