# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:21:56 2020

@author: 18325
"""

from selenium import webdriver

path_to_chromedriver = 'D:\Downloads\chromedriver_win32\chromedriver.exe' # Path to access a chrome driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

url = 'https://stats.nba.com/leaders'
browser.get(url)

table = browser.find_element_by_class_name('nba-stat-table__overflow')

player_ids = []
player_names = []
player_stats = []

for line_id, lines in enumerate(table.text.split('\n')):
    if line_id == 0:
        column_names = lines.split(' ')[1:]
    else:
        if line_id % 3 == 1:
            player_ids.append(lines)
        if line_id % 3 == 2:
            player_names.append(lines)
        if line_id % 3 == 0:
            player_stats.append( [float(i) for i in lines.split(' ')] )
            
print(player_stats)