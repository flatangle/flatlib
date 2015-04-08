"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module implements the Almutem Traditional 
    Protocol. The Almutem protocol returns the Planet 
    which scores higher in some hylegic points.
    
"""

from flatlib import const
from flatlib.tools import planetarytime
from flatlib.dignities import essential


# House scores
HOUSE_SCORES = {
    const.HOUSE1: 12,
    const.HOUSE2: 6,
    const.HOUSE3: 3,
    const.HOUSE4: 9,
    const.HOUSE5: 7,
    const.HOUSE6: 1,
    const.HOUSE7: 10,
    const.HOUSE8: 4,
    const.HOUSE9: 5,
    const.HOUSE10: 11,
    const.HOUSE11: 8,
    const.HOUSE12: 2
}

# List of dignities
DIGNITY_LIST = [
    'ruler',
    'exalt',
    'dayTrip',
    'nightTrip',
    'partTrip',
    'term',
    'face'
]

# List of objects
OBJECT_LIST = const.LIST_SEVEN_PLANETS


def newRow():
    """ Returns a new Almutem table row. """
    row = {}
    for obj in OBJECT_LIST:
        row[obj] = {
            'string': '',
            'score': 0
        }
    return row

def compute(chart):
    """ Computes the Almutem table. """
    almutems = {}
    
    # Hylegic points
    hylegic = [
        chart.getObject(const.SUN),
        chart.getObject(const.MOON),
        chart.getAngle(const.ASC),
        chart.getObject(const.PARS_FORTUNA),
        chart.getObject(const.SYZYGY)
    ]
    for hyleg in hylegic:
        row = newRow()
        digInfo = essential.getInfo(hyleg.sign, hyleg.signlon)
        
        # Add the scores of each planet where hyleg has dignities
        for dignity in DIGNITY_LIST:
            objID = digInfo[dignity]
            if objID:
                score = essential.SCORES[dignity]
                row[objID]['string'] += '+%s' % score
                row[objID]['score'] += score
                
        almutems[hyleg.id] = row
        
    # House positions
    row = newRow()
    for objID in OBJECT_LIST:
        obj = chart.getObject(objID)
        house = chart.houses.getObjectHouse(obj)
        score = HOUSE_SCORES[house.id]
        row[objID]['string'] = '+%s' % score
        row[objID]['score'] = score
    almutems['Houses'] = row
    
    # Planetary time
    row = newRow()
    table = planetarytime.getHourTable(chart.date, chart.pos)
    ruler = table.currRuler()
    hourRuler = table.hourRuler()
    row[ruler] = {
        'string': '+7',
        'score': 7
    }
    row[hourRuler] = {
        'string': '+6',
        'score': 6
    }
    almutems['Rulers'] = row;
    
    # Compute scores
    scores = newRow()
    for _property, _list in almutems.items():
        for objID, values in _list.items():
            scores[objID]['string'] += values['string']
            scores[objID]['score'] += values['score']
    almutems['Score'] = scores
    
    return almutems