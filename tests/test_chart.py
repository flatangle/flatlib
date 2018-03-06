import unittest

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


class ChartTests(unittest.TestCase):

    def setUp(self):
        self.date = Datetime('2015/03/13', '17:00', '+00:00')
        self.pos = GeoPos('38n32', '8w54')

    def test_solar_return_hsys(self):
        """Solar return charts must maintain original house system."""
        chart = Chart(self.date, self.pos, hsys=const.HOUSES_MORINUS)
        sr_chart = chart.solarReturn(2018)
        self.assertEqual(chart.hsys, sr_chart.hsys)
