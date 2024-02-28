#!/usr/bin/python3
"""This module defines the Storage class"""
from models.base_model import BaseModel, Base
from models.song import Song
from models.word import Word
from models.interpretation import Interpretation
from models.suggestion import Suggestion
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os

classes = {"Song": Song, "Word": Word, "Interpretation": Interpretation,
           "Suggestion": Suggestion}


