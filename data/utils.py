""" A script filled functions that converts data into different forms.

Antares Chen
September 2, 2016
"""

from datetime import datetime
from collections import defaultdict
import argparse
import json
import csv
import ast


# -------------------------- FILE UTILITIES --------------------------


def load_csv(filename):
    """ Loads in a csv file and converts each line to a dictionary. Groups
    csv lines by the same sid.
    """
    results = defaultdict(list)
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            results[line['sid']].append(line)
    return results

def load_json(filename):
    """ Loads the json at FILENAME. """
    with open(filename, 'r') as f:
        results = json.load(f)
    return results

def export_json(contents, filename):
    """ Exports CONTENTS into a json named FILENAME. """
    with open(filename, 'w') as f:
        json.dump(contents, f)


# -------------------------- JSON CREATORS ---------------------------


def create_assignments_json(csv_contents):
    """ Returns the assignments json. """
    questions = settings['questions']
    results = {}
    for name in questions:
        key_func = lambda x : x['problem_name'] == name
        results[name] = {}
        for sid in csv_contents:
            elems = filter(key_func, csv_contents[sid])
            results[name][sid] = get_submissions(elems)
    return results

def create_students_json(csv_contents):
    """ Returns the students json. """
    questions = settings['questions']
    results = {}
    for sid in csv_contents:
        key_func = lambda x : x['problem_name'] == name
        results[sid] = {}
        for name in questions:
            elems = filter(key_func, csv_contents[sid])
            results[sid][name] = get_submissions(elems)
    return results

def create_info_json(csv_contents):
    """ Returns the info json. Assumes that experiment groups and consent for
    each student remains consistent for all entries in the csv.
    """
    students, assignments = {}, {}
    questions = settings['questions']

    # For loop to process the students information dictionary
    for sid in csv_contents:
        elems = csv_contents[sid]
        students[sid] = {
            'consent' : elems[0]['consent'],
            'experiment group' : elems[0]['exp_group']
        }

    # For loop to process the assignments dictionary
    for name in questions:
        assignments[name] = {}

    return {'students' : students, 'assignments' : assignments}


# ------------------------- JSON UTILITIES ---------------------------


def get_submissions(submissions):
    """ Returns SUBMISSIONS, a collection of csv lines, to json form. """
    results = []
    for entry in submissions:
        results.append({
            'timestamp' : entry['timestamp'],
            'code' : entry['raw_text'],
            'style_score' : entry['style_score'],
            'cluster' : entry['cluster'],
            'correct' : get_correct(entry),
            'hints' : get_hints(entry)
        })
    sorted(results, key=lambda x : x['timestamp'])
    for entry in results:
        entry['timestamp'] = convert_timestamp(entry['timestamp'])
    return results

def get_correct(entry):
    """ Returns whether or not ENTRY is correct. """
    return entry['correct'] == "1"

def get_hints(entry):
    """ Returns the hints from ENTRY. """
    hints = {}
    if entry['approach_hints'] and entry['approach_hints'] != "[]":
        hints['approach'] = ast.literal_eval(str(entry['approach_hints']))
    if entry['syntactic_hints'] and entry['syntactic_hints'] != "[]":
        hints['syntactic'] = ast.literal_eval(str(entry['syntactic_hints']))
    if entry['skeleton_hints']:
        hints['skeleton'] = entry['skeleton_hints']
    return hints

def convert_timestamp(stamp):
    """ Converts STAMP from unix time to human-readable format. """
    date = datetime.fromtimestamp(float(stamp))
    return date.strftime("%m/%d/%y %I:%M:%S %p")


# ------------------------- ARGPARSE THINGS ---------------------------

settings = load_json("settings.json")
parser = argparse.ArgumentParser(description='A small script to convert the csv to a json file')
parser.add_argument("path",
                    help="The path to the experiment's csv dump.",
                    type=str)
parser.add_argument("--all",
                    help="Exports all jsons from the csv file.",
                    action="store_true")
parser.add_argument("--questions",
                    help="Exports the assignments json from the csv file.",
                    action="store_true")
parser.add_argument("--students",
                    help="Exports the students json from the csv file.",
                    action="store_true")
parser.add_argument("--info",
                    help="Exports the info json from the csv file.",
                    action="store_true")
args = parser.parse_args()
csv_file = load_csv(args.path)
if args.all is None and args.questions is None and args.students is None and args.info is None:
    args.all = True
if args.all or args.questions:
    print(">> Creating questions.json")
    assignments = create_assignments_json(csv_file)
    export_json(assignments, "assignments.json")
if args.all or args.students:
    print(">> Creating students.json")
    students = create_students_json(csv_file)
    export_json(students, "students.json")
if args.all or args.info:
    print(">> Creating info.json")
    info = create_info_json(csv_file)
    export_json(info, "info.json")
print(">> Done")
