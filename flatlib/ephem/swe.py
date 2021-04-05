"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    
    This module implements a simple interface with the C 
    Swiss Ephemeris using the pyswisseph library.
    
    The pyswisseph library must be already installed and
    accessible.
  
"""

import swisseph
from flatlib import angle
from flatlib import const


# Map objects
SWE_OBJECTS = {
    const.SUN: 0,
    const.MOON: 1,
    const.MERCURY: 2, 
    const.VENUS: 3,
    const.MARS: 4,
    const.JUPITER: 5, 
    const.SATURN: 6,
    const.URANUS: 7,
    const.NEPTUNE: 8, 
    const.PLUTO: 9,
    const.CHIRON: 15, 
    const.NORTH_NODE: 10
}

# Map house systems
SWE_HOUSESYS = {
    const.HOUSES_PLACIDUS: b'P',
    const.HOUSES_KOCH: b'K', 
    const.HOUSES_PORPHYRIUS: b'O',
    const.HOUSES_REGIOMONTANUS: b'R',
    const.HOUSES_CAMPANUS: b'C',
    const.HOUSES_EQUAL: b'A',
    const.HOUSES_EQUAL_2: b'E',
    const.HOUSES_VEHLOW_EQUAL: b'V',
    const.HOUSES_WHOLE_SIGN: b'W',
    const.HOUSES_MERIDIAN: b'X', 
    const.HOUSES_AZIMUTHAL: b'H',
    const.HOUSES_POLICH_PAGE: b'T', 
    const.HOUSES_ALCABITUS: b'B',
    const.HOUSES_MORINUS: b'M'
}


# ==== Internal functions ==== #

def setPath(path):
    """ Sets the path for the swe files. """
    swisseph.set_ephe_path(path)


# === Object functions === #

def sweObject(obj, jd):
    """ Returns an object from the Ephemeris. """
    sweObj = SWE_OBJECTS[obj]
    sweList, flg = swisseph.calc_ut(jd, sweObj)
    return {
        'id': obj,
        'lon': sweList[0],
        'lat': sweList[1],
        'lonspeed': sweList[3],
        'latspeed': sweList[4]
    }
    
def sweObjectLon(obj, jd):
    """ Returns the longitude of an object. """
    sweObj = SWE_OBJECTS[obj]
    sweList, flg = swisseph.calc_ut(jd, sweObj)
    return sweList[0]

def sweNextTransit(obj, jd, lat, lon, flag):
    """ Returns the julian date of the next transit of
    an object. The flag should be 'RISE' or 'SET'. 
    
    """
    sweObj = SWE_OBJECTS[obj]
    flag = swisseph.CALC_RISE if flag == 'RISE' else swisseph.CALC_SET
    trans = swisseph.rise_trans(jd, sweObj, lon, lat, 0, 0, 0, flag)
    return trans[1][0]


# === Houses and angles === #
        
def sweHouses(jd, lat, lon, hsys):
    """ Returns lists of houses and angles. """
    hsys = SWE_HOUSESYS[hsys]
    hlist, ascmc = swisseph.houses(jd, lat, lon, hsys)
    # Add first house to the end of 'hlist' so that we
    # can compute house sizes with an iterator 
    hlist += (hlist[0],)
    houses = [
        {
            'id': const.LIST_HOUSES[i],
            'lon': hlist[i], 
            'size': angle.distance(hlist[i], hlist[i+1])
        } for i in range(12)
    ]
    angles = [
        {'id': const.ASC, 'lon': ascmc[0]}, 
        {'id': const.MC, 'lon': ascmc[1]},
        {'id': const.DESC, 'lon': angle.norm(ascmc[0] + 180)},
        {'id': const.IC, 'lon': angle.norm(ascmc[1] + 180)}
    ]
    return (houses, angles)
    
def sweHousesLon(jd, lat, lon, hsys):
    """ Returns lists with house and angle longitudes. """
    hsys = SWE_HOUSESYS[hsys]
    hlist, ascmc = swisseph.houses(jd, lat, lon, hsys)
    angles = [
        ascmc[0],
        ascmc[1],
        angle.norm(ascmc[0] + 180), 
        angle.norm(ascmc[1] + 180)
    ]
    return (hlist, angles)


# === Fixed stars === #

# Beware: the swisseph.fixstar_mag function is really 
# slow because it parses the fixstars.cat file every 
# time..

def sweFixedStar(star, jd):
    """ Returns a fixed star from the Ephemeris. """
    sweList, stnam, flg = swisseph.fixstar2_ut(star, jd)
    mag = swisseph.fixstar2_mag(star)
    return {
        'id': star, 
        'mag': mag,
        'lon': sweList[0],
        'lat': sweList[1]
    }


# === Eclipses === #

def solarEclipseGlobal(jd, backward):
    """ Returns the jd details of previous or next global solar eclipse. """

    sweList = swisseph.sol_eclipse_when_glob(jd, backward=backward)
    return {
        'maximum': sweList[1][0],
        'begin': sweList[1][2],
        'end': sweList[1][3],
        'totality_begin': sweList[1][4],
        'totality_end': sweList[1][5],
        'center_line_begin': sweList[1][6],
        'center_line_end': sweList[1][7],
    }

def lunarEclipseGlobal(jd, backward):
    """ Returns the jd details of previous or next global lunar eclipse. """

    sweList = swisseph.lun_eclipse_when(jd, backward=backward)
    return {
        'maximum': sweList[1][0],
        'partial_begin': sweList[1][2],
        'partial_end': sweList[1][3],
        'totality_begin': sweList[1][4],
        'totality_end': sweList[1][5],
        'penumbral_begin': sweList[1][6],
        'penumbral_end': sweList[1][7],
    }
