"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module provides useful for handling aspects between 
    objects in flatlib. An aspect is an angular relation 
    between a planet and another object.
  
    This module has the following base terminology:
    - Active/Passive object: The active object is the planet 
      responsible for the aspect.
    - Separation: the angular distance between the active and 
      passive object.
    - Orb: the orb distance (>0) between active and passive 
      objects.
    - Obj.orb: is the orb allowed by the aspect.
    - Type: the type of the aspect.
    - Direction/Condition/Movement/etc. are properties of an 
      aspect.
    - Movement: The objects have their movements, but the 
      aspect movement can be also exact.
  
    Major aspects must be within orb of one of the planets.
    Minor aspects only when within a max allowed orb.
  
    In parameters, objA is the active object and objP is the 
    passive object.

"""

from . import angle
from . import const


# Orb for minor and exact aspects
MAX_MINOR_ASP_ORB = 3
MAX_EXACT_ORB = 0.3


# === Private functions === #
    
def _orbList(obj1, obj2, aspList):
    """ Returns a list with the orb and angular
    distances from obj1 to obj2, considering a
    list of possible aspects. 
    
    """
    sep = angle.closestdistance(obj1.lon, obj2.lon)
    absSep = abs(sep)
    return [
        {
            'type': asp,
            'orb': abs(absSep - asp),
            'separation': sep,
        } for asp in aspList
    ]

def _aspectDict(obj1, obj2, aspList):
    """ Returns the properties of the aspect of 
    obj1 to obj2, considering a list of possible
    aspects.
    
    This function makes the following assumptions:
    - Syzygy does not start aspects but receives 
      any aspect.
    - Pars Fortuna and Moon Nodes only starts 
      conjunctions but receive any aspect.
    - All other objects can start and receive
      any aspect.
      
    Note: this function returns the aspect
    even if it is not within the orb of obj1
    (but is within the orb of obj2).
    
    """
    # Ignore aspects from same and Syzygy
    if obj1 == obj2 or obj1.id == const.SYZYGY:
        return None
    
    orbs = _orbList(obj1, obj2, aspList)
    for aspDict in orbs:
        asp = aspDict['type']
        orb = aspDict['orb']  
        
        # Check if aspect is within orb
        if asp in const.MAJOR_ASPECTS:
            # Ignore major aspects out of orb
            if obj1.orb() < orb and obj2.orb() < orb:
                continue
        else:
            # Ignore minor aspects out of max orb
            if MAX_MINOR_ASP_ORB < orb:
                continue
            
        # Only conjunctions for Pars Fortuna and Nodes
        if obj1.id in [const.PARS_FORTUNA, 
                       const.NORTH_NODE, 
                       const.SOUTH_NODE] and \
                asp != const.CONJUNCTION:
            continue
        
        # We have a valid aspect within orb
        return aspDict

    return None

def _aspectProperties(obj1, obj2, aspDict):
    """ Returns the properties of an aspect between
    obj1 and obj2, given by 'aspDict'. 
    
    This function assumes obj1 to be the active object, 
    i.e., the one responsible for starting the aspect.
    
    """
    orb = aspDict['orb']
    asp = aspDict['type']
    sep = aspDict['separation']
    
    # Properties
    prop1 = {
        'id': obj1.id,
        'inOrb': False,
        'movement': const.NO_MOVEMENT         
    }
    prop2 = {
        'id': obj2.id,
        'inOrb': False,
        'movement': const.NO_MOVEMENT         
    }
    prop = {
        'type': asp,
        'orb': orb,
        'direction': -1,
        'condition': -1,
        'active': prop1,
        'passive': prop2        
    }
    
    if asp == const.NO_ASPECT:
        return prop
    
    # Aspect within orb
    prop1['inOrb'] = orb <= obj1.orb()
    prop2['inOrb'] = orb <= obj2.orb()
    
    # Direction
    prop['direction'] = const.DEXTER if sep <= 0 else const.SINISTER
    
    # Sign conditions
    # Note: if obj1 is before obj2, orbDir will be less than zero
    orbDir = sep-asp if sep >= 0 else sep+asp
    offset = obj1.signlon + orbDir
    if 0 <= offset < 30:
        prop['condition'] = const.ASSOCIATE
    else:
        prop['condition'] = const.DISSOCIATE 
    
    # Movement of the individual objects
    if abs(orbDir) < MAX_EXACT_ORB:
        prop1['movement'] = prop2['movement'] = const.EXACT
    else:
        # Active object applies to Passive if it is before 
        # and direct, or after the Passive and Rx..
        prop1['movement'] = const.SEPARATIVE
        if (orbDir > 0 and obj1.isDirect()) or \
                (orbDir < 0 and obj1.isRetrograde()):
            prop1['movement'] = const.APPLICATIVE
        elif obj1.isStationary():
            prop1['movement'] = const.STATIONARY
        
        # The Passive applies or separates from the Active 
        # if it has a different direction..
        # Note: Non-planets have zero speed
        prop2['movement'] = const.NO_MOVEMENT
        obj2speed = obj2.lonspeed if obj2.isPlanet() else 0.0
        sameDir = obj1.lonspeed * obj2speed >= 0
        if not sameDir:
            prop2['movement'] = prop1['movement']
        
    return prop

def _getActivePassive(obj1, obj2):
    """ Returns which is the active and the passive objects. """
    speed1 = abs(obj1.lonspeed) if obj1.isPlanet() else -1.0
    speed2 = abs(obj2.lonspeed) if obj2.isPlanet() else -1.0
    if speed1 > speed2:
        return {
            'active': obj1,
            'passive': obj2
        }
    else:
        return {
            'active': obj2,
            'passive': obj1
        }


# === Public functions === #

def aspectType(obj1, obj2, aspList):
    """ Returns the aspect type between objects considering
    a list of possible aspect types.
    
    """
    ap = _getActivePassive(obj1, obj2)
    aspDict = _aspectDict(ap['active'], ap['passive'], aspList)
    return aspDict['type'] if aspDict else const.NO_ASPECT

def hasAspect(obj1, obj2, aspList):
    """ Returns if there is an aspect between objects 
    considering a list of possible aspect types.
    
    """
    aspType = aspectType(obj1, obj2, aspList)
    return aspType != const.NO_ASPECT

def isAspecting(obj1, obj2, aspList):
    """ Returns if obj1 aspects obj2 within its orb,
    considering a list of possible aspect types. 
    
    """
    aspDict = _aspectDict(obj1, obj2, aspList)
    if aspDict:
        return aspDict['orb'] < obj1.orb()
    return False

def getAspect(obj1, obj2, aspList):
    """ Returns an Aspect object for the aspect between two
    objects considering a list of possible aspect types.
    
    """
    ap = _getActivePassive(obj1, obj2)
    aspDict = _aspectDict(ap['active'], ap['passive'], aspList)
    if not aspDict:
        aspDict = {
            'type': const.NO_ASPECT,
            'orb': 0,
            'separation': 0,
        } 
    aspProp = _aspectProperties(ap['active'], ap['passive'], aspDict)
    return Aspect(aspProp)


# ---------------- #
#   Aspect Class   #
# ---------------- #

class AspectObject:
    """ Dummy class to represent the Active and
    Passive objects and to allow access to their
    properties using the dot notation.
    
    """
    
    def __init__(self, properties):
        self.__dict__.update(properties)
        

class Aspect:
    """ This class represents an aspect with all
    its properties.
    
    """
    
    def __init__(self, properties):
        self.__dict__.update(properties)
        self.active = AspectObject(self.active)
        self.passive = AspectObject(self.passive)

    def exists(self):
        """ Returns if this aspect is valid. """
        return self.type != const.NO_ASPECT
    
    def movement(self):
        """ Returns the movement of this aspect. 
        The movement is the one of the active object, except
        if the active is separating but within less than 1 
        degree.
        
        """
        mov = self.active.movement
        if self.orb < 1 and mov == const.SEPARATIVE:
            mov = const.EXACT
        return mov
    
    def mutualAspect(self):
        """ Returns if both object are within aspect orb. """
        return self.active.inOrb == self.passive.inOrb == True
    
    def mutualMovement(self):
        """ Returns if both objects are mutually applying or
        separating.
        
        """
        return self.active.movement == self.passive.movement
    
    def getRole(self, ID):
        """ Returns the role (active or passive) of an object
        in this aspect.
        
        """
        if self.active.id == ID:
            return {
                'role': 'active',
                'inOrb': self.active.inOrb,
                'movement': self.active.movement
            }
        elif self.passive.id == ID:
            return {
                'role': 'passive',
                'inOrb': self.passive.inOrb,
                'movement': self.passive.movement
            }
        return None
    
    def inOrb(self, ID):
        """ Returns if the object (given by ID) is within orb
        in the Aspect.
        
        """
        role = self.getRole(ID)
        return role['inOrb'] if role else None
    
    def __str__(self):
        return '<%s %s %s %s %s>' % (self.active.id,
                                     self.passive.id,
                                     self.type,
                                     self.active.movement,
                                     angle.toString(self.orb))