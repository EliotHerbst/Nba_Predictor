# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:50:08 2019

@author: Eliot Herbst
"""
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

class Game(object): 
#Reading and Writing to File
    
File_object = open("GameData.txt","w")