"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module implements the Temperament Traditional 
    Protocol.

    The Temperament protocol returns the temperament 
    scores given the characteristics of the objects 
    and other things which affects the Asc, the Moon 
    and the Sun Season.
    
"""

from flatlib import const, dignities
from flatlib import aspects
from flatlib import props
from flatlib.dignities import essential


# Temperament factors
ASC_SIGN = 'Asc Sign'
ASC_RULER = 'Asc Ruler'
ASC_RULER_SIGN = 'Asc Ruler Sign'
HOUSE1_PLANETS_IN = 'Planets in House1'
ASC_PLANETS_CONJ = 'Planets conj Asc'
ASC_PLANETS_ASP = 'Planets asp Asc'
MOON_SIGN = 'Moon Sign'
MOON_PHASE = 'Moon Phase'
MOON_DISPOSITOR_SIGN = 'Moon Dispositor Sign'
MOON_PLANETS_CONJ = 'Planets conj Moon'
MOON_PLANETS_ASP = 'Planets asp Moon'
SUN_SEASON = 'Sun season'

# Modifier factors
MOD_ASC = 'Asc'
MOD_ASC_RULER = 'Asc Ruler'
MOD_MOON = 'Moon'


# === Computation of factors === #

def singleFactor(factors, chart, factor, obj, aspect=None):
    """" Single factor for the table. """
    
    objID = obj if type(obj) == str else obj.id
    res = {
        'factor': factor,
        'objID': objID,
        'aspect': aspect
    }
    
    # For signs (obj as string) return sign element
    if type(obj) == str:
        res['element'] = props.sign.element[obj]
        
    # For Sun return sign and sunseason element
    elif objID == const.SUN:
        sunseason = props.sign.sunseason[obj.sign]
        res['sign'] = obj.sign
        res['sunseason'] = sunseason
        res['element'] = props.base.sunseasonElement[sunseason]
        
    # For Moon return phase and phase element
    elif objID == const.MOON:
        phase = chart.getMoonPhase()
        res['phase'] = phase
        res['element'] = props.base.moonphaseElement[phase]
        
    # For regular planets return element or sign/sign element
    # if there's an aspect involved
    elif objID in const.LIST_SEVEN_PLANETS:
        if aspect:
            res['sign'] = obj.sign
            res['element'] = props.sign.element[obj.sign]
        else:
            res['element'] = obj.element()
            
    try:
        # If there's element, insert into list
        res['element']
        factors.append(res)
    except KeyError:
        pass
    
    return res
    

def modifierFactor(chart, factor, factorObj, otherObj, aspList):
    """ Computes a factor for a modifier. """
    
    asp = aspects.aspectType(factorObj, otherObj, aspList)
    if asp != const.NO_ASPECT:
        return {
            'factor': factor,
            'aspect': asp,
            'objID': otherObj.id,
            'element': otherObj.element()
        }
    return None


# === Temperament factors and modifiers === #

def getFactors(chart):
    """ Returns the factors for the temperament. """
    
    factors = []
    
    # Asc sign
    asc = chart.getAngle(const.ASC)
    singleFactor(factors, chart, ASC_SIGN, asc.sign)
    
    # Asc ruler
    ascRulerID = essential.ruler(asc.sign)
    ascRuler = chart.getObject(ascRulerID)
    singleFactor(factors, chart, ASC_RULER, ascRuler)
    singleFactor(factors, chart, ASC_RULER_SIGN, ascRuler.sign)
    
    # Planets in House 1
    house1 = chart.getHouse(const.HOUSE1)
    planetsHouse1 = chart.objects.getObjectsInHouse(house1)
    for obj in planetsHouse1:
        singleFactor(factors, chart, HOUSE1_PLANETS_IN, obj)
        
    # Planets conjunct Asc
    planetsConjAsc = chart.objects.getObjectsAspecting(asc, [0])
    for obj in planetsConjAsc:
        # Ignore planets already in house 1
        if obj not in planetsHouse1:
            singleFactor(factors, chart, ASC_PLANETS_CONJ, obj)
            
    # Planets aspecting Asc cusp
    aspList = [60, 90, 120, 180]
    planetsAspAsc = chart.objects.getObjectsAspecting(asc, aspList)
    for obj in planetsAspAsc:
        aspect = aspects.aspectType(obj, asc, aspList)
        singleFactor(factors, chart, ASC_PLANETS_ASP, obj, aspect)
    
    # Moon sign and phase
    moon = chart.getObject(const.MOON)
    singleFactor(factors, chart, MOON_SIGN, moon.sign)
    singleFactor(factors, chart, MOON_PHASE, moon)
    
    # Moon dispositor
    moonRulerID = essential.ruler(moon.sign)
    moonRuler = chart.getObject(moonRulerID)
    moonFactor = singleFactor(factors, chart, MOON_DISPOSITOR_SIGN, moonRuler.sign)
    moonFactor['planetID'] = moonRulerID  # Append moon dispositor ID
    
    # Planets conjunct Moon
    planetsConjMoon = chart.objects.getObjectsAspecting(moon, [0])
    for obj in planetsConjMoon:
        singleFactor(factors, chart, MOON_PLANETS_CONJ, obj)
            
    # Planets aspecting Moon
    aspList = [60, 90, 120, 180]
    planetsAspMoon = chart.objects.getObjectsAspecting(moon, aspList)
    for obj in planetsAspMoon:
        aspect = aspects.aspectType(obj, moon, aspList)
        singleFactor(factors, chart, MOON_PLANETS_ASP, obj, aspect)
    
    # Sun season
    sun = chart.getObject(const.SUN)
    singleFactor(factors, chart, SUN_SEASON, sun)
    
    return factors


def getModifiers(chart):
    """ Returns the factors of the temperament modifiers. """
    
    modifiers = []
    
    # Factors which can be affected
    asc = chart.getAngle(const.ASC)
    ascRulerID = essential.ruler(asc.sign)
    ascRuler = chart.getObject(ascRulerID)
    moon = chart.getObject(const.MOON)
    factors = [
        [MOD_ASC, asc],
        [MOD_ASC_RULER, ascRuler],
        [MOD_MOON, moon]
    ]
    
    # Factors of affliction
    mars = chart.getObject(const.MARS)
    saturn = chart.getObject(const.SATURN)
    sun = chart.getObject(const.SUN)
    affect = [
        [mars, [0, 90, 180]],
        [saturn, [0, 90, 180]],
        [sun, [0]]     
    ]
    
    # Do calculations of afflictions
    for affectingObj, affectingAsps in affect:
        for factor, affectedObj in factors:
            modf = modifierFactor(chart, 
                                  factor, 
                                  affectedObj, 
                                  affectingObj, 
                                  affectingAsps)
            if modf:
                modifiers.append(modf)
    
    return modifiers


def scores(factors):
    """ Computes the score of temperaments
    and elements.
    
    """
    temperaments = {
        const.CHOLERIC: 0,
        const.MELANCHOLIC: 0,
        const.SANGUINE: 0,
        const.PHLEGMATIC: 0                
    }
    
    qualities = {
        const.HOT: 0,
        const.COLD: 0,
        const.DRY: 0,
        const.HUMID: 0
    }
    
    for factor in factors:
        element = factor['element']
        
        # Score temperament
        temperament = props.base.elementTemperament[element]
        temperaments[temperament] += 1
        
        # Score qualities
        tqualities = props.base.temperamentQuality[temperament]
        qualities[tqualities[0]] += 1
        qualities[tqualities[1]] += 1
        
    return {
        'temperaments': temperaments,
        'qualities': qualities
    }
    

# --------------------- #
#   Temperament Class   #
# --------------------- #

class Temperament:
    """ This class represents the calculation
    of the temperament of a chart.
    
    """
    
    def __init__(self, chart):
        self.chart = chart
        
    def getFactors(self):
        """ Returns the list of temperament factors. """
        return getFactors(self.chart)
    
    def getModifiers(self):
        """ Returns the list of temperament modifiers. """
        return getModifiers(self.chart)
    
    def getScore(self):
        """ Returns the temperament and qualitiy scores. """
        return scores(self.getFactors())