"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling 
    accidental dignities.

"""

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.dignities import accidental


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Get some objects
obj = chart.get(const.VENUS)
sun = chart.get(const.SUN)

# Sun relation
relation = accidental.sunRelation(obj, sun)
print(relation)

# Augmenting or Diminishing light
light = accidental.light(obj, sun)
print(light)

# Orientality
orientality = accidental.orientality(obj, sun)
print(orientality)

# Haiz
haiz = accidental.haiz(obj, chart)
print(haiz)