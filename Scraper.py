# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# PART 1


# Advance a month
def nextMonth(month):
    months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    if months.index(month) == 11:
        return "january"
    else:
        return months[months.index(month)+1]
    
def makeUrlBBallRef(month, year):
    # cycle through various years and mos
    return 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_games-' + month + '.html'
    
# Baseline start at 2009, because starting off with first 10 years
year = 2009
month = "october"
while year < 2019:
    # 2012 was an oddball year
    if year == 2012:
        year = 2013
    
    print(makeUrlBBallRef(month, year))
    source = urllib.request.urlopen(
        makeUrlBBallRef(month, year)).read()
    month = nextMonth(month)
    if month == 'april':
        year = year + 1
        month = 'october'
    
    
# Set the URL you want to webscrape from
source = urllib.request.urlopen(
        'https://www.basketball-reference.com/leagues/NBA_2020_games.html').read()

    

soup = BeautifulSoup(source,'lxml')

print(soup.title)
print("Part 1: URL scraping works")
