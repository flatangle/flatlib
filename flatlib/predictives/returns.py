"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module provides useful functions for 
    handling solar and lunar returns.
    It only handles solar returns for now.
    
"""

from flatlib import const
from flatlib.ephem import ephem
from flatlib.chart import Chart



def _computeChart(chart, date):
    """ Internal function to return a new chart for
    a specific date using properties from old chart.
    
    """
    pos = chart.pos
    hsys = chart.hsys
    IDs = [obj.id for obj in chart.objects]
    return Chart(date, pos, IDs=IDs, hsys=hsys)

def nextSolarReturn(chart, date):
    """ Returns the solar return of a Chart
    after a specific date.
    
    """
    sun = chart.getObject(const.SUN)
    srDate = ephem.nextSolarReturn(date, sun.lon)
    return _computeChart(chart, srDate)

def prevSolarReturn(chart, date):
    """ Returns the solar return of a Chart
    before a specific date.
    
    """
    sun = chart.getObject(const.SUN)
    srDate = ephem.prevSolarReturn(date, sun.lon)
    return _computeChart(chart, srDate)