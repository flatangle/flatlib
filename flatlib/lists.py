"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module provides classes for handling lists of 
    Astrology Objects, Houses and Fixed Stars.
    
    It is basically a wrapper around a native dict with 
    useful augmentations.

"""

from . import aspects



# ---------------- #
#   Generic List   #
# ---------------- #

class GenericList:
    """ This class represents a Generic List of Objects,
    Houses or Fixed Stars.
    
    Although this class internally implements a dict object
    internally, so that retrievals are faster, its public 
    interfaces are more like a list.
    
    """
    
    def __init__(self, values=[]):
        """ Builds a Generic List from a list of objects. """
        self.content = {}
        for obj in values:
            self.content[obj.id] = obj
    
    def add(self, obj):
        """ Adds an object to this list. """
        self.content[obj.id] = obj
        
    def get(self, ID):
        """ Retrieves an object from this list. """
        return self.content[ID]
    
    def copy(self):
        """ Returns a deep copy of this list. """
        values = [obj.copy() for obj in self]
        return GenericList(values)
    
    def __iter__(self):
        """ Returns an iterator to this list. """
        return self.content.values().__iter__()


# ---------------- #
#    Object List   #
# ---------------- #

class ObjectList(GenericList):
    """ Implements a list of astrology objects. """
    
    def getObjectsInHouse(self, house):
        """ Returns a list with all objects in a house. """
        res = [obj for obj in self if house.hasObject(obj)]
        return ObjectList(res)
    
    def getObjectsAspecting(self, point, aspList):
        """ Returns a list of objects aspecting a point 
        considering a list of possible aspects.
        
        """
        res = []
        for obj in self:
            if obj.isPlanet() and aspects.isAspecting(obj, point, aspList):
                res.append(obj)
        return ObjectList(res)


# ---------------- #
#    House List    #
# ---------------- #

class HouseList(GenericList):
    """ Implements a list of houses. """
    
    def getHouseByLon(self, lon):
        """ Returns a house given a longitude. """
        for house in self:
            if house.inHouse(lon):
                return house
        return None
    
    def getObjectHouse(self, obj):
        """ Returns the house where an object is located. """
        return self.getHouseByLon(obj.lon)


# ----------------- #
#  Fixed star List  #
# ----------------- #

class FixedStarList(GenericList):
    """ Implements a list of fixed stars. """
    
    pass