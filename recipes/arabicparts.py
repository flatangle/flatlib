"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for computing 
    arabic parts.

"""

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.tools import arabicparts


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Retrieve the Pars Spirit
parsSpirit = arabicparts.getPart(arabicparts.PARS_SPIRIT, chart)
print(parsSpirit)    # <Pars Spirit Sagittarius +03:52:01>