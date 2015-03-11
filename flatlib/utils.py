"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    This module provides generic utility functions. 
"""

import math
from . import angle


# === Diurnal and nocturnal arcs === #

def ascdiff(decl, lat):
    """ Returns the Ascensional Difference of a point. """
    delta = math.radians(decl)
    phi = math.radians(lat)
    ad = math.asin(math.tan(delta) * math.tan(phi))
    return math.degrees(ad)

def dnarcs(decl, lat):
    """ Returns the diurnal and nocturnal arcs of a point. """
    dArc = 180 + 2 * ascdiff(decl, lat)
    nArc = 360 - dArc
    return (dArc, nArc)


# === Above horizon === #

def isAboveHorizon(ra, decl, mcRA, lat):
    """ Returns if an object's 'ra' and 'decl' 
    is above the horizon at a specific latitude, 
    given the MC's right ascension.
    
    """
    # This function checks if the equatorial distance from 
    # the object to the MC is within its diurnal semi-arc.
    
    dArc, _ = dnarcs(decl, lat)
    dist = abs(angle.closestdistance(mcRA, ra))
    return dist <= dArc/2.0 + 0.0003  # 1 arc-second


# === Coordinate systems === #

def eqCoords(lon, lat):
    """ Converts from ecliptical to equatorial coordinates. 
    This algorithm is described in book 'Primary Directions', 
    pp. 147-150.
    
    """
    # Convert to radians
    _lambda = math.radians(lon)
    _beta = math.radians(lat)
    _epson = math.radians(23.44)  # The earth's inclination
    
    # Declination in radians
    decl = math.asin(math.sin(_epson) * math.sin(_lambda) * math.cos(_beta) + \
           math.cos(_epson) * math.sin(_beta))
    
    # Equatorial Distance in radians
    ED = math.acos(math.cos(_lambda) * math.cos(_beta) / math.cos(decl))
    
    # RA in radians
    ra = ED if lon < 180 else math.radians(360) - ED
    
    # Correctness of RA if longitude is close to 0º or 180º in a radius of 5º
    if (abs(angle.closestdistance(lon, 0)) < 5 or 
        abs(angle.closestdistance(lon, 180)) < 5):
            a = math.sin(ra) * math.cos(decl)
            b = math.cos(_epson) * math.sin(_lambda) * math.cos(_beta) - \
                math.sin(_epson) * math.sin(_beta)
            if (math.fabs(a-b) > 0.0003):
                ra = math.radians(360) - ra
                
    return (math.degrees(ra), math.degrees(decl))