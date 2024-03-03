"""This module starts the Lyrics_For_Learning Flask web application and defines endpoints
"""
from flask import Flask
from flask import render_template
from models import storage
from models import BaseModel
from models import Song

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def display_homepage():
    """handles request for homepage"""
    return render_template('homepage.html')

@app.route('/songs/<text>', strict_slashes=False)
def display_song(text):
    """handles request for specific song based on title"""
    songs_dict = storage.all(Song)
    result = songs_dict.get("Song.{:}".format(text))
    if result is not None:
            return render_template('song.html', song=result)
    return "NOT FOUND"
