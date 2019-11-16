# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
source = urllib.request.urlopen('https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1').read()

soup = BeautifulSoup(source,'lxml')

print(soup.title)