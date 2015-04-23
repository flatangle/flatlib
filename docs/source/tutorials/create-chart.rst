Creating a Chart
================

The goal for this tutorial is to help you create a Chart for a specific date and location.
To build a Chart it will be necessary to define:

* the date and time, given by the *Datetime* object.
* the geographic position, given by the *GeoPos* object. 


Datetime
--------

The *Datetime* class represents a specific moment in time given by a *Date*, a *Time*, an *UTC offset* 
and the calendar type. It assumes, by default, the Gregorian calendar.

To create a Datetime object, we must first import it. Here's an example that creates a Datetime object for the
13th of March of 2015 at 5pm, assuming UTC+0::

   >>> from flatlib.datetime import Datetime
   >>> date = Datetime('2015/03/13', '17:00', '+00:00')
   >>> date.jd
   2457095.2083333335
   
The *jd* attribute (as in ``date.jd``) returns the `Julian Date`_.

The time and UTC offset parameters are optional, and the arguments could be given as lists instead of strings.
Some alternative ways to build the same date object are::

   >>> # No UTC Offset argument
   >>> date = Datetime('2015/03/13', '17:00')
   >>> date.jd
   2457095.2083333335
   
   >>> # Build date with date and time lists
   >>> date = Datetime([2015,3,13], ['+',17,0,0])
   >>> date.jd
   2457095.2083333335

The Datetime object provides properties and functions which may be useful for some situations::

   >>> # Print date, time and offset
   >>> print(date.date)
   <2015/03/13>
   >>> print(date.time)
   <17:00:00>
   >>> print(date.utcoffset)
   <00:00:00>
   
   >>> # Other properties
   >>> date.date.dayofweek()
   5   # 5 is Friday
   >>> date.time.toList()
   ['+', 17, 0, 0]


GeoPos
------

The *GeoPos* class represents a geographic position on Earth given by a latitude and longitude. 
To create a GeoPos object, we must first import the class definition and instantiate an object. 
Here's an example::

   >>> from flatlib.geopos import GeoPos
   >>> pos = GeoPos('38n32', '8w54')
   >>> pos.lat
   38.53333333333333
   >>> pos.lon
   -8.9
   
When building the geopos object, the first parameter must be the latitude and the second the longitude. 
The latitude and longitude properties can be accessed directly (using ``pos.lat`` and ``pos.lon``). 
Northern latitudes and eastern longitudes have positive values, while southern latitudes and western longitudes 
have negative values.

Alternative ways to build a Geopos object can be::

   >>> # Using angle strings
   >>> pos = GeoPos('+38:32','-8:54')
   >>> pos.lat, pos.lon
   (38.53333333333333, -8.9)
   
   >>> # Using angle lists 
   >>> pos = GeoPos(['+',38,32], ['-',8,54])
   >>> pos.lat, pos.lon
   (38.53333333333333, -8.9)
   
   >>> # Using the float values
   >>> pos = GeoPos(38.53333333333333, -8.9)
   >>> pos.lat, pos.lon
   (38.53333333333333, -8.9)


Chart
-----

The *Chart* class represents an Astrology chart for a specific datetime and geographic position.
To create a chart object, we must create the Datetime and GeoPos objects and pass them as arguments to the Chart::

   >>> # Set datetime and position
   >>> from flatlib.datetime import Datetime
   >>> from flatlib.geopos import GeoPos
   >>> date = Datetime('2015/03/13', '17:00', '+00:00')
   >>> pos = GeoPos('38n32', '8w54')
   
   >>> # Finally create the chart
   >>> from flatlib.chart import Chart
   >>> chart = Chart(date, pos)

By default, the chart will include only the Traditional planets (*Sun* to *Saturn*, including *Pars Fortuna* and 
the Moon nodes) and the *Alcabitius* house system. 
To create a chart with other parameters, we must first import the **flatlib.const** module (where some things are 
defined) and pass some arguments in the object constructor::

   >>> from flatlib import const
   
   >>> # Build a chart with Regiomontanus houses
   >>> chart = Chart(date, pos, hsys=const.HOUSES_REGIOMONTANUS)
   
   >>> # Build a chart including modern planets
   >>> chart = Chart(date, pos, IDs=const.LIST_OBJECTS)
   
   >>> # Build a chart with only the Sun and Moon
   >>> chart = Chart(date, pos, IDs=[const.SUN, const.MOON])   

In the next tutorials it will be shown how we can access the chart's properties, including objects, houses and angles.


.. _`Julian Date`: http://en.wikipedia.org/wiki/Julian_day