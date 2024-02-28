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

