# Import libraries
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from game import Game

#Variables
Games = []

#Methods
def writeGamesToFile():
    File_object = open("GameData.txt","w")
    lines = []
    for x in range(0, len(Games)):
        game = Games[x]
        line = ''
        line = line + str(game.date) + ','
        line = line + str(game.visitor) + ',' + str(game.home) + ','
        line = line + str(game.visitorScore) + ',' + str(game.homeScore) + ','
        line = line + str(game.OT) + ":"
        line = line + '{}'
        lines.append(line)
        
    File_object.writelines(lines)
    File_object.close()
        

def makeUrlBBallRef(month, year):
    return 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_games-' + month + '.html'

# Advance a month
def nextMonth(month):
    months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    if months.index(month) == 11:
        return "january"
    else:
        return months[months.index(month)+1]

def getText(list):
    texts = []
    for string in list:
        soupy = BeautifulSoup((str("<html>") + str(string) + str("</html>")))
        text = soupy.get_text()
        texts.append(text)
    return texts
        
    
def add(input):
    
    #Create Beautiful Soup of the Website
    soup = BeautifulSoup(input)
    date = getText(soup.find('tbody').select('th[data-stat="date_game"]'))
    visitor = getText(soup.find('tbody').select('td[data-stat="visitor_team_name"]'))
    home = getText(soup.find('tbody').select('td[data-stat="home_team_name"]'))
    visitorScore = getText(soup.find('tbody').select('td[data-stat="visitor_pts"]'))
    homeScore = getText(soup.find('tbody').select('td[data-stat="home_pts"]'))
    OT = getText(soup.find('tbody').select('td[data-stat="overtimes"]'))
    for x in range(0, len(date)):
        Games.append(Game(visitor[x],home[x],date[x],visitorScore[x],homeScore[x],OT[x]))
    
    
#Content
year = 2000
month = "october"
while year < 2020:
    print(year, month)
    try: 
        source = urllib.request.urlopen(
        makeUrlBBallRef(month, year)).read()
        add(source)
    except urllib.error.HTTPError:
        pass       
    month = nextMonth(month)
    if month == 'may':
        year = year + 1
        month = 'october'       
writeGamesToFile()
print('done')
        

        

    

