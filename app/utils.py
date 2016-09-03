""" Utility functions used by the application. Involves a lot of loading of
json data.

September 2, 2016
"""

import json

def load_json(filename):
    """ Loads in a json file """
    with open(filename, 'r') as f:
        results = json.load(f)
    return results

def create_error(message):
    """ Returns a dict containing an error message. """
    return {"error" : message}
