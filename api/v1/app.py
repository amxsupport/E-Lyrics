"""starts the Lyrics for Learning API Flask app"""

import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask import Blueprint
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": 'http://0.0.0.0:5000'}})


@app.errorhandler(404)
def page_not_found(e):
    """Error handling, 404"""
    return jsonify({"error": "Not found"}), 404



