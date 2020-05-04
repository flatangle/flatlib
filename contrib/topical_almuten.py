from flatlib import const
from flatlib.tools import planetarytime
from flatlib.dignities import essential
from flatlib.tools import arabicparts

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
    
# Computes the topical almuten (TA) table.
def computeTA(chart, TA):

    almutems = {}


    # SECOND HOUSE, 
    # source: Omar of Tiberias - Three Books on Nativities, p. 57; Persian Nativities II, p. 52
    if TA == "TA_2H":
        TA_LIST = [
            chart.getHouse(const.HOUSE2)
            ]
        TA_LIST.extend(
            [v for k, v in chart.objects.getObjectsInHouse(chart.getHouse(const.HOUSE2)).content.items()])
        TA_LIST.extend(
            [chart.getObject(essential.ruler(chart.getHouse(const.HOUSE2).sign)),
             arabicparts.getPart(arabicparts.PARS_SUBSTANCE, chart),
             chart.getObject(essential.ruler(arabicparts.getPart(arabicparts.PARS_SUBSTANCE, chart).sign)),
             chart.getObject(const.JUPITER),
             chart.getObject(const.PARS_FORTUNA),
             chart.getObject(essential.ruler(chart.getObject(const.PARS_FORTUNA).sign))
            ])

    # THIRD HOUSE, 
    # source: Omar of Tiberias - Three Books on Nativities, p. 58-59; Persian Nativities II, p. 53
    if TA == "TA_3H":
        TA_LIST = [
            chart.getHouse(const.HOUSE3)
            ]
        TA_LIST.extend(
            [v for k, v in chart.objects.getObjectsInHouse(chart.getHouse(const.HOUSE3)).content.items()])
        TA_LIST.extend(
            [chart.getObject(essential.ruler(chart.getHouse(const.HOUSE3).sign)),
             arabicparts.getPart(arabicparts.PARS_BROTHERS, chart),
             chart.getObject(essential.ruler(arabicparts.getPart(arabicparts.PARS_BROTHERS, chart).sign)),
             chart.getObject(const.MARS),
             chart.getObject(essential.dayTrip(chart.getObject(const.MARS).sign)),
             chart.getObject(essential.nightTrip(chart.getObject(const.MARS).sign)),
             chart.getObject(essential.partTrip(chart.getObject(const.MARS).sign))
            ])

    # And many more...

    for hyleg in TA_LIST:
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

    # Compute scores
    scores = newRow()
    for _property, _list in almutems.items():
        for objID, values in _list.items():
            scores[objID]['string'] += values['string']
            scores[objID]['score'] += values['score']
    almutems['Score'] = scores

    return almutems
