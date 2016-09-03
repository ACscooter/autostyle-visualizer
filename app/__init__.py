from flask import Flask

app = Flask(__name__)

from app import visualizer

settings = utils.load_json("data/settings.json")
