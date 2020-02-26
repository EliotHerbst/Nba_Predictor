# Import libraries
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from game import Game

# PART 1
# Make array for Game to be stored
Games = []


def writeGamesToFile():
    File_object = open("GameDataTesting.txt", "a")
    lines = []
    # Make string representation
    for x in range(0, len(Games)):
        game = Games[x]
        line = ''
        line = line + str(game.date) + ','
        line = line + str(game.visitor) + ',' + str(game.home) + ','
        line = line + str(game.visitorScore) + ',' + str(game.homeScore) + ','
        line = line + str(game.OT) + ":"
        line = line + '{}'
        lines.append(line)
    # Close the file
    print(Games)
    print(lines)
    File_object.writelines(lines)
    File_object.close()


def makeUrlBBallRef(month, year):
    return 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_games-' + month + '.html'


# Advance a month
def nextMonth(month):
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"]
    # Move to next year
    if months.index(month) == 11:
        return "january"
    else:
        return months[months.index(month) + 1]


# Grabbing text in between any html tags and turn it into a BeautifulSoup object
def getText(list):
    texts = []
    for string in list:
        soupy = BeautifulSoup((str("<html>") + str(string) + str("</html>")), 'html.parser')
        text = soupy.get_text()
        texts.append(text)
    return texts


def add(input):
    # Create Beautiful Soup of the Website
    soup = BeautifulSoup(input, 'html.parser')
    date = getText(soup.find('tbody').select('th[data-stat="date_game"]'))
    visitor = getText(soup.find('tbody').select('td[data-stat="visitor_team_name"]'))
    home = getText(soup.find('tbody').select('td[data-stat="home_team_name"]'))
    visitorScore = getText(soup.find('tbody').select('td[data-stat="visitor_pts"]'))
    homeScore = getText(soup.find('tbody').select('td[data-stat="home_pts"]'))
    OT = getText(soup.find('tbody').select('td[data-stat="overtimes"]'))
    print(len(date))
    for x in range(0, len(date)):
        g = Game(visitor[x], home[x], date[x], visitorScore[x], homeScore[x], OT[x])
        if g.visitorScore == "" or g.homeScore == "":
            pass
        else:
            print(x)
            Games.append(g)


# For now, starting with year 2000, could change later
year = 2020
month = "october"
# Still in current season
while month != "march":
    print(year, month)
    # If a year or something doesn't exist, then throw an error and then just skip it
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
print('Completed scrape')
