# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:50:08 2019

@author: Eliot Herbst
"""

# Next steps to be completed
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

source = urllib.request.urlopen(
        "https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1").read()
soup = BeautifulSoup(source, 'html.parser')

print(soup)

    
#File_object = open("GameData.txt","w")
