""" This file contains all web-app routes.

Created: September 2, 2016
"""

from flask import render_template, request, jsonify
from app.constants import settings, assignments, students, info
from app.utils import create_error
from app import app


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/assignments/')
def questions():
    """ Returns a list of all assignments. """
    results = {'names' : settings['question_names']}
    return jsonify(results)

@app.route('/sids/')
def sids():
    """ Returns a list of all students who participated in the experiment. """
    return jsonify({'names' : list(students.keys())})

@app.route('/<question>/')
def question_submitters(question):
    """ Returns a list of sids who submitted to QUESTION. """
    if question not in assignments:
        err = create_error("Assignment {0} not found!".format(question))
        return jsonify(err)
    return jsonify({'submitters' : list(assignments[question])})

@app.route('/<question>/<sid>/')
def question_by_student(question, sid):
    """ Returns a list of submissisions from SID to QUESTION. """
    if question not in assignments:
        err = create_error("Assignment {0} not found!".format(question))
        return jsonify(err)
    submissions = assignments[question]
    if sid not in submissions:
        err = create_error("Student {0} not found for assignment {1}!".format(sid, question))
        return jsonify(err)
    return jsonify({'submissions' : submissions[sid]})

@app.route('/<sid>/student-info/')
def student_info(sid):
    """ Returns the information associated with SID. """
    if sid not in info['students']:
        err = create_error("No info found for student {0}!".format(sid))
        return jsonify(err)
    return jsonify(info['students'][sid])

@app.route('/<sid>/submissions/')
def student_submissions(sid):
    """ Returns all submissions to all assignments from SID. """
    if sid not in students:
        err = create_error("No submissions found for student {0}!".format(sid))
        return jsonify(err)
    return jsonify(students[sid])
