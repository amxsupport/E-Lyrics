#!/usr/bin/python3
"""Script for testing the addition of songs to the site"""
import models, requests
from models.base_model import BaseModel
from models.song import Song
from models.word import Word
from models import storage

input_artist = input('Artist: ')
input_song = input('Song: ')
db_songs = {}
for song in storage.all(Song).values():
    db_songs[song.title] = song
if db_songs.get(input_song) is None:


else:

