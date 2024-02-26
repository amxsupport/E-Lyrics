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

