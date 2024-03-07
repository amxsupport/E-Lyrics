#!/usr/bin/python3
"""defines view functions to handle requests for songs data"""


from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
import requests
import os
app = Flask(__name__)


