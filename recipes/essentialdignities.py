"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling 
    essential dignities.

"""

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.dignities import essential


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Get the Asc ruler
asc = chart.get(const.ASC)
ascRulerID = essential.ruler(asc.sign)
ascRuler = chart.get(ascRulerID)
print(ascRuler)   # <Mercury Pisces +00:48:57 +01:29:49>

# Get the Asc ruler score
score = essential.score(ascRuler.id, ascRuler.sign, ascRuler.signlon)
print(score)

# Simpler alternative using the EssentialInfo class
info = essential.EssentialInfo(ascRuler)
print(info.score)