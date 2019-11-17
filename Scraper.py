# Import libraries
import urllib.request
from bs4 import BeautifulSoup

class Game(object):
  def __init__(self, visitor, home, date, visitorScore, homeScore, OT):
    self.visitor = visitor
    self.home = home
    self.date = date
    self.visitorScore = visitorScore
    self.homeScore = homeScore
    self.OT = OT  
  def __str__(self):
      return str(self.visitor) + " " + str(self.visitorScore) + " " + str(self.home) + " " + str(self.homeScore) + " " + str(self.date) + " " + str(self.OT)


# PART 1

Games = []

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
    
    
    
# Baseline start at 2009, because starting off with first 10 years
year = 2009
month = "october"
while year < 2020:
    # 2012 was an oddball year
    if year == 2012:
        year = 2013
    source = urllib.request.urlopen(
        makeUrlBBallRef(month, year)).read()
    add(source)
    month = nextMonth(month)
    if month == 'may':
        year = year + 1
        month = 'october'
        
writeGamesToFile();
print('done')
        

        

    

