#!/usr/bin/python3
"""This module creates the Song class"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import *

metadata = Base.metadata


