"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)


    This module provides useful functions for handling
    essential dignities. It provides easy access to an
    essential dignity table, functions for retrieving
    information from the table and to compute scores and
    almutems.

"""

from . import tables
from flatlib import const


# Face variants
CHALDEAN_FACES = 'Chaldean Faces'
TRIPLICITY_FACES = 'Triplicity Faces'

# Term variants
EGYPTIAN_TERMS = 'Egyptian Terms'
TETRABIBLOS_TERMS = 'Tetrabiblos Terms'
LILLY_TERMS = 'Lilly Terms'

# Defaults
FACES = tables.CHALDEAN_FACES
TERMS = tables.EGYPTIAN_TERMS
TABLE = tables.ESSENTIAL_DIGNITIES


def setFaces(variant):
    """
    Sets the default faces variant

    """
    global FACES
    if variant == CHALDEAN_FACES:
        FACES = tables.CHALDEAN_FACES
    else:
        FACES = tables.TRIPLICITY_FACES


def setTerms(variant):
    """
    Sets the default terms of the Dignities
    table.

    """
    global TERMS
    if variant == EGYPTIAN_TERMS:
        TERMS = tables.EGYPTIAN_TERMS
    elif variant == TETRABIBLOS_TERMS:
        TERMS = tables.TETRABIBLOS_TERMS
    elif variant == LILLY_TERMS:
        TERMS = tables.LILLY_TERMS


# === Table properties === #

def ruler(sign):
    """ Returns the ruler of the sign. """
    return TABLE[sign]['ruler']

def exalt(sign):
    """ Returns the exaltation. """
    return TABLE[sign]['exalt'][0]

def exaltDeg(sign):
    """ Returns the exaltation degree. """
    return TABLE[sign]['exalt'][1]

def dayTrip(sign):
    """ Returns the diurnal triplicity. """
    return TABLE[sign]['trip'][0]

def nightTrip(sign):
    """ Returns the nocturnal triplicity. """
    return TABLE[sign]['trip'][1]

def partTrip(sign):
    """ Returns the participant triplicity. """
    return TABLE[sign]['trip'][2]

def exile(sign):
    """ Returns the exile. """
    return TABLE[sign]['exile']

def fall(sign):
    """ Returns the fall. """
    return TABLE[sign]['fall'][0]

def fallDeg(sign):
    """ Returns the fall degree. """
    return TABLE[sign]['fall'][1]

def term(sign, lon):
    """ Returns the term for a sign and longitude. """
    terms = TERMS[sign]
    for (ID, a, b) in terms:
        if (a <= lon < b):
            return ID
    return None

def face(sign, lon):
    """ Returns the face for a sign and longitude. """
    faces = FACES[sign]
    if lon < 10:
        return faces[0]
    elif lon < 20:
        return faces[1]
    else:
        return faces[2]


# === Complex properties === #

def getInfo(sign, lon):
    """ Returns the complete essential dignities
    for a sign and longitude.

    """
    return {
        'ruler': ruler(sign),
        'exalt': exalt(sign),
        'dayTrip': dayTrip(sign),
        'nightTrip': nightTrip(sign),
        'partTrip': partTrip(sign),
        'term': term(sign, lon),
        'face': face(sign, lon),
        'exile': exile(sign),
        'fall': fall(sign)
    }

def isPeregrine(ID, sign, lon):
    """ Returns if an object is peregrine
    on a sign and longitude.

    """
    info = getInfo(sign, lon)
    for dign, objID in info.items():
        if dign not in ['exile', 'fall'] and ID == objID:
            return False
    return True


# === Scores === #

SCORES = {
    'ruler': 5,
    'exalt': 4,
    'dayTrip': 3,
    'nightTrip': 3,
    'partTrip': 3,
    'term': 2,
    'face': 1,
    'fall': -4,
    'exile': -5,
}

def score(ID, sign, lon):
    """ Returns the score of an object on
    a sign and longitude.

    """
    info = getInfo(sign, lon)
    dignities = [dign for (dign, objID) in info.items() if objID == ID]
    return sum([SCORES[dign] for dign in dignities])

def almutem(sign, lon):
    """ Returns the almutem for a given
    sign and longitude.

    """
    planets = const.LIST_SEVEN_PLANETS
    res = [None, 0]
    for ID in planets:
        sc = score(ID, sign, lon)
        if sc > res[1]:
            res = [ID, sc]
    return res[0]


# ----------------------- #
#   EssentialInfo Class   #
# ----------------------- #

class EssentialInfo:
    """ This class represents the Essential dignities
    information for a given object.

    """

    def __init__(self, obj):
        self.obj = obj
        # Include info in instance properties
        info = getInfo(obj.sign, obj.signlon)
        self.__dict__.update(info)
        # Add score and almutem
        self.score = score(obj.id, obj.sign, obj.signlon)
        self.almutem = almutem(obj.sign, obj.signlon)

    def getInfo(self):
        """ Returns the essential dignities for this object. """
        return getInfo(self.obj.sign, self.obj.signlon)

    def getDignities(self):
        """ Returns the dignities belonging to this object. """
        info = self.getInfo()
        dignities = [dign for (dign, objID) in info.items()
                        if objID == self.obj.id]
        return dignities

    def isPeregrine(self):
        """ Returns if this object is peregrine. """
        return isPeregrine(self.obj.id,
                           self.obj.sign,
                           self.obj.signlon)
