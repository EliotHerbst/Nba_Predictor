# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:50:08 2019

@author: Eliot Herbst
"""
# Grabbing text in between any html tags and turn it into a BeautifulSoup object
def getText(list):
    texts = []
    for string in list:
        soupy = BeautifulSoup((str("<html>") + str(string) + str("</html>")), 'html.parser')
        text = soupy.get_text()
        texts.append(text)
    return texts
# Next steps to be completed
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

source = urllib.request.urlopen(
        "https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1").read()
soup = BeautifulSoup(source, 'html.parser')
date = getText(soup.find('body').select('td[class="first"]'))


print(date)

    
#File_object = open("GameData.txt","w")
