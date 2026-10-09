from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.ephem import swe

"""
Module to calcualate the moon next ingress and
voc
"""

# Assign a minute in Julian Calendar
MINUTE = const.MINUTE
# List of house distances
DIST = [0, 2, 3, 4, 6, 8, 9, 10]

# Mean Moon motion in deg/s
MEAN_MOTION_MOON_S = const.MEAN_MOTION_MOON / 86400

MAX_ERROR = 0.0003

def next_moon_ingress(chart):
    """
    Calculates datetime of the next Moon ingress
    """

    # Define the sign angles
    angles = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]

    # Initate local variables
    # The next sign angle from the current moon position
    angle = 0.0
    # Distance between the current Moon position and the next sign
    dist = 0.0
    # Intiate iteration counter for statistical purposes
    i = 0

    # Load the current Moon position
    moon_lon = swe.sweObjectLon(const.MOON, chart.date.jd)

    # Find the next sign angle
    for ang in angles:
        if moon_lon < ang:
            angle = ang
            dist = ang - moon_lon
            break

    # Evalute a mean time in days before the next Moon ingress
    jd = dist / const.MEAN_MOTION_MOON

    # Add the 'jd' into the the current Moon position
    jd = jd + chart.date.jd

    # Run the loop for calculating the ingress time
    while abs(dist) > MAX_ERROR:
        # Get Moon longtitude
        moon_lon = swe.sweObjectLon(const.MOON, jd)
        # Correct value of the moon's longtitude if ingress
        # to Aries
        if angle == 360 and moon_lon >= 0.0 and moon_lon < 30.0:
            moon_lon = moon_lon + 360.0
        
        # Calcualte distance
        dist = angle - moon_lon
        # Calculate position differential
        jd = jd + dist / const.MEAN_MOTION_MOON

        i += 1
    return {'Date':Datetime.fromJD(jd, '+00:00'), 'Iter':i} 

