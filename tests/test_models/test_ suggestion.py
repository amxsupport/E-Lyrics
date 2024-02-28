#!/usr/bin/python3
"""Defines unnittests for models/suggestion.py."""
import unittest
from models.suggestion import Suggestion
from datetime import datetime
from unittest.mock import patch

class TestSuggestion(unittest.TestCase):
    """Test cases for the Suggestion class"""
    
    def setUp(self):
        """Set up test environment"""
        self.suggestion = Suggestion(suggested_artist="Test Artist",
                                     suggested_song="Test Song",
                                     suggested_words="Test Words",
                                     name="Test User",
                                     email="test@example.com")

    def test_attributes(self):
        """Test Suggestion attributes"""
        self.assertTrue(hasattr(self.suggestion, 'id'))
        self.assertTrue(hasattr(self.suggestion, 'created_at'))
        self.assertTrue(hasattr(self.suggestion, 'updated_at'))
        self.assertTrue(hasattr(self.suggestion, 'suggested_artist'))
        self.assertTrue(hasattr(self.suggestion, 'suggested_song'))
        self.assertTrue(hasattr(self.suggestion, 'suggested_words'))
        self.assertTrue(hasattr(self.suggestion, 'name'))
        self.assertTrue(hasattr(self.suggestion, 'email'))

    def test_suggested_artist_attribute(self):
        """Test suggested_artist attribute"""
        self.assertEqual(self.suggestion.suggested_artist, "Test Artist")
        
    def test_suggested_song_attribute(self):
        """Test suggested_song attribute"""
        self.assertEqual(self.suggestion.suggested_song, "Test Song")
        
    def test_suggested_words_attribute(self):
        """Test suggested_words attribute"""
        self.assertEqual(self.suggestion.suggested_words, "Test Words")

    def test_name_attribute(self):
        """Test name attribute"""
        self.assertEqual(self.suggestion.name, "Test User")
        
    def test_email_attribute(self):
        """Test email attribute"""
        self.assertEqual(self.suggestion.email, "test@example.com")
        
if __name__ == '__main__':
    unittest.main()
