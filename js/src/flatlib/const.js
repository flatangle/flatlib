// flatlib constants ported from Python
// This module exports named constants for use throughout the library.

// Four primitive qualities
export const HOT = 'Hot';
export const COLD = 'Cold';
export const DRY = 'Dry';
export const HUMID = 'Humid';

// Four Elements
export const FIRE = 'Fire';
export const EARTH = 'Earth';
export const AIR = 'Air';
export const WATER = 'Water';

// Four Temperaments
export const CHOLERIC = 'Choleric';
export const MELANCHOLIC = 'Melancholic';
export const SANGUINE = 'Sanguine';
export const PHLEGMATIC = 'Phlegmatic';

// Genders
export const MASCULINE = 'Masculine';
export const FEMININE = 'Feminine';
export const NEUTRAL = 'Neutral';

// Factions
export const DIURNAL = 'Diurnal';
export const NOCTURNAL = 'Nocturnal';

// Sun seasons
export const SPRING = 'Spring';
export const SUMMER = 'Summer';
export const AUTUMN = 'Autumn';
export const WINTER = 'Winter';

// Moon Quarters
export const MOON_FIRST_QUARTER = 'First Quarter';
export const MOON_SECOND_QUARTER = 'Second Quarter';
export const MOON_THIRD_QUARTER = 'Third Quarter';
export const MOON_LAST_QUARTER = 'Last Quarter';

// === Signs ===
export const ARIES = 'Aries';
export const TAURUS = 'Taurus';
export const GEMINI = 'Gemini';
export const CANCER = 'Cancer';
export const LEO = 'Leo';
export const VIRGO = 'Virgo';
export const LIBRA = 'Libra';
export const SCORPIO = 'Scorpio';
export const SAGITTARIUS = 'Sagittarius';
export const CAPRICORN = 'Capricorn';
export const AQUARIUS = 'Aquarius';
export const PISCES = 'Pisces';

export const CARDINAL = 'Cardinal';
export const FIXED = 'Fixed';
export const MUTABLE = 'Mutable';

export const SIGN_FIGURE_NONE = 'None';
export const SIGN_FIGURE_BEAST = 'Beast';
export const SIGN_FIGURE_HUMAN = 'Human';
export const SIGN_FIGURE_WILD = 'Wild';

export const SIGN_FERTILE = 'Fertile';
export const SIGN_STERILE = 'Sterile';
export const SIGN_MODERATELY_FERTILE = 'Moderately Fertile';
export const SIGN_MODERATELY_STERILE = 'Moderately Sterile';

// === Objects ===
export const SUN = 'Sun';
export const MOON = 'Moon';
export const MERCURY = 'Mercury';
export const VENUS = 'Venus';
export const MARS = 'Mars';
export const JUPITER = 'Jupiter';
export const SATURN = 'Saturn';
export const URANUS = 'Uranus';
export const NEPTUNE = 'Neptune';
export const PLUTO = 'Pluto';
export const CHIRON = 'Chiron';
export const NORTH_NODE = 'North Node';
export const SOUTH_NODE = 'South Node';
export const SYZYGY = 'Syzygy';
export const PARS_FORTUNA = 'Pars Fortuna';
export const NO_PLANET = 'None';

export const DIRECT = 'Direct';
export const RETROGRADE = 'Retrogade';
export const STATIONARY = 'Stationary';

export const MEAN_MOTION_SUN = 0.9833;
export const MEAN_MOTION_MOON = 13.1833;

export const OBJ_PLANET = 'Planet';
export const OBJ_HOUSE = 'House';
export const OBJ_MOON_NODE = 'Moon Node';
export const OBJ_ARABIC_PART = 'Arabic Part';
export const OBJ_FIXED_STAR = 'Fixed Star';
export const OBJ_ASTEROID = 'Asteroid';
export const OBJ_LUNATION = 'Lunation';
export const OBJ_GENERIC = 'Generic';

// === Houses ===
export const HOUSE1 = 'House1';
export const HOUSE2 = 'House2';
export const HOUSE3 = 'House3';
export const HOUSE4 = 'House4';
export const HOUSE5 = 'House5';
export const HOUSE6 = 'House6';
export const HOUSE7 = 'House7';
export const HOUSE8 = 'House8';
export const HOUSE9 = 'House9';
export const HOUSE10 = 'House10';
export const HOUSE11 = 'House11';
export const HOUSE12 = 'House12';

export const ANGULAR = 'Angular';
export const SUCCEDENT = 'Succedent';
export const CADENT = 'Cadent';

export const HOUSES_BENEFIC = [HOUSE1, HOUSE5, HOUSE11];
export const HOUSES_MALEFIC = [HOUSE6, HOUSE12];

export const HOUSES_PLACIDUS = 'Placidus';
export const HOUSES_KOCH = 'Koch';
export const HOUSES_PORPHYRIUS = 'Porphyrius';
export const HOUSES_REGIOMONTANUS = 'Regiomontanus';
export const HOUSES_CAMPANUS = 'Campanus';
export const HOUSES_EQUAL = 'Equal';
export const HOUSES_EQUAL_2 = 'Equal 2';
export const HOUSES_VEHLOW_EQUAL = 'Vehlow Equal';
export const HOUSES_WHOLE_SIGN = 'Whole Sign';
export const HOUSES_MERIDIAN = 'Meridian';
export const HOUSES_AZIMUTHAL = 'Azimuthal';
export const HOUSES_POLICH_PAGE = 'Polich Page';
export const HOUSES_ALCABITUS = 'Alcabitus';
export const HOUSES_MORINUS = 'Morinus';
export const HOUSES_DEFAULT = HOUSES_PLACIDUS;

// === Angles ===
export const ASC = 'Asc';
export const DESC = 'Desc';
export const MC = 'MC';
export const IC = 'IC';

// === Fixed Stars ===
export const STAR_ALGENIB = 'Algenib';
export const STAR_ALPHERATZ = 'Alpheratz';
export const STAR_ALGOL = 'Algol';
export const STAR_ALCYONE = 'Alcyone';
export const STAR_PLEIADES = STAR_ALCYONE;
export const STAR_ALDEBARAN = 'Aldebaran';
export const STAR_RIGEL = 'Rigel';
export const STAR_CAPELLA = 'Capella';
export const STAR_BETELGEUSE = 'Betelgeuse';
export const STAR_SIRIUS = 'Sirius';
export const STAR_CANOPUS = 'Canopus';
export const STAR_CASTOR = 'Castor';
export const STAR_POLLUX = 'Pollux';
export const STAR_PROCYON = 'Procyon';
export const STAR_ASELLUS_BOREALIS = 'Asellus Borealis';
export const STAR_ASELLUS_AUSTRALIS = 'Asellus Australis';
export const STAR_ALPHARD = 'Alphard';
export const STAR_REGULUS = 'Regulus';
export const STAR_DENEBOLA = 'Denebola';
export const STAR_ALGORAB = 'Algorab';
export const STAR_SPICA = 'Spica';
export const STAR_ARCTURUS = 'Arcturus';