#!/usr/bin/python3
"""This module creates the BaseModel class"""

import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel():
    """A class named BaseModel
    Attributes:
    attr1(id): object id
    attr2(created_at): datetime instance is created
    attr3(updated_at): datetime instance is created and updated when changed
    """
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

