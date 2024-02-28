#!/usr/bin/python3
"""This module defines the Storage class"""
from models.base_model import BaseModel, Base
from models.song import Song
from models.word import Word
from models.interpretation import Interpretation
from models.suggestion import Suggestion
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os

classes = {"Song": Song, "Word": Word, "Interpretation": Interpretation,
           "Suggestion": Suggestion}

class Storage:
    """This class manages the MySQL database for Lyrics for Learning"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv("LYRICS_MYSQL_USER"), os.getenv("LYRICS_MYSQL_PWD"),
            os.getenv("LYRICS_MYSQL_HOST"), os.getenv("LYRICS_MYSQL_DB"),
            pool_pre_ping=True))

    def all(self, cls=None):
        """return a dictionary
        Return:
            returns a dictionary of objects
        """
        obj_dict = {}
        if cls is None:
            for obj in self.__session.query(Song, Word, Interpretation,
                                            Suggestion).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """add the object to the current database session
        Args:
            obj: given object
        """
        self.__session.add(obj)


