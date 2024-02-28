#!/usr/bin/python3
"""This module creates the Unittest for Word class"""
import unittest
from models.word import Word
from models.base_model import BaseModel
from models.song import Song
from models.suggestion import Suggestion
from models.interpretation import Interpretation
from datetime import datetime
from unittest.mock import patch

class TestWord(unittest.TestCase):
    """Test cases for the Word class"""
    
    def setUp(self):
        """Set up test environment"""
        self.word = Word(text="Test Word")

