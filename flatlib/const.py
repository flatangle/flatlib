"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module defines the names of signs, objects, angles, 
    houses and fixed-stars used in the library.

"""


# === Base constants === */

# Four primitive qualities
HOT = 'Hot'
COLD = 'Cold'
DRY = 'Dry'
HUMID = 'Humid'

# Four Elements
FIRE = 'Fire'
EARTH = 'Earth'
AIR = 'Air'
WATER = 'Water'

# Four Temperaments
CHOLERIC = 'Choleric'
MELANCHOLIC = 'Melancholic'
SANGUINE = 'Sanguine'
PHLEGMATIC = 'Phlegmatic'

# Genders
MASCULINE = 'Masculine'
FEMININE = 'Feminine'
NEUTRAL = 'Neutral'

# Factions
DIURNAL = 'Diurnal'
NOCTURNAL = 'Nocturnal'

# Sun seasons
SPRING = 'Spring'
SUMMER = 'Summer'
AUTUMN = 'Autumn'
WINTER = 'Winter'

# Moon Quarters
MOON_FIRST_QUARTER = 'First Quarter'
MOON_SECOND_QUARTER = 'Second Quarter'
MOON_THIRD_QUARTER = 'Third Quarter'
MOON_LAST_QUARTER = 'Last Quarter'


# === Signs === */

ARIES = 'Aries'
TAURUS = 'Taurus'
GEMINI = 'Gemini'
CANCER = 'Cancer'
LEO = 'Leo'
VIRGO = 'Virgo'
LIBRA = 'Libra'
SCORPIO = 'Scorpio'
SAGITTARIUS = 'Sagittarius'
CAPRICORN = 'Capricorn'
AQUARIUS = 'Aquarius'
PISCES = 'Pisces'

# Sign modes
CARDINAL = 'Cardinal'
FIXED = 'Fixed'
MUTABLE = 'Mutable'

# Sign figures
SIGN_FIGURE_NONE = 'None'
SIGN_FIGURE_BEAST = 'Beast'
SIGN_FIGURE_HUMAN = 'Human'
SIGN_FIGURE_WILD = 'Wild'

# Sign fertilities
SIGN_FERTILE = 'Fertile'
SIGN_STERILE = 'Sterile'
SIGN_MODERATELY_FERTILE = 'Moderately Fertile'
SIGN_MODERATELY_STERILE = 'Moderately Sterile'


# === Objects === */

# Names
SUN = 'Sun'
MOON = 'Moon'
MERCURY = 'Mercury'
VENUS = 'Venus'
MARS = 'Mars'
JUPITER = 'Jupiter'
SATURN = 'Saturn'
URANUS = 'Uranus'
NEPTUNE = 'Neptune'
PLUTO = 'Pluto'
CHIRON = 'Chiron'
NORTH_NODE = 'North Node'
SOUTH_NODE = 'South Node'
SYZYGY = 'Syzygy'
PARS_FORTUNA = 'Pars Fortuna'
NO_PLANET = 'None'

# Object movement
DIRECT = 'Direct'
RETROGRADE = 'Retrograde'
STATIONARY = 'Stationary'

# Mean daily motions
MEAN_MOTION_SUN = 0.9833
MEAN_MOTION_MOON = 13.1833

# Object type
OBJ_PLANET = 'Planet'
OBJ_HOUSE = 'House'
OBJ_MOON_NODE = 'Moon Node'
OBJ_ARABIC_PART = 'Arabic Part'
OBJ_FIXED_STAR = 'Fixed Star'
OBJ_ASTEROID = 'Asteroid'
OBJ_LUNATION = 'Lunation'
OBJ_GENERIC = 'Generic'


# === Houses === */

HOUSE1 = 'House1'
HOUSE2 = 'House2'
HOUSE3 = 'House3'
HOUSE4 = 'House4'
HOUSE5 = 'House5'
HOUSE6 = 'House6'
HOUSE7 = 'House7'
HOUSE8 = 'House8'
HOUSE9 = 'House9'
HOUSE10 = 'House10'
HOUSE11 = 'House11'
HOUSE12 = 'House12'

# House conditions
ANGULAR = 'Angular'
SUCCEDENT = 'Succedent'
CADENT = 'Cadent'

# Benefic/Malefic houses
HOUSES_BENEFIC = [HOUSE1, HOUSE5, HOUSE11]
HOUSES_MALEFIC = [HOUSE6, HOUSE12]

# House Systems
HOUSES_PLACIDUS = 'Placidus'
HOUSES_KOCH = 'Koch'
HOUSES_PORPHYRIUS = 'Porphyrius'
HOUSES_REGIOMONTANUS = 'Regiomontanus'
HOUSES_CAMPANUS = 'Campanus'
HOUSES_EQUAL = 'Equal'
HOUSES_EQUAL_2 = 'Equal 2'
HOUSES_VEHLOW_EQUAL = 'Vehlow Equal'
HOUSES_WHOLE_SIGN = 'Whole Sign'
HOUSES_MERIDIAN = 'Meridian'
HOUSES_AZIMUTHAL = 'Azimuthal'
HOUSES_POLICH_PAGE = 'Polich Page'
HOUSES_ALCABITUS = 'Alcabitus'
HOUSES_MORINUS = 'Morinus'
HOUSES_DEFAULT = HOUSES_ALCABITUS


# === Angles === */

ASC = 'Asc'
DESC = 'Desc'
MC = 'MC'
IC = 'IC'


# === Fixed Stars === */

STAR_ALGENIB = 'Algenib'
STAR_ALPHERATZ = 'Alpheratz'
STAR_ALGOL = 'Algol'
STAR_ALCYONE = 'Alcyone'
STAR_PLEIADES = STAR_ALCYONE
STAR_ALDEBARAN = 'Aldebaran'
STAR_RIGEL = 'Rigel'
STAR_CAPELLA = 'Capella'
STAR_BETELGEUSE = 'Betelgeuse'
STAR_SIRIUS = 'Sirius'
STAR_CANOPUS = 'Canopus'
STAR_CASTOR = 'Castor'
STAR_POLLUX = 'Pollux'
STAR_PROCYON = 'Procyon'
STAR_ASELLUS_BOREALIS = 'Asellus Borealis'
STAR_ASELLUS_AUSTRALIS = 'Asellus Australis'
STAR_ALPHARD = 'Alphard'
STAR_REGULUS = 'Regulus'
STAR_DENEBOLA = 'Denebola'
STAR_ALGORAB = 'Algorab'
STAR_SPICA = 'Spica'
STAR_ARCTURUS = 'Arcturus'
STAR_ALPHECCA = 'Alphecca'
STAR_ZUBEN_ELGENUBI = 'Zuben Elgenubi'
STAR_ZUBEN_ELSCHEMALI = 'Zuben Eshamali'
STAR_UNUKALHAI = 'Unukalhai'
STAR_AGENA = 'Agena'
STAR_RIGEL_CENTAURUS = 'Rigel Kentaurus'
STAR_ANTARES = 'Antares'
STAR_LESATH = 'Lesath'
STAR_VEGA = 'Vega'
STAR_ALTAIR = 'Altair'
STAR_DENEB_ALGEDI = 'Deneb Algedi'
STAR_FOMALHAUT = 'Fomalhaut'
STAR_DENEB_ADIGE = 'Deneb'  # Alpha-Cygnus
STAR_ACHERNAR = 'Achernar'


# === Aspects === */

# Major Aspects
NO_ASPECT = -1
CONJUNCTION = 0
SEXTILE = 60
SQUARE = 90
TRINE = 120
OPPOSITION = 180

# Minor Aspects
SEMISEXTILE = 30
SEMIQUINTILE = 36
SEMISQUARE = 45
QUINTILE = 72
SESQUIQUINTILE = 108
SESQUISQUARE = 135
BIQUINTILE = 144
QUINCUNX = 150

# Aspect movement
APPLICATIVE = 'Applicative'
SEPARATIVE = 'Separative'
EXACT = 'Exact'
NO_MOVEMENT = 'None'

# Aspect direction
DEXTER = 'Dexter'      # Right side
SINISTER = 'Sinister'  # Left side

# Aspect properties
ASSOCIATE = 'Associate'
DISSOCIATE = 'Dissociate'

# Aspect lists
MAJOR_ASPECTS = [0, 60, 90, 120, 180]
MINOR_ASPECTS = [30, 36, 45, 72, 108, 135, 144, 150]
ALL_ASPECTS = MAJOR_ASPECTS + MINOR_ASPECTS


# === Some Lists === */

LIST_SIGNS = [
    ARIES, TAURUS, GEMINI, CANCER, LEO, VIRGO, LIBRA,
    SCORPIO, SAGITTARIUS, CAPRICORN, AQUARIUS, PISCES
]

LIST_OBJECTS = [
    SUN, MOON, MERCURY, VENUS, MARS, JUPITER, SATURN, 
    URANUS, NEPTUNE, PLUTO, CHIRON, NORTH_NODE,
    SOUTH_NODE, SYZYGY, PARS_FORTUNA,
]

LIST_OBJECTS_TRADITIONAL = [
    SUN, MOON, MERCURY, VENUS, MARS, JUPITER, SATURN,
    NORTH_NODE, SOUTH_NODE, SYZYGY, PARS_FORTUNA
]

LIST_SEVEN_PLANETS = [
    SUN, MOON, MERCURY, VENUS, MARS, JUPITER, SATURN
]

LIST_HOUSES = [
    HOUSE1, HOUSE2, HOUSE3, HOUSE4, HOUSE5, HOUSE6,
    HOUSE7, HOUSE8, HOUSE9, HOUSE10, HOUSE11, HOUSE12,
]

LIST_ANGLES = [
    ASC, MC, DESC, IC
]

LIST_FIXED_STARS = [
    STAR_ALGENIB, STAR_ALPHERATZ, STAR_ALGOL, STAR_ALCYONE,
    STAR_PLEIADES, STAR_ALDEBARAN, STAR_RIGEL, STAR_CAPELLA,
    STAR_BETELGEUSE, STAR_SIRIUS, STAR_CANOPUS, STAR_CASTOR,
    STAR_POLLUX, STAR_PROCYON, STAR_ASELLUS_BOREALIS,
    STAR_ASELLUS_AUSTRALIS, STAR_ALPHARD, STAR_REGULUS,
    STAR_DENEBOLA, STAR_ALGORAB, STAR_SPICA, STAR_ARCTURUS,
    STAR_ALPHECCA, STAR_ZUBEN_ELSCHEMALI, STAR_UNUKALHAI,
    STAR_AGENA, STAR_RIGEL_CENTAURUS, STAR_ANTARES,
    STAR_LESATH, STAR_VEGA, STAR_ALTAIR, STAR_DENEB_ALGEDI,
    STAR_FOMALHAUT, STAR_DENEB_ADIGE, STAR_ACHERNAR,
]
