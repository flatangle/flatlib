"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling 
    aspects.

"""

from flatlib import aspects
from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Retrieve the Sun and Moon 
sun = chart.get(const.SUN)
moon = chart.get(const.MOON)

# Get the aspect
aspect = aspects.getAspect(sun, moon, const.MAJOR_ASPECTS)
print(aspect)     # <Moon Sun 90 Applicative +00:24:30>