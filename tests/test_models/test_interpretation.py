#!/usr/bin/python3
"""Defines unnittests for models/interpretation.py."""

import unittest
from models.interpretation import Interpretation
from datetime import datetime
from unittest.mock import patch

class TestInterpretation(unittest.TestCase):
    """Test cases for the Interpretation class"""
    
    def setUp(self):
        """Set up test environment"""
        self.interpretation = Interpretation(text="Test interpretation",
                                             song_id="test_song_id",
                                             word_id="test_word_id")

    def test_attributes(self):
        """Test Interpretation attributes"""
        self.assertTrue(hasattr(self.interpretation, 'id'))
        self.assertTrue(hasattr(self.interpretation, 'created_at'))
        self.assertTrue(hasattr(self.interpretation, 'updated_at'))
        self.assertTrue(hasattr(self.interpretation, 'text'))
        self.assertTrue(hasattr(self.interpretation, 'song_id'))
        self.assertTrue(hasattr(self.interpretation, 'word_id'))
        self.assertTrue(hasattr(self.interpretation, 'likes'))

