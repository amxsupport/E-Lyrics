#!/usr/bin/python3
"""This module prompts a user for a song and returns the top 10 words from it that are used least frequently in the English-speaking world"""
"""Import modules and defines Request Headers for Words API get request"""

import requests, re, operator
headers = {
    'x-rapidapi-host': "ENTER WORDS API HOST URL",
    'x-rapidapi-key': "ENTER API KEY FOR WORDS API"
    }

