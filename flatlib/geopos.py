"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module provides functions and a class for handling 
    geographic positions. Each latitude/longitude is an angle 
    represented by a <float> value.

"""

from . import angle


# Modes
LAT = 0
LON = 1

# Mappings
SIGN = {'N': '+', 'S': '-', 'E': '+', 'W': '-'}
CHAR = {
    LAT: {'+': 'N', '-': 'S'},
    LON: {'+': 'E', '-': 'W'},
}


# === Conversions === #

def toFloat(value):
    """ Converts angle representation to float. 
    Accepts angles and strings such as "12W30:00".
    
    """
    if isinstance(value, str):
        # Find lat/lon char in string and insert angle sign
        value = value.upper()
        for char in ['N', 'S', 'E', 'W']:
            if char in value:
                value = SIGN[char] + value.replace(char, ':')
                break
    return angle.toFloat(value)

def toList(value):
    """ Converts angle float to signed list. """
    return angle.toList(value)

def toString(value, mode):
    """ Converts angle float to string. 
    Mode refers to LAT/LON.
    
    """
    string = angle.toString(value)
    sign = string[0]
    separator = CHAR[mode][sign]
    string = string.replace(':', separator, 1)
    return string[1:]


# ------------------ #
#    GeoPos Class    #
# ------------------ #

class GeoPos:
    """ This class represents a geographic position 
    on the planet specified by a given lat and lon.
    
    Objects of this class can be instantiated with
    GeoPos("45N32", "128W45") or another angle type
    such as strings, signed lists or floats. 
    
    """
    
    def __init__(self, lat, lon):
        self.lat = toFloat(lat)
        self.lon = toFloat(lon)
        
    def slists(self):
        """ Return lat/lon as signed lists. """
        return [
            toList(self.lat), 
            toList(self.lon)
        ]
    
    def strings(self):
        """ Return lat/lon as strings. """
        return [
            toString(self.lat, LAT),
            toString(self.lon, LON)
        ]
        
    def __str__(self):
        strings = self.strings()
        return '<%s %s>' % (strings[0], strings[1])