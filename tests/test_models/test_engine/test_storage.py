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

    def test_new_method(self):
        """Test new method"""
        # Test adding a new song
        new_song = Song(artist="Test Artist", title="Test Title",
                        lyrics="Test Lyrics", genre="Test Genre",
                        image_url="https://example.com/test.jpg")
        self.storage.new(new_song)
        all_songs = self.storage.all(Song)
        self.assertIn(new_song.id, all_songs)

    def test_save_method(self):
        """Test save method"""
        # Test saving changes
        new_song = Song(artist="Test Artist", title="Test Title",
                        lyrics="Test Lyrics", genre="Test Genre",
                        image_url="https://example.com/test.jpg")
        self.storage.new(new_song)
        self.storage.save()
        all_songs = self.storage.all(Song)
        self.assertIn(new_song.id, all_songs)

    def test_delete_method(self):
        """Test delete method"""
        # Test deleting a song
        new_song = Song(artist="Test Artist", title="Test Title",
                        lyrics="Test Lyrics", genre="Test Genre",
                        image_url="https://example.com/test.jpg")
        self.storage.new(new_song)
        self.storage.save()
        self.storage.delete(new_song)
        all_songs = self.storage.all(Song)
        self.assertNotIn(new_song.id, all_songs)

    def test_reload_method(self):
        """Test reload method"""
        # Test reloading session
        initial_session = self.storage._Storage__session
        self.storage.reload()
        new_session = self.storage._Storage__session
        self.assertIsNot(initial_session, new_session)

