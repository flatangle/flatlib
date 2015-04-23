Chart properties and objects
============================

In the previous tutorial it was shown the necessary steps to create a Chart object. 
In this tutorial it will be shown which properties, objects and functions are accessible on the chart.
Specifically, you will learn how to access:

* Objects, houses or angles from the chart
* Fixed stars
* Other chart functions

Let's start by creating a new chart::

   >>> from flatlib.datetime import Datetime
   >>> from flatlib.geopos import GeoPos
   >>> from flatlib.chart import Chart
   
   >>> date = Datetime('2015/03/13', '17:00', '+00:00')
   >>> pos = GeoPos('38n32', '8w54')
   >>> chart = Chart(date, pos)


Objects
-------

In *flatlib* an object is a planet, a moon node, the syzygy or pars fortuna. 
The following example shows how you can access an object from the chart::

   >>> sun = chart.getObject(const.SUN)
   >>> print(sun)
   <Sun Pisces +22:47:25 +00:59:51>
   
In this specific example, we use the *getObject* method and say specifically which object we want to access.
All objects identifiers are defined in *const.py* (see `source code`_).

Another possibility is to use the generic *get* method, which works for objects, houses, angles and fixed-stars::

   >>> moon = chart.get(const.MOON)
   >>> print(moon)
   <Moon Sagittarius +22:22:54 +13:16:01>

By default, when we *print* an object, it prints its identifier, the sign, sign longitude and travel speed.
However, more information can be accessed from the object. Some of the available properties are::

   >>> sun.lon
   352.7901809551436
   >>> sun.lat
   0.00014399505974328042
   >>> sun.sign
   'Pisces'
   >>> sun.signlon
   22.790180955143626
   >>> sun.lonspeed
   0.9976256538994072

Some of the available functions are::

   >>> sun.orb()
   15
   >>> sun.meanMotion()
   0.9833
   >>> sun.movement()
   'Direct'
   >>> sun.gender()
   'Masculine'
   >>> sun.element()
   'Fire'
   >>> sun.isFast()
   True
   
Most of these properties and functions are self explanatory.


Houses
------

Similarly to objects, a list of houses is available from the chart. 
To retrieve an individual house, we can use the *getHouse* method or the generic *get* method::

   >>> house1 = chart.get(const.HOUSE1)
   >>> print(house1)
   <House1 Virgo +03:27:30 29.39933122126604>
   
Similarly to objects, we can also access the properties of an house::

   >>> house1.lon
   153.45843823091616
   >>> house1.sign
   'Virgo'
   >>> house1.signlon
   3.4584382309161583
   >>> house1.size
   29.39933122126604

or its functions::

   >>> house1.condition()
   'Angular'
   >>> house1.gender()
   'Masculine'

Houses provides also interesting functions to check if an object is in a house, such as::

   >>> house1.hasObject(sun)
   False


Angles
------

In some house systems, such as *Equal* or *Whole sign houses*, there is a clear distinction between the *Ascendant* 
and *MC*, and the 1st and 10th house cusps, hence the necessity of angles. 
To retrieve an angle from the chart you can use the *getAngle* method or the generic *get* method::

   >>> asc = chart.get(const.ASC)
   >>> mc = chart.get(const.MC)
   >>> print(asc)
   <Asc Virgo +03:27:30>
   >>> print(mc)
   <MC Taurus +29:19:03>
   
Similarly to objects and houses, some properties and functions are also available for angles. 

Fixed-stars
-----------

To retrieve fixed stars from the chart, we must use the *getFixedStar* method::

   >>> spica = chart.getFixedStar(const.STAR_SPICA)
   >>> print(spica)
   <Spica Libra +24:03:34 0.97>
   >>> spica.mag  # magnitude
   0.97
   >>> spica.orb()
   7.5

The list of avaliable fixed stars are defined in the `source code`_. 

Lists
-----

In some cases, instead of retrieving objects, houses or angles one by one, it may be useful to get direct access to
their lists. The *chart* object provides the following lists:

* *chart.objects*, with a list of all objects
* *chart.houses*, with a list of all houses
* *chart.angles*, with a list of all angles
 
The following example uses the ``for`` command to iterate over all objects in the list of objects::

   >>> for obj in chart.objects:
   ...     print(obj)
   ...
   <Moon Sagittarius +22:22:54 +13:16:01>
   <Venus Aries +25:30:11 +01:12:41>
   <Saturn Sagittarius +04:55:45 +00:00:06>
   <Mercury Pisces +00:48:57 +01:29:49>
   <North Node Libra +11:08:28 -00:03:11>
   <Syzygy Virgo +14:50:23 +11:48:44>
   <Sun Pisces +22:47:25 +00:59:51>
   <South Node Aries +11:08:28 -00:03:11>
   <Pars Fortuna Gemini +03:03:00 +00:00:00>
   <Mars Aries +16:32:48 +00:45:18>
   <Jupiter Leo +13:38:37 -00:04:45>
   
Lists also provides us with useful functions. 
For instance, the house list provides a function to retrieve the house where an object is::

   >>> house = chart.houses.getObjectHouse(sun)
   >>> print(house)
   <House7 Pisces +03:27:30 29.39933122126604>
   
In this specific case, the sun is in the 7th house. 
The `lists.py`_ file provides a full overview of what is available for each list.  


Chart functions
---------------

Besides the functions to retrieve objects, houses, angles and fixed-stars, the chart object provides other useful 
functions::

   >>> chart.isDiurnal()
   True
   >>> chart.getMoonPhase()
   'Third Quarter'
  
Finally, the chart object also provides a useful function to retrieve the solar return chart for a year::

   >>> srchart = chart.solarReturn(2020)
   >>> print(srchart.date)
   <2020/03/12 22:01:59 00:00:00>
   
   
.. _`source code`: https://github.com/flatangle/flatlib/blob/master/flatlib/const.py
.. _`lists.py`: https://github.com/flatangle/flatlib/blob/master/flatlib/lists.py