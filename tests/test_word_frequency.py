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
        
    def test_process_lyrics(self):
        """Test process_lyrics function"""
        # Input
        lyrics = 'This is a test lyrics with some punctuation! And newlines.\n'
        
        # Call function
        result = process_lyrics(lyrics)
        
        # Assertions
        expected_result = ['This', 'is', 'a', 'test', 'lyrics', 'with', 'some', 'punctuation', 'And', 'newlines']
        self.assertEqual(result, expected_result)

    @patch('requests.get')
    def test_fetch_word_frequency(self, mock_requests_get):
        """Test fetch_word_frequency function"""
        # Mock response
        word_dict = {'frequency': 10}
        mock_requests_get.return_value.json.return_value = word_dict
        
        # Call function
        result = fetch_word_frequency('test')
        
        # Assertions
        self.assertEqual(result, 10)

    def test_find_least_frequent_words(self):
        """Test find_least_frequent_words function"""
        # Input
        word_frequency = {'word1': 10, 'word2': 5, 'word3': 20, 'word4': 3}
        
        # Call function
        result = find_least_frequent_words(word_frequency, 2)
        
        # Assertions
        expected_result = [('word4', 3), ('word2', 5)]
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()
