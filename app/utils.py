import json
import csv

def load_csv(filename):
    """ Loads in a csv file and converts each line to a dictionary. """
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        results = [line for line in reader]
    return results

def load_json(filename):
    pass

def get_assignments_json():
    pass

def get_students_json():
    pass

def get_info_json():
    pass
