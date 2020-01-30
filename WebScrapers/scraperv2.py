# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:21:56 2020

@author: 18325
"""

from selenium import webdriver
from pandas import *
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import *

path_to_chromedriver = '/path/to/chromedriver' # Path to access a chrome driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)