#!/usr/bin/python3
"""defines view functions to handle requests for interpretations data"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.song import Song
from models.word import Word
from models.interpretation import Interpretation
from better_profanity import profanity
app = Flask(__name__)


