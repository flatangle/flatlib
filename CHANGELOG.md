# Changelog
---
## const.py
    * Added LIST_OBJECTS as a common source for assignement of the
      default Object list
    * Added list with ten planest for modern astrology - LIST_TEN_PLANETS
    * Added list of aspecing planets - LIST_ASP_PLANTES
    * Added list with harmonious aspects - LIST_ASPECTS_POS
    * Added list with hard aspects - LIST_ASPECTS_NEG
    * Added list with tight orbs - LIST_ORBS_TIGHT
    * Added list with wide orbs - LIST_WIDE_ORBS
    * Defined a common orbs list LIST_IRBS for asignement
    * Added constant MINUTE for Julian calendar claculations
    * Added constant HOUR for Julian calendar calculations

---
## chart.py
    * Changed Traditional list of objects with the general list LIST_OBJECTS
      so the asignement can happen in the *const.py*
    * Removed assignement of a default house system @ 166
    * Changed default house system to Placidus

---
## object.py
    * Changed the traditional house offset from -5deg to 0deg

---
## props.py
    * Feeds orbs from the const.py rather than being hardcoded
