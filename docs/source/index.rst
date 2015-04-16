Flatlib documentation
=====================

Flatlib is a Python 3 library for Traditional Astrology.::

    >>> date = Datetime('2015/03/13', '17:00', '+00:00')
    >>> pos = GeoPos('38n32', '8w54')
    >>> chart = Chart(date, pos)

    >>> sun = chart.get(const.SUN)
    >>> print(sun)
    <Sun Pisces +22:47:25 +00:59:51>


Contents
--------

.. toctree::
   :maxdepth: 2
   
   installation
   tutorials/index
   faq