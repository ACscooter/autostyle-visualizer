""" This file contains all web-app routes.

Created: August 27, 2016
"""

from flask import render_template, request
from app import app


@app.route('/')
def index():
    pass

@app.route('/assignments/')
def assignments():
    pass

@app.route('/students/')
def students():
    pass

@app.route('/<assignment>/')
def assignment_submitters(assignment):
    pass

@app.route('/<assignment>/<sid>/')
def assignment_by_student(assignment, sid):
    pass

@app.route('/<sid>/student-info/')
def student_info(sid):
    pass

@app.route('/<sid>/submissions/')
def student_submissions(sid):
    pass
