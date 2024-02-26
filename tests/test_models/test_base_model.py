import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()
