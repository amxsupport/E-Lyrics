#!/usr/bin/python3
"""This module prompts a user for a song and returns the top 10 words from it that are used least frequently in the English-speaking world"""
"""Import modules and defines Request Headers for Words API get request"""

import requests, re, operator
headers = {
    'x-rapidapi-host': "ENTER WORDS API HOST URL",
    'x-rapidapi-key': "ENTER API KEY FOR WORDS API"
    }

"""Prompt the user"""

print('Enter an artist and song! Then see the words from the song that are used least frequently in the English-speaking world!', '\n')
artist = input('Artist: ')
song = input('Song: ')

"""Fetch lyrics from lyrics.ovh based on user input and print them. Validate input data"""

lyrics_dict = requests.get('https://api.lyrics.ovh/v1/{:}/{:}'.format(artist, song)).json()
if lyrics_dict == None:
    print("Sorry, that song does not exist. Check your spelling and try again")
    exit
lyrics = lyrics_dict.get('lyrics')
print("Lyrics...", "\n", "\n", lyrics)

