"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for computing 
    the almutem protocol.

"""

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.protocols import almutem


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Print almutem scores
alm = almutem.compute(chart)
for k, v in alm['Score'].items():
    print(k, v)  # Mercury scores 40