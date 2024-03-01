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

    def test_all_method(self):
        """Test all method"""
        # Test without specifying class
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertTrue(all_objects)
        
        # Test with specifying class
        all_songs = self.storage.all(Song)
        self.assertIsInstance(all_songs, dict)
        self.assertTrue(all_songs)
        
        all_words = self.storage.all(Word)
        self.assertIsInstance(all_words, dict)
        self.assertTrue(all_words)
        
        all_interpretations = self.storage.all(Interpretation)
        self.assertIsInstance(all_interpretations, dict)
        self.assertTrue(all_interpretations)
        
        all_suggestions = self.storage.all(Suggestion)
        self.assertIsInstance(all_suggestions, dict)
        self.assertTrue(all_suggestions)

