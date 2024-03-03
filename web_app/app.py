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
