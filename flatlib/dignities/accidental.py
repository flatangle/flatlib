"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    
    This module implements some utility functions for
    handling the accidental dignities of an Astrology
    Chart.
  
"""

from . import essential
from flatlib import angle
from flatlib import const
from flatlib import props
from flatlib import aspects
from flatlib.tools.chartdynamics import ChartDynamics


# Relations with Sun
COMBUST = 'Combust'
CAZIMI = 'Cazimi'
UNDER_SUN = 'Under the Sun'

# Light
LIGHT_AUGMENTING = 'Augmenting Light'
LIGHT_DIMINISHING = 'Diminishing Light'

# Orientality
ORIENTAL = 'Oriental'
OCCIDENTAL = 'Occidental'

# Haiz
HAIZ = 'Haiz'
CHAIZ = 'Contra-Haiz'


# === Base functions === #

def sunRelation(obj, sun):
    """ Returns an object's relation with the sun. """
    if obj.id == const.SUN:
        return None
    dist = abs(angle.closestdistance(sun.lon, obj.lon))
    if dist < 0.2833: return CAZIMI
    elif dist < 8.0: return COMBUST
    elif dist < 16.0: return UNDER_SUN
    else:
        return None
    
def light(obj, sun):
    """ Returns if an object is augmenting or diminishing light. """
    dist = angle.distance(sun.lon, obj.lon)
    faster = sun if sun.lonspeed > obj.lonspeed else obj
    if faster == sun:
        return LIGHT_DIMINISHING if dist < 180 else LIGHT_AUGMENTING
    else:
        return LIGHT_AUGMENTING if dist < 180 else LIGHT_DIMINISHING
    
def orientality(obj, sun):
    """ Returns if an object is oriental or 
    occidental to the sun. 
    
    """
    dist = angle.distance(sun.lon, obj.lon)
    return OCCIDENTAL if dist < 180 else ORIENTAL

def viaCombusta(obj):
    """ Returns if an object is in the Via Combusta. """
    return 195 < obj.lon < 225

def haiz(obj, chart):
    """ Returns if an object is in Haiz. """
    objGender = obj.gender()
    objFaction = obj.faction()
    
    if obj.id == const.MERCURY:
        # Gender and faction of mercury depends on orientality
        sun = chart.getObject(const.SUN)
        orientalityM = orientality(obj, sun)
        if orientalityM == ORIENTAL:
            objGender = const.MASCULINE
            objFaction = const.DIURNAL
        else:
            objGender = const.FEMININE
            objFaction = const.NOCTURNAL
            
    # Object gender match sign gender?
    signGender = props.sign.gender[obj.sign]
    genderConformity = (objGender == signGender)
    
    # Match faction
    factionConformity = False
    diurnalChart = chart.isDiurnal()
    
    if obj.id == const.SUN and not diurnalChart:
        # Sun is in conformity only when above horizon
        factionConformity = False
    else:
        # Get list of houses in the chart's diurnal faction
        if diurnalChart:
            diurnalFaction = props.house.aboveHorizon
            nocturnalFaction = props.house.belowHorizon
        else:
            diurnalFaction = props.house.belowHorizon
            nocturnalFaction = props.house.aboveHorizon
        
        # Get the object's house and match factions
        objHouse = chart.houses.getObjectHouse(obj)
        if (objFaction == const.DIURNAL and objHouse.id in diurnalFaction or
            objFaction == const.NOCTURNAL and objHouse.id in nocturnalFaction):
                factionConformity = True
        
    # Match things
    if (genderConformity and factionConformity): return HAIZ
    elif (not genderConformity and not factionConformity): return CHAIZ
    else:
        return None