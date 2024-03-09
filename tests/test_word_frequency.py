import unittest
from unittest.mock import patch
from word_analysis_script import fetch_lyrics, process_lyrics, fetch_word_frequency, find_least_frequent_words

class TestWordAnalysis(unittest.TestCase):
    """Test cases for word analysis script"""
