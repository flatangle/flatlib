"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling 
    planetary times.

"""

from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.tools import planetarytime


# Build a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')

# Get the planetary hour table
hourTable = planetarytime.getHourTable(date, pos) 
print(hourTable.dayRuler())    # Venus
print(hourTable.nightRuler())  # Mars
print(hourTable.hourRuler())   # Saturn

# Use the info Dict to print hour number information
info = hourTable.currInfo()
print(info['hourNumber'])  # 11
print(info['start'])       # <2015/03/13 16:42:10 00:00:00>
print(info['end'])         # <2015/03/13 17:41:20 00:00:00>