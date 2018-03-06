"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module implements a class to represent an 
    astrology Chart. It provides methods to handle
    the chart, as well as three relevant properties:
    
    - objects: a list with the chart's objects
    - houses: a list with the chart's houses
    - angles: a list with the chart's angles

    Since houses 1 and 10 may not match the Asc and
    MC in some house systems, the Chart class 
    includes the list of angles. The angles should be
    used when you want to deal with angle's longitudes.
    
    There are also methods to access fixed stars.
    
"""

from . import angle
from . import const
from . import utils
from .ephem import ephem
from .datetime import Datetime


# ------------------ #
#    Chart Class     #
# ------------------ #

class Chart:
    """ This class represents an astrology chart. """
    
    def __init__(self, date, pos, **kwargs):
        """ Creates an astrology chart for a given
        date and location. 
        
        Optional arguments are:
        - hsys: house system
        - IDs: list of objects to include
        
        """
        # Handle optional arguments
        hsys = kwargs.get('hsys', const.HOUSES_DEFAULT)
        IDs = kwargs.get('IDs', const.LIST_OBJECTS_TRADITIONAL)
        
        self.date = date
        self.pos = pos
        self.hsys = hsys
        self.objects = ephem.getObjectList(IDs, date, pos)
        self.houses, self.angles = ephem.getHouses(date, pos, hsys)
        
    def copy(self):
        """ Returns a deep copy of this chart. """
        chart = Chart.__new__(Chart)
        chart.date = self.date
        chart.pos = self.pos
        chart.hsys = self.hsys
        chart.objects = self.objects.copy()
        chart.houses = self.houses.copy()
        chart.angles = self.angles.copy()
        return chart
    
    
    # === Properties === #
    
    def getObject(self, ID):
        """ Returns an object from the chart. """
        return self.objects.get(ID)
    
    def getHouse(self, ID):
        """ Returns an house from the chart. """
        return self.houses.get(ID)
    
    def getAngle(self, ID):
        """ Returns an angle from the chart. """
        return self.angles.get(ID)
    
    def get(self, ID):
        """ Returns an object, house or angle 
        from the chart.
        
        """
        if ID.startswith('House'):
            return self.getHouse(ID)
        elif ID in const.LIST_ANGLES:
            return self.getAngle(ID)
        else:
            return self.getObject(ID)


    # === Fixed stars === #
    
    # The computation of fixed stars is inefficient,
    # so the access must be made directly to the
    # ephemeris only when needed.
        
    def getFixedStar(self, ID):
        """ Returns a fixed star from the ephemeris. """
        return ephem.getFixedStar(ID, self.date)
    
    def getFixedStars(self):
        """ Returns a list with all fixed stars. """
        IDs = const.LIST_FIXED_STARS
        return ephem.getFixedStarList(IDs, self.date)


    # === Houses and angles === #
    
    def isHouse1Asc(self):
        """ Returns true if House1 is the same as the Asc. """
        house1 = self.getHouse(const.HOUSE1)
        asc = self.getAngle(const.ASC)
        dist = angle.closestdistance(house1.lon, asc.lon)
        return abs(dist) < 0.0003  # 1 arc-second
    
    def isHouse10MC(self):
        """ Returns true if House10 is the same as the MC. """
        house10 = self.getHouse(const.HOUSE10)
        mc = self.getAngle(const.MC)
        dist = angle.closestdistance(house10.lon, mc.lon)
        return abs(dist) < 0.0003  # 1 arc-second


    # === Other properties === #
    
    def isDiurnal(self):
        """ Returns true if this chart is diurnal. """
        sun = self.getObject(const.SUN)
        mc = self.getAngle(const.MC)
        
        # Get ecliptical positions and check if the
        # sun is above the horizon.
        lat = self.pos.lat
        sunRA, sunDecl = utils.eqCoords(sun.lon, sun.lat)
        mcRA, mcDecl = utils.eqCoords(mc.lon, 0)
        return utils.isAboveHorizon(sunRA, sunDecl, mcRA, lat)
    
    def getMoonPhase(self):
        """ Returns the phase of the moon. """
        sun = self.getObject(const.SUN)
        moon = self.getObject(const.MOON)
        dist = angle.distance(sun.lon, moon.lon)
        if dist < 90:
            return const.MOON_FIRST_QUARTER
        elif dist < 180:
            return const.MOON_SECOND_QUARTER
        elif dist < 270:
            return const.MOON_THIRD_QUARTER
        else:
            return const.MOON_LAST_QUARTER
    
    
    # === Solar returns === #
    
    def solarReturn(self, year):
        """ Returns this chart's solar return for a 
        given year. 
        
        """
        sun = self.getObject(const.SUN)
        date = Datetime('{0}/01/01'.format(year),
                        '00:00',
                        self.date.utcoffset)
        srDate = ephem.nextSolarReturn(date, sun.lon)
        return Chart(srDate, self.pos, hsys=self.hsys)
