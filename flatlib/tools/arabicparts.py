"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    
    This module provides useful functions for computing 
    Arabic Parts.
  
"""

from flatlib import const
from flatlib.object import GenericObject
from flatlib.dignities import essential


# Define arabic parts
PARS_FORTUNA = const.PARS_FORTUNA
PARS_SPIRIT = 'Pars Spirit'
PARS_FAITH = 'Pars Faith'
PARS_SUBSTANCE = 'Pars Substance'
PARS_WEDDING_MALE = 'Pars Wedding [Male]'
PARS_WEDDING_FEMALE = 'Pars Wedding [Female]'
PARS_SONS = 'Pars Sons'
PARS_FATHER = 'Pars Father'
PARS_MOTHER = 'Pars Mother'
PARS_BROTHERS = 'Pars Brothers'
PARS_DISEASES = 'Pars Diseases'
PARS_DEATH = 'Pars Death'
PARS_TRAVEL = 'Pars Travel'
PARS_FRIENDS = 'Pars Friends'
PARS_ENEMIES = 'Pars Enemies'
PARS_SATURN = 'Pars Saturn'
PARS_JUPITER = 'Pars Jupiter'
PARS_MARS = 'Pars Mars'
PARS_VENUS = 'Pars Venus'
PARS_MERCURY = 'Pars Mercury'
PARS_HORSEMANSHIP = 'Pars Horsemanship'  # aka Bravery

# Define Diurnal and Nocturnal formulas as
# "Distance of A to B projected from C".
# Note that '$R' stands for the Ruler of something
FORMULAS = {}

FORMULAS[PARS_FORTUNA] = [
    [const.SUN, const.MOON, const.ASC],  # Diurnal
    [const.MOON, const.SUN, const.ASC]   # Nocturnal
]

FORMULAS[PARS_SPIRIT] = [
    [const.MOON, const.SUN, const.ASC],
    [const.SUN, const.MOON, const.ASC]
]

FORMULAS[PARS_FAITH] = [
    [const.MOON, const.MERCURY, const.ASC],
    [const.MERCURY, const.MOON, const.ASC]
]

FORMULAS[PARS_SUBSTANCE] = [
    ['$R' + const.HOUSE2, const.HOUSE2, const.ASC],
    ['$R' + const.HOUSE2, const.HOUSE2, const.ASC]
]

FORMULAS[PARS_WEDDING_MALE] = [
    [const.SATURN, const.VENUS, const.ASC],
    [const.SATURN, const.VENUS, const.ASC]
]

FORMULAS[PARS_WEDDING_FEMALE] = [
    [const.VENUS, const.SATURN, const.ASC],
    [const.VENUS, const.SATURN, const.ASC]
]

FORMULAS[PARS_SONS] = [
    [const.JUPITER, const.SATURN, const.ASC],
    [const.SATURN, const.JUPITER, const.ASC]
]

FORMULAS[PARS_FATHER] = [
    [const.SUN, const.SATURN, const.ASC],
    [const.SATURN, const.SUN, const.ASC]
]

FORMULAS[PARS_MOTHER] = [
    [const.VENUS, const.MOON, const.ASC],
    [const.MOON, const.VENUS, const.ASC]
]

FORMULAS[PARS_BROTHERS] = [
    [const.SATURN, const.JUPITER, const.ASC],
    [const.SATURN, const.JUPITER, const.ASC]
]

FORMULAS[PARS_DISEASES] = [
    [const.SATURN, const.MARS, const.ASC],
    [const.MARS, const.SATURN, const.ASC]
]

FORMULAS[PARS_DEATH] = [
    [const.MOON, const.HOUSE8, const.SATURN],
    [const.MOON, const.HOUSE8, const.SATURN]
]

FORMULAS[PARS_TRAVEL] = [
    ['$R' + const.HOUSE9, const.HOUSE9, const.ASC],
    ['$R' + const.HOUSE9, const.HOUSE9, const.ASC]
]

FORMULAS[PARS_FRIENDS] = [
    [const.MOON, const.MERCURY, const.ASC],
    [const.MOON, const.MERCURY, const.ASC]
]

FORMULAS[PARS_ENEMIES] = [
    ['$R' + const.HOUSE12, const.HOUSE12, const.ASC],
    ['$R' + const.HOUSE12, const.HOUSE12, const.ASC]
]

FORMULAS[PARS_SATURN] = [
    [const.SATURN, const.PARS_FORTUNA, const.ASC],
    [const.PARS_FORTUNA, const.SATURN, const.ASC]
]

FORMULAS[PARS_JUPITER] = [
    [PARS_SPIRIT, const.JUPITER, const.ASC],
    [const.JUPITER, PARS_SPIRIT, const.ASC]
]

FORMULAS[PARS_MARS] = [
    [const.MARS, const.PARS_FORTUNA, const.ASC],
    [const.PARS_FORTUNA, const.MARS, const.ASC]
]

FORMULAS[PARS_VENUS] = [
    [PARS_SPIRIT, const.VENUS, const.ASC],
    [const.VENUS, PARS_SPIRIT, const.ASC]
]

FORMULAS[PARS_MERCURY] = [
    [const.MERCURY, const.PARS_FORTUNA, const.ASC],
    [const.PARS_FORTUNA, const.MERCURY, const.ASC]
]

FORMULAS[PARS_HORSEMANSHIP] = [
    [const.SATURN, const.MOON, const.ASC],
    [const.MOON, const.SATURN, const.ASC]
]

# === Functions === #

def objLon(ID, chart):
    """ Returns the longitude of an object. """
    if ID.startswith('$R'):
        # Return Ruler
        ID = ID[2:]
        obj = chart.get(ID)
        rulerID = essential.ruler(obj.sign)
        ruler = chart.getObject(rulerID)
        return ruler.lon
    elif ID.startswith('Pars'):
        # Return an arabic part
        return partLon(ID, chart)
    else:
        # Return an object
        obj = chart.get(ID)
        return obj.lon
    
def partLon(ID, chart):
    """ Returns the longitude of an arabic part. """
    # Get diurnal or nocturnal formula
    abc = FORMULAS[ID][0] if chart.isDiurnal() else FORMULAS[ID][1]
    a = objLon(abc[0], chart)
    b = objLon(abc[1], chart)
    c = objLon(abc[2], chart)
    return c + b - a

def getPart(ID, chart):
    """ Returns an Arabic Part. """
    obj = GenericObject()
    obj.id = ID
    obj.type = const.OBJ_ARABIC_PART
    obj.relocate(partLon(ID, chart))
    return obj
    