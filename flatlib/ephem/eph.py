"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    
    This module implements functions for retrieving 
    astronomical and astrological data from an ephemeris.
    
    It is as middle layer between the Swiss Ephemeris 
    and user software. Objects are treated as python 
    dicts and jd/lat/lon as float.
  
"""

from . import swe
from . import tools
from flatlib import angle
from flatlib import const


# === Objects === #

def getObject(ID, jd, lat, lon):
    """ Returns an object for a specific date and 
    location.
    
    """
    if ID == const.SOUTH_NODE:
        obj = swe.sweObject(const.NORTH_NODE, jd)
        obj.update({
            'id': const.SOUTH_NODE,
            'lon': angle.norm(obj['lon'] + 180)
        })
    elif ID == const.PARS_FORTUNA:
        pflon = tools.pfLon(jd, lat, lon)
        obj = {
            'id': ID,
            'lon': pflon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }
    elif ID == const.SYZYGY:
        szjd = tools.syzygyJD(jd)
        obj = swe.sweObject(const.MOON, szjd)
        obj['id'] = const.SYZYGY
    else:
        obj = swe.sweObject(ID, jd)
    
    _signInfo(obj)
    return obj


# === Houses === #

def getHouses(jd, lat, lon, hsys):
    """ Returns lists of houses and angles. """
    houses, angles = swe.sweHouses(jd, lat, lon, hsys)
    for house in houses:
        _signInfo(house)
    for angle in angles:
        _signInfo(angle)
    return (houses, angles)


# === Fixed stars === #

def getFixedStar(ID, jd):
    """ Returns a fixed star. """
    star = swe.sweFixedStar(ID, jd)
    _signInfo(star)
    return star


# === Solar returns === #

def nextSolarReturn(jd, lon):
    """ Return the JD of the next solar return. """
    return tools.solarReturnJD(jd, lon, True)

def prevSolarReturn(jd, lon):
    """ Returns the JD of the previous solar return. """
    return tools.solarReturnJD(jd, lon, False)


# === Sunrise and sunsets === #
    
def nextSunrise(jd, lat, lon):
    """ Returns the JD of the next sunrise. """
    return swe.sweNextTransit(const.SUN, jd, lat, lon, 'RISE')

def nextSunset(jd, lat, lon):
    """ Returns the JD of the next sunset. """
    return swe.sweNextTransit(const.SUN, jd, lat, lon, 'SET')

def lastSunrise(jd, lat, lon):
    """ Returns the JD of the last sunrise. """
    return nextSunrise(jd - 1.0, lat, lon)

def lastSunset(jd, lat, lon):
    """ Returns the JD of the last sunset. """
    return nextSunset(jd - 1.0, lat, lon)


# === Stations === #

def nextStation(ID, jd):
    """ Returns the aproximate jd of the next station. """
    return tools.nextStationJD(ID, jd)


# === Other functions === #

def _signInfo(obj):
    """ Appends the sign id and longitude to an object. """
    lon = obj['lon']
    obj.update({
        'sign': const.LIST_SIGNS[int(lon / 30)],
        'signlon': lon % 30
    })


# === Objects and houses (sidereal and topocentric functions) === #

def get_object(obj, jd, lat=None, lon=None, alt=None, mode=None):
    """
    Returns an object for a specific date and location.
    - If lat/lon/alt values are set, it returns the topocentric position
    - If mode is set, returns sidereal positions for the given mode

    :param obj: the object
    :param jd: the julian date
    :param lat: the latitude in degrees
    :param lon: the longitude in degrees
    :param alt: the altitude above msl in meters
    :param mode: the ayanamsa
    :return: dictionary
    """

    if obj == const.SOUTH_NODE:
        eph_obj = swe.swe_object(const.NORTH_NODE, jd, lat, lon, alt, mode)
        eph_obj.update({
            'id': const.SOUTH_NODE,
            'lon': angle.norm(eph_obj['lon'] + 180)
        })

    elif obj == const.PARS_FORTUNA:
        # TODO: tools.pfLon must compute sidereal/topocentric positions
        pflon = tools.pfLon(jd, lat, lon)
        eph_obj = {
            'id': obj,
            'lon': pflon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }

    elif obj == const.SYZYGY:
        szjd = tools.syzygyJD(jd)
        eph_obj = swe.swe_object(const.MOON, szjd, lat, lon, alt, mode)
        eph_obj['id'] = const.SYZYGY

    else:
        eph_obj = swe.swe_object(obj, jd, lat, lon, alt, mode)

    _signInfo(eph_obj)
    return eph_obj


def get_houses(jd, lat, lon, hsys, mode=None):
    """
    Returns a list of house and angle cusps.
    - If mode is set, returns sidereal positions for the given mode

    :param jd: the julian date
    :param lat: the latitude in degrees
    :param lon: the longitude in degrees
    :param hsys: the house system
    :param mode: the ayanamsa
    :return: list of houses and angles
    """
    houses, angles = swe.swe_houses(jd, lat, lon, hsys, mode)

    for house in houses:
        _signInfo(house)
    for angle in angles:
        _signInfo(angle)

    return houses, angles
