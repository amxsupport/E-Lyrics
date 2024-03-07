#!/usr/bin/python3
"""defines view functions to handle requests for song_word data"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.song import Song
app = Flask(__name__)


