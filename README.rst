flatlib
=======

A Python 3 library for Traditional Astrology.


Example
-------

::

    >>> date = Datetime('2015/03/10', '14:00', '+00:00')
    >>> pos = GeoPos('38n32', '8w54')
    >>> chart = Chart(date, pos)

    >>> sun = chart.get(const.SUN)    
    >>> print(sun)
    <Sun Pisces +19:40:13 +00:59:57>


Changelog
---------

* 0.2.1 (released 06-05-2016)
    - Added Pars Horsemanship
    - Return accidental dignities that score more than zero
    - Added chartdynamics.disposits to return dignities where planet A disposes a planet B
    - Includes new Triplicity Faces

* 0.2.0 (released 08-04-2015)
    - Many new features:
        - Planetary time
        - Arabic Parts
        - Chart Dynamics
        - Accidental dignities
        - Predictives (Profections, Solar Returns and Primary Directions)
        - Protocols (Almutem, Temperament and Behavior calculations)
    - Bug fixes
    
* 0.1.1 (released 18-03-2015)
    - Changed threshold for stationary (1 arc-second)
    - Implementation of essential dignities
    - Added essential dignities recipe

* 0.1.0 (released 14-03-2015)
    - Initial release
    - Implementation of core modules
