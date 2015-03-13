"""
    Author: João Ventura <flatangleweb@gmail.com>
    

    Solar return date and time jumps forward and backwards 
    every year. This is related with the average number of
    days in a year (365.25). However, in certain conditions,
    the time distance is greater than 24h and increases with
    the years.
    
    This recipe was implemented to reply to a topic opened
    at http://skyscript.co.uk/forums/viewtopic.php?t=8563
    
    Set the birth date and time and 'span' as the number of 
    years to see what happens with the hourly distances.
    
    To plot the graphics you must have matplotlib installed.

"""

from flatlib import const
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.ephem import ephem


def plot(hdiff, title):
    """ Plots the solar return hour distance to 
    anniversary using matplotlib.
    
    """
    import matplotlib.pyplot as plt
    years = [elem[0] for elem in hdiff]
    hours = [elem[1] for elem in hdiff]
    plt.plot(years, hours)
    plt.ylabel('Hour distance')
    plt.xlabel('Year')
    plt.title(title)
    plt.axhline(y=-24, c='red')
    plt.show()


# Set the birth date and time 
date = [1983, 3, 21]
time = ['+', 0, 0, 0]

# Get the sun position at birth
dt = Datetime(date, time)
pos = GeoPos('38n32', '8w54')
sun = ephem.getObject(const.SUN, dt, pos)

# Collect hour differences for the following 100 years
hdiff = []
span = 100
for year in range(date[0], date[0] + 1 + span):
    
    # Get solar return of the year
    dt = Datetime('%s/01/01' % year, '00:00')
    sr = ephem.nextSolarReturn(dt, sun.lon)
    
    # Create anniversary date for the year
    date[0] = year
    an = Datetime(date, time)
    
    # Get the difference in days but add in hours
    diff = sr.jd - an.jd
    hdiff.append((year, diff * 24))
    
print(hdiff)
plot(hdiff, 'Born on %s and living %s years' % (date[0]-span, span))