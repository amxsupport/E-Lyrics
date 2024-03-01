#!/usr/bin/python3
"""Defines unnittests for models/engine/storage.py"""
import pep8
import models
import MySQLdb
import unittest
from models.engine.storage import Storage
from models.song import Song
from models.word import Word
from models.interpretation import Interpretation
from models.suggestion import Suggestion
from models.base_model import BaseModel
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine

class TestStorage(unittest.TestCase):
    """Test cases for the Storage class"""
    
    def setUp(self):
        """Set up test environment"""
        self.storage = Storage()
        self.storage.reload()

