"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    
    This module defines relevant tables, such as
    the Essential Dignities.
  
"""


# ----------------------- #
#   Essential Dignities   #
# ----------------------- #

SIGN_LIST = ['Aries', 'Taurus', 'Gemini', 'Cancer',
             'Leo', 'Virgo', 'Libra', 'Scorpio',
             'Sagittarius', 'Capricorn', 'Aquarius', 
             'Pisces']


# === Face variants === #


CHALDEAN_FACES = {

    'Aries': ['Mars', 'Sun', 'Venus'],
    'Taurus': ['Mercury', 'Moon', 'Saturn'],
    'Gemini': ['Jupiter', 'Mars', 'Sun'],
    'Cancer': ['Venus', 'Mercury', 'Moon'],
    'Leo': ['Saturn', 'Jupiter', 'Mars'],
    'Virgo': ['Sun', 'Venus', 'Mercury'],
    'Libra': ['Moon', 'Saturn', 'Jupiter'],
    'Scorpio': ['Mars', 'Sun', 'Venus'],
    'Sagittarius': ['Mercury', 'Moon', 'Saturn'],
    'Capricorn': ['Jupiter', 'Mars', 'Sun'],
    'Aquarius': ['Venus', 'Mercury', 'Moon'],
    'Pisces': ['Saturn', 'Jupiter', 'Mars']
}


TRIPLICITY_FACES = {

    'Aries': ['Mars', 'Sun', 'Jupiter'],
    'Taurus': ['Venus', 'Mercury', 'Saturn'],
    'Gemini': ['Mercury', 'Venus', 'Saturn'],
    'Cancer': ['Moon', 'Mars', 'Jupiter'],
    'Leo': ['Sun', 'Jupiter', 'Mars'],
    'Virgo': ['Mercury', 'Saturn', 'Venus'],
    'Libra': ['Venus', 'Saturn', 'Mercury'],
    'Scorpio': ['Mars', 'Jupiter', 'Moon'],
    'Sagittarius': ['Jupiter', 'Mars', 'Sun'],
    'Capricorn': ['Saturn', 'Venus', 'Mercury'],
    'Aquarius': ['Saturn', 'Mercury', 'Venus'],
    'Pisces': ['Jupiter', 'Moon', 'Mars']
}


# === Term variants === #

# This table represents the Egyptian terms
EGYPTIAN_TERMS = {
    
    'Aries': [
        ['Jupiter', 0, 6],
        ['Venus', 6, 12],
        ['Mercury', 12, 20],
        ['Mars', 20, 25],
        ['Saturn', 25, 30]
    ],

    'Taurus': [
        ['Venus', 0, 8],
        ['Mercury', 8, 14],
        ['Jupiter', 14, 22],
        ['Saturn', 22, 27],
        ['Mars', 27, 30]
    ],
    
    'Gemini': [
        ['Mercury', 0, 6],
        ['Jupiter', 6, 12],
        ['Venus', 12, 17],
        ['Mars', 17, 24],
        ['Saturn', 24, 30]
    ],

    'Cancer': [
        ['Mars', 0, 7],
        ['Venus', 7, 13],
        ['Mercury', 13, 19],
        ['Jupiter', 19, 26],
        ['Saturn', 26, 30]
    ],

    'Leo': [
        ['Jupiter', 0, 6],
        ['Venus', 6, 11],
        ['Saturn', 11, 18],
        ['Mercury', 18, 24],
        ['Mars', 24, 30]
    ],

    'Virgo': [
        ['Mercury', 0, 7],
        ['Venus', 7, 17],
        ['Jupiter', 17, 21],
        ['Mars', 21, 28],
        ['Saturn', 28, 30]
    ],

    'Libra': [
        ['Saturn', 0, 6],
        ['Mercury', 6, 14],
        ['Jupiter', 14, 21],
        ['Venus', 21, 28],
        ['Mars', 28, 30]
    ],

    'Scorpio': [
        ['Mars', 0, 7],
        ['Venus', 7, 11],
        ['Mercury', 11, 19],
        ['Jupiter', 19, 24],
        ['Saturn', 24, 30]
    ],

    'Sagittarius': [
        ['Jupiter', 0, 12],
        ['Venus', 12, 17],
        ['Mercury', 17, 21],
        ['Saturn', 21, 26],
        ['Mars', 26, 30]
    ],

    'Capricorn': [
        ['Mercury', 0, 7],
        ['Jupiter', 7, 14],
        ['Venus', 14, 22],
        ['Saturn', 22, 26],
        ['Mars', 26, 30]
    ],

    'Aquarius': [
        ['Mercury', 0, 7],
        ['Venus', 7, 13],
        ['Jupiter', 13, 20],
        ['Mars', 20, 25],
        ['Saturn', 25, 30]
    ],

    'Pisces': [
        ['Venus', 0, 12],
        ['Jupiter', 12, 16],
        ['Mercury', 16, 19],
        ['Mars', 19, 28],
        ['Saturn', 28, 30]
    ]
}

# This table represents the Ptolemaic terms
# from Tetrabiblos (F.E. Robbins translation)
TETRABIBLOS_TERMS = {
    
    'Aries': [
        ['Jupiter', 0, 6],
        ['Venus', 6, 14],
        ['Mercury', 14, 21],
        ['Mars', 21, 26],
        ['Saturn', 26, 30]
    ],

    'Taurus': [
        ['Venus', 0, 8],
        ['Mercury', 8, 15],
        ['Jupiter', 15, 22],
        ['Saturn', 22, 24],
        ['Mars', 24, 30]
    ],
    
    'Gemini': [
        ['Mercury', 0, 7],
        ['Jupiter', 7, 13],
        ['Venus', 13, 20],
        ['Mars', 20, 26],
        ['Saturn', 26, 30]
    ],

    'Cancer': [
        ['Mars', 0, 6],
        ['Jupiter', 6, 13],
        ['Mercury', 13, 20],
        ['Venus', 20, 27],
        ['Saturn', 27, 30]
    ],

    'Leo': [
        ['Jupiter', 0, 6],
        ['Mercury', 6, 13],
        ['Saturn', 13, 19],
        ['Venus', 19, 25],
        ['Mars', 25, 30]
    ],

    'Virgo': [
        ['Mercury', 0, 7],
        ['Venus', 7, 13],
        ['Jupiter', 13, 18],
        ['Saturn', 18, 24],
        ['Mars', 24, 30]
    ],

    'Libra': [
        ['Saturn', 0, 6],
        ['Venus', 6, 11],
        ['Mercury', 11, 16],
        ['Jupiter', 16, 24],
        ['Mars', 24, 30]
    ],

    'Scorpio': [
        ['Mars', 0, 6],
        ['Venus', 6, 13],
        ['Jupiter', 13, 21],
        ['Mercury', 21, 27],
        ['Saturn', 27, 30]
    ],

    'Sagittarius': [
        ['Jupiter', 0, 8],
        ['Venus', 8, 14],
        ['Mercury', 14, 19],
        ['Saturn', 19, 25],
        ['Mars', 25, 30]
    ],

    'Capricorn': [
        ['Venus', 0, 6],
        ['Mercury', 6, 12],
        ['Jupiter', 12, 19],
        ['Saturn', 19, 25],
        ['Mars', 25, 30]
    ],

    'Aquarius': [
        ['Saturn', 0, 6],
        ['Mercury', 6, 12],
        ['Venus', 12, 20],
        ['Jupiter', 20, 25],
        ['Mars', 25, 30]
    ],

    'Pisces': [
        ['Venus', 0, 8],
        ['Jupiter', 8, 14],
        ['Mercury', 14, 20],
        ['Mars', 20, 25],
        ['Saturn', 25, 30]
    ]
}

# This table represents the Ptolemaic terms
# as described in Christian Astrology (W. Lilly)
LILLY_TERMS = {
    
    'Aries': [
        ['Jupiter', 0, 6],
        ['Venus', 6, 14],
        ['Mercury', 14, 21],
        ['Mars', 21, 26],
        ['Saturn', 26, 30]
    ],

    'Taurus': [
        ['Venus', 0, 8],
        ['Mercury', 8, 15],
        ['Jupiter', 15, 22],
        ['Saturn', 22, 26],
        ['Mars', 26, 30]
    ],
    
    'Gemini': [
        ['Mercury', 0, 7],
        ['Jupiter', 7, 14],
        ['Venus', 14, 21],
        ['Saturn', 21, 25],
        ['Mars', 25, 30]
    ],

    'Cancer': [
        ['Mars', 0, 6],
        ['Jupiter', 6, 13],
        ['Mercury', 13, 20],
        ['Venus', 20, 27],
        ['Saturn', 27, 30]
    ],

    'Leo': [
        ['Saturn', 0, 6],
        ['Mercury', 6, 13],
        ['Venus', 13, 19],
        ['Jupiter', 19, 25],
        ['Mars', 25, 30]
    ],

    'Virgo': [
        ['Mercury', 0, 7],
        ['Venus', 7, 13],
        ['Jupiter', 13, 18],
        ['Saturn', 18, 24],
        ['Mars', 24, 30]
    ],

    'Libra': [
        ['Saturn', 0, 6],
        ['Venus', 6, 11],
        ['Jupiter', 11, 19],
        ['Mercury', 19, 24],
        ['Mars', 24, 30]
    ],

    'Scorpio': [
        ['Mars', 0, 6],
        ['Jupiter', 6, 14],
        ['Venus', 14, 21],
        ['Mercury', 21, 27],
        ['Saturn', 27, 30]
    ],

    'Sagittarius': [
        ['Jupiter', 0, 8],
        ['Venus', 8, 14],
        ['Mercury', 14, 19],
        ['Saturn', 19, 25],
        ['Mars', 25, 30]
    ],

    'Capricorn': [
        ['Venus', 0, 6],
        ['Mercury', 6, 12],
        ['Jupiter', 12, 19],
        ['Mars', 19, 25],
        ['Saturn', 25, 30]
    ],

    'Aquarius': [
        ['Saturn', 0, 6],
        ['Mercury', 6, 12],
        ['Venus', 12, 20],
        ['Jupiter', 20, 25],
        ['Mars', 25, 30]
    ],

    'Pisces': [
        ['Venus', 0, 8],
        ['Jupiter', 8, 14],
        ['Mercury', 14, 20],
        ['Mars', 20, 25],
        ['Saturn', 25, 30]
    ]
}


# === Dignity Table === #

# This is the default essential dignities table, 
# not considering the terms.
ESSENTIAL_DIGNITIES = {

        'Aries': {
            'ruler': 'Mars',
            'exalt': ['Sun', 19],
            'trip': ['Sun', 'Jupiter', 'Saturn'],
            'faces': ['Mars', 'Sun', 'Venus'],
            'exile': 'Venus',
            'fall': ['Saturn', 21]
        },

        'Taurus': {
            'ruler': 'Venus',
            'exalt': ['Moon', 3],
            'trip': ['Venus', 'Moon', 'Mars'],
            'faces': ['Mercury', 'Moon', 'Saturn'],
            'exile': 'Mars',
            'fall': [None, 0]
        },

        'Gemini': {
            'ruler': 'Mercury',
            'exalt': [None, 0],
            'trip': ['Saturn', 'Mercury', 'Jupiter'],
            'faces': ['Jupiter', 'Mars', 'Sun'],
            'exile': 'Jupiter',
            'fall': [None, 0]
        },

        'Cancer': {
            'ruler': 'Moon',
            'exalt': ['Jupiter', 15],
            'trip': ['Venus', 'Mars', 'Moon'],
            'faces': ['Venus', 'Mercury', 'Moon'],
            'exile': 'Saturn',
            'fall': ['Mars', 28]
        },

        'Leo': {
            'ruler': 'Sun',
            'exalt': [None, 0],
            'trip': ['Sun', 'Jupiter', 'Saturn'],
            'faces': ['Saturn', 'Jupiter', 'Mars'],
            'exile': 'Saturn',
            'fall': [None, 0]
        },

        'Virgo': {
            'ruler': 'Mercury',
            'exalt': ['Mercury', 15],
            'trip': ['Venus', 'Moon', 'Mars'],
            'faces': ['Sun', 'Venus', 'Mercury'],
            'exile': 'Jupiter',
            'fall': ['Venus', 27]
        },

        'Libra': {
            'ruler': 'Venus',
            'exalt': ['Saturn', 21],
            'trip': ['Saturn', 'Mercury', 'Jupiter'],
            'faces': ['Moon', 'Saturn', 'Jupiter'],
            'exile': 'Mars',
            'fall': ['Sun', 19]
        },

        'Scorpio': {
            'ruler': 'Mars',
            'exalt': [None, 0],
            'trip': ['Venus', 'Mars', 'Moon'],
            'faces': ['Mars', 'Sun', 'Venus'],
            'exile': 'Venus',
            'fall': ['Moon', 3]
        },

        'Sagittarius': {
            'ruler': 'Jupiter',
            'exalt': [None, 0],
            'trip': ['Sun', 'Jupiter', 'Saturn'],
            'faces': ['Mercury', 'Moon', 'Saturn'],
            'exile': 'Mercury',
            'fall': [None, 0]
        },

        'Capricorn': {
            'ruler': 'Saturn',
            'exalt': ['Mars', 28],
            'trip': ['Venus', 'Moon', 'Mars'],
            'faces': ['Jupiter', 'Mars', 'Sun'],
            'exile': 'Moon',
            'fall': ['Jupiter', 15]
        },

        'Aquarius': {
            'ruler': 'Saturn',
            'exalt': [None, 0],
            'trip': ['Saturn', 'Mercury', 'Jupiter'],
            'faces': ['Venus', 'Mercury', 'Moon'],
            'exile': 'Sun',
            'fall': [None, 0]
        },

        'Pisces': {
            'ruler': 'Jupiter',
            'exalt': ['Venus', 27],
            'trip': ['Venus', 'Mars', 'Moon'],
            'faces': ['Saturn', 'Jupiter', 'Mars'],
            'exile': 'Mercury',
            'fall': ['Mercury', 15]
        }
    }


# === Functions === #

def termLons(TERMS):
    """ Returns a list with the absolute longitude 
    of all terms.
    
    """
    res = []
    for i, sign in enumerate(SIGN_LIST):
        termList = TERMS[sign]
        res.extend([
            ID,
            sign,
            start + 30 * i,
        ] for (ID, start, end) in termList)
    return res
