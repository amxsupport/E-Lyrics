import unittest
from unittest.mock import patch
from word_analysis_script import fetch_lyrics, process_lyrics, fetch_word_frequency, find_least_frequent_words

class TestWordAnalysis(unittest.TestCase):
    """Test cases for word analysis script"""

    @patch('requests.get')
    def test_fetch_lyrics(self, mock_requests_get):
        """Test fetch_lyrics function"""
        # Mock response
        lyrics_dict = {'lyrics': 'This is a test lyrics'}
        mock_requests_get.return_value.json.return_value = lyrics_dict
        
        # Call function
        result = fetch_lyrics('Test Artist', 'Test Song')
        
        # Assertions
        self.assertEqual(result, 'This is a test lyrics')
        
