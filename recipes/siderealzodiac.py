"""
    Author: João Ventura <flatangleweb@gmail.com>


    This recipe shows sample code for creating a chart
    with sidereal zodiac

"""

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Get a copy of the chart in the sidereal zodiac
sid_chart = chart.to_sidereal_zodiac(const.AY_LAHIRI)
print(sid_chart.get(const.SATURN))
