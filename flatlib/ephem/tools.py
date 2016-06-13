"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    
    This module implements functions specifically 
    for the ephem subpackage.
    
"""

from . import swe
from flatlib import angle
from flatlib import const
from flatlib import utils


# One arc-second error for iterative algorithms
MAX_ERROR = 0.0003


# === Object positions === #

def pfLon(jd, lat, lon):
    """ Returns the ecliptic longitude of Pars Fortuna.
    It considers diurnal or nocturnal conditions.
    
    """
    sun = swe.sweObjectLon(const.SUN, jd)
    moon = swe.sweObjectLon(const.MOON, jd)
    asc = swe.sweHousesLon(jd, lat, lon,
                           const.HOUSES_DEFAULT)[1][0]
    
    if isDiurnal(jd, lat, lon):
        return angle.norm(asc + moon - sun)
    else:
        return angle.norm(asc + sun - moon)
    
    
# === Diurnal  === #

def isDiurnal(jd, lat, lon):
    """ Returns true if the sun is above the horizon
    of a given date and location. 
    
    """
    sun = swe.sweObject(const.SUN, jd)
    mc = swe.sweHousesLon(jd, lat, lon, 
                          const.HOUSES_DEFAULT)[1][1]
    ra, decl = utils.eqCoords(sun['lon'], sun['lat'])
    mcRA, _ = utils.eqCoords(mc, 0.0)
    return utils.isAboveHorizon(ra, decl, mcRA, lat)
    

# === Iterative algorithms === #

def syzygyJD(jd):
    """ Finds the latest new or full moon and
    returns the julian date of that event. 
    
    """
    sun = swe.sweObjectLon(const.SUN, jd)
    moon = swe.sweObjectLon(const.MOON, jd)
    dist = angle.distance(sun, moon)
    
    # Offset represents the Syzygy type. 
    # Zero is conjunction and 180 is opposition.
    offset = 180 if (dist >= 180) else 0
    while abs(dist) > MAX_ERROR:
        jd = jd - dist / 13.1833  # Moon mean daily motion
        sun = swe.sweObjectLon(const.SUN, jd)
        moon = swe.sweObjectLon(const.MOON, jd)
        dist = angle.closestdistance(sun - offset, moon)
    return jd

def solarReturnJD(jd, lon, forward=True):
    """ Finds the julian date before or after 
    'jd' when the sun is at longitude 'lon'. 
    It searches forward by default.
    
    """
    sun = swe.sweObjectLon(const.SUN, jd)
    if forward:
        dist = angle.distance(sun, lon)
    else:
        dist = -angle.distance(lon, sun)
        
    while abs(dist) > MAX_ERROR:
        jd = jd + dist / 0.9833  # Sun mean motion
        sun = swe.sweObjectLon(const.SUN, jd)
        dist = angle.closestdistance(sun, lon)
    return jd


# === Other algorithms === #

def nextStationJD(ID, jd):
    """ Finds the aproximate julian date of the
    next station of a planet.

    """
    speed = swe.sweObject(ID, jd)['lonspeed']
    for i in range(2000):
        nextjd = jd + i / 2
        nextspeed = swe.sweObject(ID, nextjd)['lonspeed']
        if speed * nextspeed <= 0:
            return nextjd
    return None
