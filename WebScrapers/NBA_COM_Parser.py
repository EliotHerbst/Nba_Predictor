# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:50:08 2019

@author: Eliot Herbst
"""
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from game import Game

# Grabbing text in between any html tags and turn it into a BeautifulSoup object
def getText(list):
    texts = []
    for string in list:
        soupy = BeautifulSoup((str("<html>") + str(string) + str("</html>")), 'html.parser')
        text = soupy.get_text()
        texts.append(text)
    return texts

#Gets NBA.com date url format from basketball reference date format
def getNBAdate(str):
    monthDayYear = str[str.index(",")+2:]
    month = monthDayYear[0:monthDayYear.index(" ")]
    if month == "Jan":
        month = "01"
    elif month == "Feb":
        month = "02"
    elif month == "Mar":
        month = "03"
    elif month == "Apr":
        month = "04"
    elif month == "Oct":
        month = "10"
    elif month == "Nov":
        month = "11"
    elif month == "Dec":
        month = "12"
        
    monthDayYear = monthDayYear[monthDayYear.index(" ")+1:]
    day = monthDayYear[0:monthDayYear.index(",")]
    if len(day) == 1:
        day = "0" + day
    monthDayYear = monthDayYear[monthDayYear.index(", ") + 2:]
    year = monthDayYear
    
    return month + "%2F" + day +"%2F" + year
    
#Gets NBA.com season url format for season from date
def getSeason(string):
    month = string[0:string.index("%2F")]
    year = int(string[string.rindex("%2F")+3:])
    mon = int(month)
    if mon > 8:
        return str(year) + "-" + str(year+1)[2:]
    else:
        return str(year-1) + "-" + str(year)[2:]
        
    
def getStats(game):
    try:
        url = getUrl(game)
        home = game.home
        visitor = game.visitor
        input = urllib.request.urlopen(url).read()  
        print(input)
    except urllib.error.HTTPError:
        pass    
    
    
#Fix with proper month and day values    
def get5DaysBefore(string):
    month = string[0:string.index("%2F")]
    year = int(string[string.rindex("%2F")+3:])
    day = int(string[string.index("%2F") +3: string.rindex("%2F")])
    mon = int(month)
    if(day < 6):
        if(mon < 2):
            return "12" + "%2F" + str(28 - (5-day)) + "%2F" + str(year-1)
        else:
            return str(mon-1) + "%2F" + str(28 - (5-day)) + "%2F" + str(year)
    else:
        return str(mon) +"%2F" + str(day-5) + "%2F"  + str(year)
    
def getUrl(game):
    visitor = game.visitor
    home = game.home
    date = game.date
    visitorScore = game.visitorScore
    homeScore = game.homeScore
    nbaDate = getNBAdate(date)
    url1 =  "https://stats.nba.com/teams/advanced/?sort=TEAM_NAME&dir=1&" + "Season=" + getSeason(nbaDate) + "&SeasonType=Regular%20Season"
    url1 = url1 + "&DateFrom=" + get5DaysBefore(nbaDate) +"&DateTo=" + nbaDate
    return url1

dateStr = "Fri, Nov 5, 1999"
print(getNBAdate(dateStr))
print(getSeason(getNBAdate(dateStr)))
print(get5DaysBefore(getNBAdate(dateStr)))
"""   
# Next steps to be completed

import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

source = urllib.request.urlopen(
        "https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1").read()
soup = BeautifulSoup(source, 'html.parser')
date = getText(soup.find('body').select('td[class="first"]'))


print(date)
"""
    
#File_object = open("GameData.txt","w")
