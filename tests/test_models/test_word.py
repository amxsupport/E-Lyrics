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

    def test_attributes(self):
        """Test Word attributes"""
        self.assertTrue(hasattr(self.word, 'id'))
        self.assertTrue(hasattr(self.word, 'created_at'))
        self.assertTrue(hasattr(self.word, 'updated_at'))
        self.assertTrue(hasattr(self.word, 'text'))
        self.assertTrue(hasattr(self.word, 'songs'))
        self.assertTrue(hasattr(self.word, 'interpretations'))

    def test_text_attribute(self):
        """Test text attribute"""
        self.assertEqual(self.word.text, "Test Word")
        
    def test_relationships(self):
        """Test relationships"""
        self.assertEqual(self.word.songs, [])
        self.assertEqual(self.word.interpretations, [])
        
if __name__ == '__main__':
    unittest.main()
