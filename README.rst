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

* 0.1.1 (released 18-03-2015)
    - Changed threshold for stationary (1 arc-second)
    - Implementation of essential dignities
    - Added essential dignities recipe

* 0.1.0 (released 14-03-2015)
    - Initial release
    - Implementation of core modules