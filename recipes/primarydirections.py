"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling the 
    primary directions.

"""

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.predictives import primarydirections


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# MC will be used for calculating arcs
mc = chart.get(const.MC)

# Get a promissor and significator
prom = chart.get(const.MARS)
sig = chart.get(const.MERCURY)

# Compute arc in zodiaco (zerolat = True)
arc = primarydirections.getArc(prom, sig, mc, pos, zerolat=True)
print(arc)  # 56.17347

# Compute arc in mundo
arc = primarydirections.getArc(prom, sig, mc, pos, zerolat=False)
print(arc)  # 56.74266

# Create Primary Directions class
from flatlib.predictives.primarydirections import PrimaryDirections
pd = PrimaryDirections(chart)

# Get arcs
arc = pd.getArc(pd.N(const.MARS), pd.N(const.MERCURY))
print(arc['arcm'])  # 56.74266 (arc in-mundo)
print(arc['arcz'])  # 56.17347 (arc in-zodiaco)