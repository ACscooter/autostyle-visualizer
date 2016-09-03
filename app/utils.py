""" Utility functions used by the application. Involves a lot of loading of
json data.

September 2, 2016
"""

import json

def load_json(filename):
    """ Loads in a json file """
    with open(filename, 'r') as f:
        results = json.read(f)
    return results

def get_assignments_json():


def get_students_json():
    pass

def get_info_json():
    pass
