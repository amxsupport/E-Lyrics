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

@app_views.route('/interpretations/<word_id>/<song_id>', methods=['GET'],
                 strict_slashes=False)
def get_interpretations(word_id=None, song_id=None):
    """Retrieves all Interpretation objects for a word from a song and returns
    a list containing all of them"""
    word = storage.get('Word', word_id)
    if word is None:
        abort(404)
    song = storage.get('Song', song_id)
    if song is None:
        abort(404)
    interpretations_dict = storage.all(Interpretation)
    interpretations_list = []
    for interpretation in interpretations_dict.values():
        if interpretation.word_id == word_id and interpretation.song_id == song_id:
            interpretations_list.append(interpretation.to_dict())
    return jsonify(interpretations_list), 200


