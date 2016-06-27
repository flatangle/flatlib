"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module implements the Primary Directions
    method.

    Default assumptions:
    - only directions with the primary motion (direct)
    - only semi-arc method
    - in-zodiaco aspects of promissors to significators
    - in-mundo directions uses latitude of both promissors and significators
    
"""

from flatlib import angle
from flatlib import utils
from flatlib import const
from flatlib.dignities import tables


# === Base functions === #

def arc(pRA, pDecl, sRA, sDecl, mcRA, lat):
    """ Returns the arc of direction between a Promissor 
    and Significator. It uses the generic proportional 
    semi-arc method.
    
    """
    pDArc, pNArc = utils.dnarcs(pDecl, lat)
    sDArc, sNArc = utils.dnarcs(sDecl, lat)
    
    # Select meridian and arcs to be used
    # Default is MC and Diurnal arcs
    mdRA = mcRA
    sArc = sDArc
    pArc = pDArc
    if not utils.isAboveHorizon(sRA, sDecl, mcRA, lat):
        # Use IC and Nocturnal arcs
        mdRA = angle.norm(mcRA + 180)
        sArc = sNArc
        pArc = pNArc
        
    # Promissor and Significator distance to meridian
    pDist = angle.closestdistance(mdRA, pRA)
    sDist = angle.closestdistance(mdRA, sRA)
    
    # Promissor should be after significator (in degrees)
    if pDist < sDist:
        pDist += 360
        
    # Meridian distances proportional to respective semi-arcs
    sPropDist = sDist / (sArc / 2.0)
    pPropDist = pDist / (pArc / 2.0)
    
    # The arc is how much of the promissor's semi-arc is
    # needed to reach the significator
    return (pPropDist - sPropDist) * (pArc / 2.0)

def getArc(prom, sig, mc, pos, zerolat):
    """ Returns the arc of direction between a promissor
    and a significator. Arguments are also the MC, the
    geoposition and zerolat to assume zero ecliptical 
    latitudes.
    
    ZeroLat true => inZodiaco, false => inMundo
    
    """
    pRA, pDecl = prom.eqCoords(zerolat)
    sRa, sDecl = sig.eqCoords(zerolat)
    mcRa, mcDecl = mc.eqCoords()
    return arc(pRA, pDecl, sRa, sDecl, mcRa, pos.lat)


# ---------------------------- #
#   Primary Directions Class   #
# ---------------------------- #

class PrimaryDirections:
    """ This class represents the Primary Directions
    for a Chart.
    
    Given the complexity of all possible combinations,
    this class encodes the objects in the following
    functions:
    
    T() - Returns a term
    A() - Returns the antiscia
    C() - Returns the contra antiscia
    D() - Returns the dexter aspect
    S() - Returns the sinister aspect
    N() - Returns the conjunction or opposition aspect
    
    """
    
    # Define common significators
    SIG_HOUSES = []
    SIG_ANGLES = [const.ASC, const.MC]
    SIG_OBJECTS = [
        const.SUN, const.MOON, const.MERCURY, 
        const.VENUS, const.MARS, const.JUPITER, 
        const.SATURN, const.PARS_FORTUNA,
        const.NORTH_NODE, const.SOUTH_NODE
    ]
    
    # Maximum arc
    MAX_ARC = 100
    
    
    def __init__(self, chart):
        self.chart = chart
        self.lat = chart.pos.lat 
        mc = self.chart.getAngle(const.MC)
        self.mcRA = mc.eqCoords()[0]
        self.terms = self._buildTerms()
        
    def _buildTerms(self):
        """ Builds a data structure indexing the terms
        longitude by sign and object.
        
        """
        termLons = tables.termLons(tables.EGYPTIAN_TERMS)
        res = {}
        for (ID, sign, lon) in termLons:
            try:
                res[sign][ID] = lon
            except KeyError:
                res[sign] = {}
                res[sign][ID] = lon
        return res
    
    
    # === Object creation methods === #
    
    def G(self, ID, lat, lon):
        """ Creates a generic entry for an object. """
        
        # Equatorial coordinates
        eqM = utils.eqCoords(lon, lat)
        eqZ = eqM
        if lat != 0:
            eqZ = utils.eqCoords(lon, 0)
        
        return {
            'id': ID,
            'lat': lat,
            'lon': lon,
            'ra': eqM[0],
            'decl': eqM[1],
            'raZ': eqZ[0],
            'declZ': eqZ[1],
        }
    
    def T(self, ID, sign):
        """ Returns the term of an object in a sign. """
        lon = self.terms[sign][ID]
        ID = 'T_%s_%s' % (ID, sign)
        return self.G(ID, 0, lon)
        
    def A(self, ID):
        """ Returns the Antiscia of an object. """
        obj = self.chart.getObject(ID).antiscia()
        ID = 'A_%s' % (ID)
        return self.G(ID, obj.lat, obj.lon)
        
    def C(self, ID):
        """ Returns the CAntiscia of an object. """
        obj = self.chart.getObject(ID).cantiscia()
        ID = 'C_%s' % (ID)
        return self.G(ID, obj.lat, obj.lon)
        
    def D(self, ID, asp):
        """ Returns the dexter aspect of an object. """
        obj = self.chart.getObject(ID).copy()
        obj.relocate(obj.lon - asp)
        ID = 'D_%s_%s' % (ID, asp)
        return self.G(ID, obj.lat, obj.lon)
        
    def S(self, ID, asp):
        """ Returns the sinister aspect of an object. """
        obj = self.chart.getObject(ID).copy()
        obj.relocate(obj.lon + asp)
        ID = 'S_%s_%s' % (ID, asp)
        return self.G(ID, obj.lat, obj.lon)
        
    def N(self, ID, asp=0):
        """ Returns the conjunction or opposition aspect 
        of an object. 
        
        """
        obj = self.chart.get(ID).copy()
        obj.relocate(obj.lon + asp)
        ID = 'N_%s_%s' % (ID, asp)
        return self.G(ID, obj.lat, obj.lon)


    # === Arcs === #
    
    def _arc(self, prom, sig):
        """ Computes the in-zodiaco and in-mundo arcs 
        between a promissor and a significator.
        
        """
        arcm = arc(prom['ra'], prom['decl'], 
                   sig['ra'], sig['decl'], 
                   self.mcRA, self.lat)
        arcz = arc(prom['raZ'], prom['declZ'], 
                   sig['raZ'], sig['declZ'], 
                   self.mcRA, self.lat)
        return {
            'arcm': arcm,
            'arcz': arcz
        }
    
    def getArc(self, prom, sig):
        """ Returns the arcs between a promissor and
        a significator. Should uses the object creation 
        functions to build the objects.
        
        """
        res = self._arc(prom, sig)
        res.update({
            'prom': prom['id'],
            'sig': sig['id']
        })
        return res


    # === Lists === #
    
    def _elements(self, IDs, func, aspList):
        """ Returns the IDs as objects considering the
        aspList and the function.
        
        """
        res = []
        for asp in aspList:
            if (asp in [0, 180]):
                # Generate func for conjunctions and oppositions
                if func == self.N:
                    res.extend([func(ID, asp) for ID in IDs])
                else:
                    res.extend([func(ID) for ID in IDs])
            else:
                # Generate Dexter and Sinister for others
                res.extend([self.D(ID, asp) for ID in IDs])
                res.extend([self.S(ID, asp) for ID in IDs])
        return res
    
    def _terms(self):
        """ Returns a list with the objects as terms. """
        res = []
        for sign, terms in self.terms.items():
            for ID, lon in terms.items():
                res.append(self.T(ID, sign))
        return res
    
    def getList(self, aspList):
        """ Returns a sorted list with all
        primary directions. 
        
        """
        # Significators
        objects = self._elements(self.SIG_OBJECTS, self.N, [0])
        houses = self._elements(self.SIG_HOUSES, self.N, [0])
        angles = self._elements(self.SIG_ANGLES, self.N, [0])
        significators = objects + houses + angles
        
        # Promissors
        objects = self._elements(self.SIG_OBJECTS, self.N, aspList)
        terms = self._terms()
        antiscias = self._elements(self.SIG_OBJECTS, self.A, [0])
        cantiscias = self._elements(self.SIG_OBJECTS, self.C, [0])
        promissors = objects + terms + antiscias + cantiscias

        # Compute all
        res = []
        for prom in promissors:
            for sig in significators:
                if (prom['id'] == sig['id']):
                    continue
                arcs = self._arc(prom, sig)
                for (x,y) in [('arcm', 'M'), ('arcz', 'Z')]:
                    arc = arcs[x]
                    if 0 < arc < self.MAX_ARC:
                        res.append([
                            arcs[x],
                            prom['id'],
                            sig['id'],
                            y,
                        ])

        return sorted(res)


# ------------------ #
#   PD Table Class   #
# ------------------ #

class PDTable:
    """ Represents the Primary Directions table
    for a chart.

    """

    def __init__(self, chart, aspList=const.MAJOR_ASPECTS):
        pd = PrimaryDirections(chart)
        self.table = pd.getList(aspList)

    def view(self, arcmin, arcmax):
        """ Returns the directions within the
        min and max arcs.

        """
        res = []
        for direction in self.table:
            if arcmin < direction[0] < arcmax:
                res.append(direction)
        return res

    def bySignificator(self, ID):
        """ Returns all directions to a significator. """
        res = []
        for direction in self.table:
            if ID in direction[2]:
                res.append(direction)
        return res

    def byPromissor(self, ID):
        """ Returns all directions to a promissor. """
        res = []
        for direction in self.table:
            if ID in direction[1]:
                res.append(direction)
        return res
