# flatlib

Flatlib is a python library for Traditional Astrology.

```python
date = Datetime('2015/03/10', '14:00', '+00:00')
pos = GeoPos('38n32', '8w54')
    
sun = ephem.getObject(const.SUN, date, pos)
print(sun)

>>> <Sun Pisces +19:40:13 +00:59:57>
```
