# Nba_Predictor

This is a project that scrapes data from past NBA games to use with an API to predict future scores and wins for NBA games.

We first build a parser that cycles through different pages from the NBA stats page to pull basic data from every game from the past xx number of years.

We also create out Game object that stores all of our data that will be sent into our GameData txt file, which stores all of our data. 

For now, it stores stats like: visitor, home, date, visitorScore, homeScore, and if it went into overtime (OT) 
