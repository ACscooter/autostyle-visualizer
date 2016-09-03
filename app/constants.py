""" A file full of constants.

September 2, 2016
"""

from app import utils

settings = utils.load_json("data/settings.json")


# ---------------------------- CONSTANTS ----------------------------


assignments = utils.load_json(settings['assignments_path'])
students = utils.load_json(settings['students_path'])
info = utils.load_json(settings['info_path'])
