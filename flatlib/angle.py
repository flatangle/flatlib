"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module provides useful functions for handling angles.
    An angle is represented in this library as a <float> value.
  
    It also provides useful functions for handling the conversion 
    of angles between strings, signed lists and float values.
  
    The conversion functions assume that:
    
    1. Angle strings are like "-12:30:00".
    2. Signed lists are like ['-',12,30,00].
    3. Regular lists are like [+12,30,30] or [-0.0,30,30]
    4. Float value are fractions of an angle with base 60.
       Eg. "-12:30:00" is converted to -12.5.
  
    Regular lists are discouraged because it is hard to represent
    negative angles such as ['-',00,30,00]. In this case a -0.0
    should be used, as [-0.0,30,00], and converted to a signed 
    list for further use.
    
"""

import math



# === Angular utilities === #

def norm(angle):
    """ Normalizes an angle between 0 and 360. """
    return angle % 360

def znorm(angle):
    """ Normalizes an angle between -180 and 180. """
    angle = angle % 360
    return angle if angle <= 180 else angle - 360

def distance(angle1, angle2):
    """ Angular distance from angle1 to angle2 (ccw). """
    return norm(angle2 - angle1)

def closestdistance(angle1, angle2):
    """ Closest distance from angle1 to angle2 (ccw is positive). """
    return znorm(angle2 - angle1)
    

# === Signed Lists utilities === #

def _fixSlist(slist):
    """ Guarantees that a signed list has exactly four elements. """
    slist.extend([0] * (4-len(slist)))
    return slist[:4]

def _roundSlist(slist):
    """ Rounds a signed list over the last element and removes it. """
    slist[-1] = 60 if slist[-1] >= 30 else 0
    for i in range(len(slist)-1, 1, -1):
        if slist[i] == 60:
            slist[i] = 0
            slist[i-1] += 1
    return slist[:-1]


# === Base conversions === #

def strSlist(string):
    """ Converts angle string to signed list. """
    sign = '-' if string[0] == '-' else '+'
    values = [abs(int(x)) for x in string.split(':')]
    return _fixSlist(list(sign) + values)

def slistStr(slist):
    """ Converts signed list to angle string. """
    slist = _fixSlist(slist)
    string = ':'.join(['%02d' % x for x in slist[1:]])
    return slist[0] + string

def slistFloat(slist):
    """ Converts signed list to float. """
    values = [v / 60**(i) for (i,v) in enumerate(slist[1:])]
    value = sum(values)
    return -value if slist[0] == '-' else value

def floatSlist(value):
    """ Converts float to signed list. """
    slist = ['+', 0, 0, 0, 0]
    if value < 0:
        slist[0] = '-'
    value = abs(value)
    for i in range(1,5):
        slist[i] = math.floor(value)
        value = (value - slist[i]) * 60
    return _roundSlist(slist)

def strFloat(string):
    """ Converts angle string to float. """
    slist = strSlist(string)
    return slistFloat(slist)

def floatStr(value):
    """ Converts angle float to string. """
    slist = floatSlist(value)
    return slistStr(slist)


# === Direct conversions === #

def toFloat(value):
    """ Converts string or signed list to float. """
    if isinstance(value, str):
        return strFloat(value)
    elif isinstance(value, list):
        return slistFloat(value)
    else:
        return value
    
def toList(value):
    """ Converts angle float to signed list. """
    return floatSlist(value)

def toString(value):
    """ Converts angle float to string. """
    return floatStr(value)
