"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    
    This module implements some utility functions for
    handling the accidental dignities of an Astrology
    Chart.
  
"""

from copy import copy

from flatlib import angle, dignities
from flatlib import const
from flatlib import props
from flatlib import aspects
from flatlib.dignities import essential
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
    if (genderConformity and factionConformity):
        return HAIZ
    elif (not genderConformity and not factionConformity):
        return CHAIZ
    else:
        return None


# ---------------------------- #
#   Accidental Dignity Class   #
# ---------------------------- #

# House scores
HOUSE_SCORES = {
    const.HOUSE1: 5,
    const.HOUSE2: 3,
    const.HOUSE3: 1,
    const.HOUSE4: 4,
    const.HOUSE5: 3,
    const.HOUSE6: -3,
    const.HOUSE7: 4,
    const.HOUSE8: -4,
    const.HOUSE9: 2,
    const.HOUSE10: 5,
    const.HOUSE11: 4,
    const.HOUSE12: -5,
}


class AccidentalDignity:
    """ This class provides methods to access the 
    accidental dignities of an object in a Chart.
    
    """
    
    def __init__(self, obj, chart):
        self.obj = obj
        self.chart = chart
        self.dyn = ChartDynamics(chart)
        self.scoreProperties = None
    
    
    # === Houses === #
    
    def house(self):
        """ Returns the object's house. """
        house = self.chart.houses.getObjectHouse(self.obj)
        return house
    
    def houseScore(self):
        """ Returns the score of the object's house. """
        house = self.house()
        return HOUSE_SCORES[house.id]
    
    
    # === Relation with Sun === #
    
    def sunRelation(self):
        """ Returns the relation of the object with the sun. """
        sun = self.chart.getObject(const.SUN)
        return sunRelation(self.obj, sun)
    
    def isCazimi(self):
        return self.sunRelation() == CAZIMI
    
    def isUnderSun(self):
        return self.sunRelation() == UNDER_SUN
    
    def isCombust(self):
        return self.sunRelation() == COMBUST
    
    def light(self):
        """ Returns if object is augmenting or diminishing its 
        light.
        
        """
        sun = self.chart.getObject(const.SUN)
        return light(self.obj, sun)
    
    def isAugmentingLight(self):
        return self.light() == LIGHT_AUGMENTING
    
    def orientality(self):
        """ Returns the orientality of the object. """
        sun = self.chart.getObject(const.SUN)
        return orientality(self.obj, sun)
    
    def isOriental(self):
        return self.orientality() == ORIENTAL
    
    
    # === Joys === #
    
    def inHouseJoy(self):
        """ Returns if the object is in its house of joy. """
        house = self.house()
        return props.object.houseJoy[self.obj.id] == house.id
    
    def inSignJoy(self):
        """ Returns if the object is in its sign of joy. """
        return props.object.signJoy[self.obj.id] == self.obj.sign
    
    
    # === Mutual Receptions === #
    
    def reMutualReceptions(self):
        """ Returns all mutual receptions with the object
        and other planets, indexed by planet ID. 
        It only includes ruler and exaltation receptions.
        
        """
        planets = copy(const.LIST_SEVEN_PLANETS)
        planets.remove(self.obj.id)
        mrs = {}
        for ID in planets:
            mr = self.dyn.reMutualReceptions(self.obj.id, ID)
            if mr:
                mrs[ID] = mr
        return mrs
    
    def eqMutualReceptions(self):
        """ Returns a list with mutual receptions with the 
        object and other planets, when the reception is the 
        same for both (both ruler or both exaltation).
        
        It basically return a list with every ruler-ruler and 
        exalt-exalt mutual receptions
        
        """
        mrs = self.reMutualReceptions()
        res = []
        for ID, receptions in mrs.items():
            for pair in receptions:
                if pair[0] == pair[1]:
                    res.append(pair[0])
        return res
    
    
    # === Aspects to benefics and malefics === #
    
    def __aspectLists(self, IDs, aspList):
        """ Returns a list with the aspects that the object
        makes to the objects in IDs. It considers only
        conjunctions and other exact/applicative aspects
        if in aspList.
        
        """
        res = []
        
        for otherID in IDs:
            # Ignore same 
            if otherID == self.obj.id:
                continue
            
            # Get aspects to the other object
            otherObj = self.chart.getObject(otherID)
            asp = aspects.getAspect(self.obj, otherObj, aspList)
            
            if asp.type == const.NO_ASPECT:
                continue
            elif asp.type == const.CONJUNCTION:
                res.append(asp.type)
            else:
                # Only exact or applicative aspects
                movement = asp.movement()
                if movement in [const.EXACT, const.APPLICATIVE]:
                    res.append(asp.type)
        
        return res
    
    def aspectBenefics(self):
        """ Returns a list with the good aspects the object 
        makes to the benefics.
        
        """
        benefics = [const.VENUS, const.JUPITER]
        return self.__aspectLists(benefics, aspList=[0, 60, 120])
    
    def aspectMalefics(self):
        """ Returns a list with the bad aspects the object
        makes to the malefics.
        
        """
        malefics = [const.MARS, const.SATURN]
        return self.__aspectLists(malefics, aspList=[0, 90, 180])
    
    
    # == Application and Separation from benefics and malefics == #
    
    def __sepApp(self, IDs, aspList):
        """ Returns true if the object last and next movement are
        separations and applications to objects in list IDs.
        It only considers aspects in aspList.
        
        This function is static since it does not test if the next
        application will be indeed perfected. It considers only
        a snapshot of the chart and not its astronomical movement.
        
        """
        sep, app = self.dyn.immediateAspects(self.obj.id, aspList)
        if sep is None or app is None:
            return False
        else:
            sepCondition = sep['id'] in IDs
            appCondition = app['id'] in IDs
            return sepCondition == appCondition == True
    
    def isAuxilied(self):
        """ Returns if the object is separating and applying to 
        a benefic considering good aspects.
        
        """
        benefics = [const.VENUS, const.JUPITER]
        return self.__sepApp(benefics, aspList=[0, 60, 120])
        
    def isSurrounded(self):
        """ Returns if the object is separating and applying to 
        a malefic considering bad aspects.
        
        """
        malefics = [const.MARS, const.SATURN]
        return self.__sepApp(malefics, aspList=[0, 90, 180])
    
    
    # === Aspects to Moon Nodes === #
    
    def isConjNorthNode(self):
        """ Returns if object is conjunct north node. """
        node = self.chart.getObject(const.NORTH_NODE)
        return aspects.hasAspect(self.obj, node, aspList=[0])
    
    def isConjSouthNode(self):
        """ Returns if object is conjunct south node. """
        node = self.chart.getObject(const.SOUTH_NODE)
        return aspects.hasAspect(self.obj, node, aspList=[0])
    
    
    # === Void of Course, Feral and Haiz === #
    
    def isVoc(self):
        """ Return if the object is Void of Course. """
        return self.dyn.isVOC(self.obj.id)
    
    def isFeral(self):
        """ Returns true if the object does not have any 
        aspects.
        
        """
        planets = copy(const.LIST_SEVEN_PLANETS)
        planets.remove(self.obj.id)
        for otherID in planets:
            otherObj = self.chart.getObject(otherID)
            if aspects.hasAspect(self.obj, otherObj, const.MAJOR_ASPECTS):
                return False
        return True
    
    def haiz(self):
        """ Returns the object haiz. """
        return haiz(self.obj, self.chart)
    
    
    # === Scores === #
    
    def getScoreProperties(self):
        """ Returns the accidental dignity score of the object 
        as dict. 
        
        """
        obj = self.obj
        score = {}
        
        # Peregrine
        isPeregrine = essential.isPeregrine(obj.id, obj.sign, obj.signlon)
        score['peregrine'] = -5 if isPeregrine else 0
        
        # Ruler-Ruler and Exalt-Exalt mutual receptions
        mr = self.eqMutualReceptions()
        score['mr_ruler'] = +5 if 'ruler' in mr else 0
        score['mr_exalt'] = +4 if 'exalt' in mr else 0
        
        # House scores
        score['house'] = self.houseScore()
        
        # Joys
        score['joy_sign'] = +3 if self.inSignJoy() else 0
        score['joy_house'] = +2 if self.inHouseJoy() else 0
        
        # Relations with sun
        score['cazimi'] = +5 if self.isCazimi() else 0
        score['combust'] = -6 if self.isCombust() else 0
        score['under_sun'] = -4 if self.isUnderSun() else 0
        score['no_under_sun'] = 0
        if obj.id != const.SUN and not self.sunRelation():
            score['no_under_sun'] = +5
        
        # Light
        score['light'] = 0
        if obj.id != const.SUN:
            score['light'] = +1 if self.isAugmentingLight() else -1
            
        # Orientality
        score['orientality'] = 0
        if obj.id in [const.SATURN, const.JUPITER, const.MARS]:
            score['orientality'] = +2 if self.isOriental() else -2
        elif obj.id in [const.VENUS, const.MERCURY, const.MOON]:
            score['orientality'] = -2 if self.isOriental() else +2
        
        # Moon nodes
        score['north_node'] = -3 if self.isConjNorthNode() else 0
        score['south_node'] = -5 if self.isConjSouthNode() else 0
        
        # Direction and speed
        score['direction'] = 0
        if obj.id not in [const.SUN, const.MOON]:
            score['direction'] = +4 if obj.isDirect() else -5
        score['speed'] = +2 if obj.isFast() else -2
        
        # Aspects to benefics
        aspBen = self.aspectBenefics()
        score['benefic_asp0'] = +5 if const.CONJUNCTION in aspBen else 0
        score['benefic_asp120'] = +4 if const.TRINE in aspBen else 0
        score['benefic_asp60'] = +3 if const.SEXTILE in aspBen else 0
        
        # Aspects to malefics
        aspMal = self.aspectMalefics()
        score['malefic_asp0'] = -5 if const.CONJUNCTION in aspMal else 0
        score['malefic_asp180'] = -4 if const.OPPOSITION in aspMal else 0
        score['malefic_asp90'] = -3 if const.SQUARE in aspMal else 0
        
        # Auxily and Surround
        score['auxilied'] = +5 if self.isAuxilied() else 0
        score['surround'] = -5 if self.isSurrounded() else 0
        
        # Voc and Feral
        score['feral'] = -3 if self.isFeral() else 0
        score['void'] = -2 if (self.isVoc() and score['feral'] == 0) else 0
        
        # Haiz
        haiz = self.haiz()
        score['haiz'] = 0
        if haiz == HAIZ:
            score['haiz'] = +3
        elif haiz == CHAIZ:
            score['haiz'] = -2
            
        # Moon via combusta
        score['viacombusta'] = 0
        if obj.id == const.MOON and viaCombusta(obj):
            score['viacombusta'] = -2
            
        return score
    
    def getActiveProperties(self):
        """ Returns the non-zero accidental dignities. """
        score = self.getScoreProperties()
        return {key: value for (key, value) in score.items()
                if value != 0} 
    
    def score(self):
        """ Returns the sum of the accidental dignities
        score.
        
        """
        if not self.scoreProperties:
            self.scoreProperties = self.getScoreProperties()
        return sum(self.scoreProperties.values())