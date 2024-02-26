#!/usr/bin/python3
"""Defines unnittests for models/song.py."""

import unittest
from models.song import Song
from datetime import datetime
from unittest.mock import patch

class TestSong(unittest.TestCase):
    """Test cases for the Song class"""
    
    def setUp(self):
        """Set up test environment"""
        self.song = Song(artist="Test Artist",
                         title="Test Title",
                         lyrics="Test Lyrics",
                         genre="Test Genre",
                         image_url="https://example.com/test.jpg")

