"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for calculating the dates
    of the previous and next solar and lunar eclipses.

"""

from flatlib.datetime import Datetime
from flatlib.ephem import ephem


# Build a Datetime object
date = Datetime('2016/10/11', '12:00', '+00:00')

# Get the date of the maximum phase of the next global lunar eclipse
lunar_eclipse = ephem.nextLunarEclipse(date)
print(lunar_eclipse)  # <2017/02/11 00:43:48 00:00:00>

# Get the date of the maximum phase of the next global solar eclipse
solar_eclipse = ephem.nextSolarEclipse(date)
print(solar_eclipse)  # <2017/02/26 14:53:23 00:00:00>
