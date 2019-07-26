"""
    Author: João Ventura <flatangleweb@gmail.com>


    This recipe shows sample code for creating a chart
    with sidereal zodiac

"""

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.ephem import swe, eph

# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Update object with the ayanamsa value
asc = chart.get(const.HOUSE10)
new_lon = asc.lon - swe.get_ayanamsa(date.jd, const.AY_LAHIRI)
asc.relocate(new_lon)
print(asc)
