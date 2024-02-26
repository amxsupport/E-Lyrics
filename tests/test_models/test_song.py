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

    def test_attributes(self):
        """Test Song attributes"""
        self.assertTrue(hasattr(self.song, 'id'))
        self.assertTrue(hasattr(self.song, 'created_at'))
        self.assertTrue(hasattr(self.song, 'updated_at'))
        self.assertTrue(hasattr(self.song, 'artist'))
        self.assertTrue(hasattr(self.song, 'title'))
        self.assertTrue(hasattr(self.song, 'lyrics'))
        self.assertTrue(hasattr(self.song, 'genre'))
        self.assertTrue(hasattr(self.song, 'words'))
        self.assertTrue(hasattr(self.song, 'interpretations'))
        self.assertTrue(hasattr(self.song, 'image_url'))

    def test_artist_attribute(self):
        """Test artist attribute"""
        self.assertEqual(self.song.artist, "Test Artist")
        
    def test_title_attribute(self):
        """Test title attribute"""
        self.assertEqual(self.song.title, "Test Title")

    def test_lyrics_attribute(self):
        """Test lyrics attribute"""
        self.assertEqual(self.song.lyrics, "Test Lyrics")
        
    def test_genre_attribute(self):
        """Test genre attribute"""
        self.assertEqual(self.song.genre, "Test Genre")

