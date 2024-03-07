#!/usr/bin/python3
"""defines view functions to handle requests for interpretations data"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.suggestion import Suggestion
app = Flask(__name__)


@app_views.route('/suggestions/', methods=['GET'], strict_slashes=False)
def get_suggestions(word_id=None, song_id=None):
    """Retrieves all Suggestion objects from database and returns a list containing
    all of them"""
    suggestions_dict = storage.all(Suggestion)
    suggestions_list = []
    for suggestion in suggestions_dict.values():
            suggestions_list.append(suggestion.to_dict())
    return jsonify(suggestions_list), 200


