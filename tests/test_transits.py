import unittest

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.transits import TransitChart


class TransitChartTests(unittest.TestCase):

    def setUp(self):
        self.date = Datetime('1993/11/15', '15:32', '+00:00')
        self.pos = GeoPos('33n27', '70w39')

    def test_transit_chart_creation(self):
        """ Test aspects """
        birth_chart = Chart(self.date, self.pos, hsys=const.HOUSES_PLACIDUS)
        dt = Datetime('2023/05/20', '23:48', '+00:00')
        transit_chart: TransitChart = TransitChart.build_chart(birth_chart, dt, transit_objects=const.LIST_TEN_PLANETS)

        self.assertEqual(transit_chart.birth_chart, birth_chart)
        self.assertEqual(transit_chart.transit_chart.hsys, birth_chart.hsys)
        self.assertEqual(transit_chart.transit_chart.houses_offset, birth_chart.houses_offset)

        object_ids = [obj.id for obj in transit_chart.transit_chart.objects]
        for planet in const.LIST_TEN_PLANETS:
            self.assertIn(planet, object_ids)


    def test_transit_chart_data(self):
        """ Test aspects """
        birth_chart = Chart(self.date, self.pos, hsys=const.HOUSES_PLACIDUS)
        dt = Datetime('2023/05/20', '23:48', '+00:00')
        transit_chart: TransitChart = TransitChart.build_chart(birth_chart, dt, transit_objects=const.LIST_TEN_PLANETS)

        sun_object = transit_chart.transit_chart.getObject(const.SUN)
        moon_object = transit_chart.transit_chart.getObject(const.MOON)
        pluto_object = transit_chart.transit_chart.getObject(const.PLUTO)
        mercury_object = transit_chart.transit_chart.getObject(const.MERCURY)
        venus_object = transit_chart.transit_chart.getObject(const.VENUS)
        uranus_object = transit_chart.transit_chart.getObject(const.URANUS)
        mars_object = transit_chart.transit_chart.getObject(const.MARS)
        jupyter_object = transit_chart.transit_chart.getObject(const.JUPITER)

        # Those values were obtained from
        # https://horoscopes.astro-seek.com/calculate-transit-chart/?send_calculation=1&muz_narozeni_den=15&muz_narozeni_mesic=11&muz_narozeni_rok=1993&muz_narozeni_hodina=12&muz_narozeni_minuta=32&muz_narozeni_sekunda=00&muz_narozeni_city=Santiago%2C+Chile&muz_narozeni_mesto_hidden=Santiago&muz_narozeni_stat_hidden=CL&muz_narozeni_podstat_kratky_hidden=&muz_narozeni_podstat_hidden=Santiago+Metropolitan&muz_narozeni_input_hidden=&muz_narozeni_podstat2_kratky_hidden=&muz_narozeni_podstat3_kratky_hidden=&muz_narozeni_sirka_stupne=33&muz_narozeni_sirka_minuty=27&muz_narozeni_sirka_smer=1&muz_narozeni_delka_stupne=70&muz_narozeni_delka_minuty=39&muz_narozeni_delka_smer=1&muz_narozeni_timezone_form=auto&muz_narozeni_timezone_dst_form=auto&send_calculation=1&zena_narozeni_den=20&zena_narozeni_mesic=5&zena_narozeni_rok=2023&zena_narozeni_hodina=19&zena_narozeni_minuta=48&zena_narozeni_city=Santiago%2C+Chile&zena_narozeni_mesto_hidden=Santiago&zena_narozeni_stat_hidden=CL&zena_narozeni_podstat_kratky_hidden=&zena_narozeni_podstat_hidden=Santiago+Metropolitan&zena_narozeni_input_hidden=&zena_narozeni_podstat2_kratky_hidden=&zena_narozeni_podstat3_kratky_hidden=&zena_narozeni_sirka_stupne=33&zena_narozeni_sirka_minuty=27&zena_narozeni_sirka_smer=1&zena_narozeni_delka_stupne=70&zena_narozeni_delka_minuty=39&zena_narozeni_delka_smer=1&zena_narozeni_timezone_form=auto&zena_narozeni_timezone_dst_form=auto&house_system=placidus&hid_fortune=1&hid_fortune_check=on&hid_vertex=1&hid_vertex_check=on&hid_chiron=1&hid_chiron_check=on&hid_lilith=1&hid_lilith_check=on&hid_uzel=1&hid_uzel_check=on&orb=3&hide_aspects=0#tabs_redraw
        # and https://carta-natal.es/
        # Our transit chart is almost equal as others online
        self.assertTrue(abs(pluto_object.signlon - 0.16) < 0.3)
        self.assertTrue(abs(moon_object.signlon - 15.31) < 0.3)
        self.assertTrue(abs(sun_object.signlon - 29.42) < 0.3)
        self.assertTrue(abs(mercury_object.signlon - 7.09) < 0.3)
        self.assertTrue(abs(venus_object.signlon - 14.23) < 0.3)
        self.assertTrue(abs(uranus_object.signlon - 19.34) < 0.3)
        self.assertTrue(abs(mars_object.signlon - 0.11) < 0.3)
        self.assertTrue(abs(jupyter_object.signlon - 0.58) < 0.4)
        self.assertEqual(pluto_object.sign, const.AQUARIUS)
        self.assertEqual(moon_object.sign, const.GEMINI)
        self.assertEqual(sun_object.sign, const.TAURUS)
        self.assertEqual(mercury_object.sign, const.TAURUS)
        self.assertEqual(venus_object.sign, const.CANCER)
        self.assertEqual(uranus_object.sign, const.TAURUS)
        self.assertEqual(mars_object.sign, const.LEO)
        self.assertEqual(jupyter_object.sign, const.TAURUS)

        aspects = transit_chart.get_aspects()

        # Test two aspects of all shown in the specified online sites
        saturn_aspects = [aspect for aspect in aspects if const.SATURN in [aspect.active.id, aspect.passive.id]]
        venus_aspect = [aspect for aspect in saturn_aspects if const.VENUS in [aspect.active.id, aspect.passive.id]][0]
        mars_aspect = [aspect for aspect in saturn_aspects if const.MARS in [aspect.active.id, aspect.passive.id]][0]
        self.assertEqual(venus_aspect.type, const.TRINE)
        self.assertEqual(mars_aspect.type, const.SQUARE)
