"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling some 
    of the chart dynamics.

"""

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.tools.chartdynamics import ChartDynamics


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Build ChartDynamics object
dyn = ChartDynamics(chart)

# Which dignities of Jupiter belong to Sun
dign = dyn.inDignities(const.JUPITER, const.SUN)
print(dign)   # ['dayTrip', 'ruler']

# In which dignities Jupiter receives Mars
dign = dyn.receives(const.JUPITER, const.MARS)
print(dign)   # ['nightTrip']

# Mutual receptions between Sun and Moon
#  - Sun receives the Moon in diurnal triplicity
#  - Moon receives the Sun in the participant triplicity
dign = dyn.mutualReceptions(const.SUN, const.MOON)
print(dign)   # [('dayTrip', 'partTrip')]

# Last separation and next application of 
asps = dyn.immediateAspects(const.SUN, const.MAJOR_ASPECTS)
print(asps)   # (None, {'id': 'Saturn', 'orb': 12.1391, 'asp': 120})

# Void of course
voc = dyn.isVOC(const.MERCURY)
print(voc)    # False