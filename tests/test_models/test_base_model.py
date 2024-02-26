import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()

    def test_attributes(self):
        """Test BaseModel attributes"""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        
    def test_id_generation(self):
        """Test ID generation"""
        self.assertIsNotNone(self.model.id)
        self.assertEqual(len(self.model.id), 36)

    def test_created_at(self):
        """Test created_at attribute"""
        self.assertIsInstance(self.model.created_at, datetime)
        
    def test_updated_at(self):
        """Test updated_at attribute"""
        self.assertIsInstance(self.model.updated_at, datetime)

