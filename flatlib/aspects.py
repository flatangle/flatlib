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
    - Movement: The objects have their movements, but the aspect 
        movement can be also exact.
  
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

def _getActivePassive(obj1, obj2):
    """ Returns the active and passive objects. """
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
    
def _orbList(objA, objP, aspList):
    """ Returns orb separations by aspect type in 'aspList'. """
    sep = angle.closestdistance(objA.lon, objP.lon)
    absSep = abs(sep)
    return [
        {
            'type': asp,
            'orb': abs(absSep - asp),
            'separation': sep,
        } for asp in aspList
    ]

def _getAspectDict(objA, objP, aspList):
    """ Returns the correct aspect considering a list of 
    possible aspect types. 
    
    """
    if objA == objP:
        return None
    
    orbs = _orbList(objA, objP, aspList)
    for aspDict in orbs:
        asp = aspDict['type']
        orb = aspDict['orb']
        
        # Syzygy and Pars Fortuna should never be the 
        # active object
        if objA.id in [const.SYZYGY, const.PARS_FORTUNA]:
            return None
        
        # Nodes only do aspects by conjunction
        if objA.id in [const.NORTH_NODE, const.SOUTH_NODE]:
            if asp != const.CONJUNCTION:
                return None
        
        # For the other objects
        if asp in const.MAJOR_ASPECTS:
            # Major aspects within orb
            if orb <= objA.orb() or orb <= objP.orb():
                return aspDict
        else:
            # Minor aspects within max orb
            if orb < MAX_MINOR_ASP_ORB:
                return aspDict

    return None

def _getAspectProperties(objA, objP, aspDict):
    """ Returns some properties of an aspect given the
    active and passive objects and the aspect dict. 
    
    """
    orb = aspDict['orb']
    asp = aspDict['type']
    sep = aspDict['separation']
    
    # Builds properties for the objects
    propA = {
        'id': objA.id,
        'inOrb': False,
        'movement': const.NO_MOVEMENT         
    }
    propP = {
        'id': objP.id,
        'inOrb': False,
        'movement': const.NO_MOVEMENT         
    }
    prop = {
        'type': asp,
        'orb': orb,
        'direction': -1,
        'condition': -1,
        'active': propA,
        'passive': propP        
    }
    
    if asp == const.NO_ASPECT:
        return prop
    
    # Mutual aspects (in orb for both)
    propA['inOrb'] = orb <= objA.orb()
    propP['inOrb'] = orb <= objP.orb()
    
    # Direction of aspect
    prop['direction'] = const.DEXTER if sep <= 0 else const.SINISTER
    
    # Conditions with signs
    # If objA is before objP, orbDir is less than zero
    orbDir = sep-asp if sep >= 0 else sep+asp
    offset = objA.signlon + orbDir
    if 0 <= offset < 30:
        prop['condition'] = const.ASSOCIATE
    else:
        prop['condition'] = const.DISSOCIATE 
    
    # Movement of the individual objects
    if abs(orbDir) < MAX_EXACT_ORB:
        propA['movement'] = propP['movement'] = const.EXACT
    else:
        # Active object applies to Passive if is before and
        # direct, or after and Rx
        propA['movement'] = const.SEPARATIVE
        if (orbDir > 0 and objA.isDirect()) or \
                (orbDir < 0 and objA.isRetrograde()):
            propA['movement'] = const.APPLICATIVE
        elif objA.isStationary():
            propA['movement'] = const.STATIONARY
        
        # The Passive applies or separates from the Active 
        # if it has a different direction
        propP['movement'] = const.NO_MOVEMENT
        objPspeed = objP.lonspeed if objP.isPlanet() else 0.0
        sameDir = objA.lonspeed * objPspeed >= 0
        if not sameDir:
            propP['movement'] = propA['movement']
        
    return prop


# === Public functions === #

def aspectType(obj1, obj2, aspList):
    """ Returns the aspect type between objects if the 
    aspect is in 'aspList'.
    
    """
    ap = _getActivePassive(obj1, obj2)
    aspDict = _getAspectDict(ap['active'], ap['passive'], aspList)
    return aspDict['type'] if aspDict else const.NO_ASPECT

def hasAspect(obj1, obj2, aspList):
    """ Returns if there is an aspect between objects 
    considering a list of aspect types.
    
    """
    aspType = aspectType(obj1, obj2, aspList)
    return aspType != const.NO_ASPECT

def isAspecting(obj1, obj2, aspList):
    """ Returns if obj1 aspects obj2 within its orb. """
    if obj1 == obj2:
        return False
    
    orbs = _orbList(obj1, obj2, aspList)
    for aspDict in orbs:
        asp = aspDict['type']
        orb = aspDict['orb']
        
        # Ignore aspects from Syzygy
        if obj1.id == const.SYZYGY:
            return False
        
        # Only conjunctions for Pars Fortuna and Nodes
        if obj1.id in [const.PARS_FORTUNA,
                       const.NORTH_NODE,
                       const.SOUTH_NODE] and \
                    asp != const.CONJUNCTION:
            return False
        
        # For the other objects
        maxOrb = MAX_MINOR_ASP_ORB
        print(asp)
        if asp in const.MAJOR_ASPECTS:
            maxOrb = obj1.orb()
        return orb < maxOrb

    return False

def getAspect(obj1, obj2, aspList):
    """ Returns an Aspect object for the aspect between
    two objects considering aspect types in 'aspList'.
    
    """
    ap = _getActivePassive(obj1, obj2)
    aspDict = _getAspectDict(ap['active'], ap['passive'], aspList)
    if not aspDict:
        aspDict = {
            'type': const.NO_ASPECT,
            'orb': 0,
            'separation': 0,
        } 
    aspProp = _getAspectProperties(ap['active'], ap['passive'], aspDict)
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