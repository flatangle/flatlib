"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    
    This module provides useful functions for handling 
    planetary times.
    
    The most import element is the HourTable class 
    which handles all queries to the planetary rulers 
    and hour rulers, including the start and ending 
    datetimes of each hour ruler.
  
"""

from flatlib import const
from flatlib.ephem import ephem
from flatlib.datetime import Datetime


# Planetary rulers starting at Sunday
DAY_RULERS = [
    const.SUN,
    const.MOON,
    const.MARS,
    const.MERCURY,
    const.JUPITER,
    const.VENUS,
    const.SATURN
]

NIGHT_RULERS = [
    const.JUPITER,
    const.VENUS,
    const.SATURN,
    const.SUN,
    const.MOON,
    const.MARS,
    const.MERCURY
]

# Planetary hours round list starting 
# at Sunday's sunrise
ROUND_LIST = [
    const.SUN,
    const.VENUS,
    const.MERCURY,
    const.MOON,
    const.SATURN,
    const.JUPITER,
    const.MARS
]


# === Private functions === #

def nthRuler(n, dow):
    """ Returns the n-th hour ruler since last sunrise
    by day of week. Both arguments are zero based.
    
    """
    index = (dow * 24 + n) % 7
    return ROUND_LIST[index]

def hourTable(date, pos):
    """ Creates the planetary hour table for a date 
    and position. 
    
    The table includes both diurnal and nocturnal 
    hour sequences and each of the 24 entries (12 * 2)
    are like (startJD, endJD, ruler).
    
    """
    
    lastSunrise = ephem.lastSunrise(date, pos)
    middleSunset = ephem.nextSunset(lastSunrise, pos)
    nextSunrise = ephem.nextSunrise(date, pos)
    table = []
    
    # Create diurnal hour sequence
    length = (middleSunset.jd - lastSunrise.jd) / 12.0
    for i in range(12):
        start = lastSunrise.jd + i * length
        end = start + length
        ruler = nthRuler(i, lastSunrise.date.dayofweek())
        table.append([start, end, ruler])
        
    # Create nocturnal hour sequence
    length = (nextSunrise.jd - middleSunset.jd) / 12.0
    for i in range(12):
        start = middleSunset.jd + i * length
        end = start + length
        ruler = nthRuler(i + 12, lastSunrise.date.dayofweek())
        table.append([start, end, ruler])
        
    return table

def getHourTable(date, pos):
    """ Returns an HourTable object. """
    table = hourTable(date, pos)
    return HourTable(table, date)


# ------------------- #
#   HourTable Class   #
# ------------------- #

class HourTable:
    """ This class represents a Planetary Hour Table
    and includes methods to access its properties.
    
    """
    
    def __init__(self, table, date):
        self.table = table
        self.date = date
        self.currIndex = self.index(date)
        
    def index(self, date):
        """ Returns the index of a date in the table. """
        for (i, (start, end, ruler)) in enumerate(self.table):
            if start <= date.jd <= end:
                return i
        return None
    
    # === Properties === #
    
    def dayRuler(self):
        """ Returns the current day ruler. """
        return self.table[0][2]
    
    def nightRuler(self):
        """ Returns the current night ruler. """
        return self.table[12][2]
    
    def currRuler(self):
        """ Returns the current day or night 
        ruler considering if it's day or night.
        
        """
        if self.currIndex < 12:
            return self.dayRuler()
        else:
            return self.nightRuler()
        
    def hourRuler(self):
        """ Returns the current hour ruler. """
        return self.table[self.currIndex][2]
        
    def currInfo(self):
        """ Returns information about the current
        planetary time.
        
        """
        return self.indexInfo(self.currIndex)
    
    def indexInfo(self, index):
        """ Returns information about a specific 
        planetary time. 
        
        """
        entry = self.table[index]
        info = {
            # Default is diurnal
            'mode': 'Day',
            'ruler': self.dayRuler(),
            'dayRuler': self.dayRuler(),
            'nightRuler': self.nightRuler(),
            'hourRuler': entry[2],
            'hourNumber': index + 1,
            'tableIndex': index,
            'start': Datetime.fromJD(entry[0], self.date.utcoffset),
            'end': Datetime.fromJD(entry[1], self.date.utcoffset)
        }
        if index >= 12:
            # Set information as nocturnal
            info.update({
                'mode': 'Night',
                'ruler': info['nightRuler'],
                'hourNumber': index + 1 - 12
            })
        return info