""" This file contains all web-app routes.

Created: September 2, 2016
"""

from flask import render_template, request
from app import app


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/assignments/')
def assignments():
    """ Returns a list of all assignments. """
    pass

@app.route('/students/')
def students():
    """ Returns a list of all students who participated in the experiment. """
    pass

@app.route('/<assignment>/')
def assignment_submitters(assignment):
    """ Returns a list of sids who submitted to ASSIGNMENT. """
    pass

@app.route('/<assignment>/<sid>/')
def assignment_by_student(assignment, sid):
    """ Returns a list of submissisions from SID to ASSIGNMENT. """
    pass

@app.route('/<sid>/student-info/')
def student_info(sid):
    """ Returns the information associated with SID. """
    pass

@app.route('/<sid>/submissions/')
def student_submissions(sid):
    """ Returns all submissions to all assignments from SID. """
    pass
