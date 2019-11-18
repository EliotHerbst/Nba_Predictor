
# Pulled out object from scraper file to reference for later
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