from datetime import datetime

from flatlib import const
from flatlib.aspects import getAspect
from flatlib.chart import Chart


# === Public transit classes === #
class TransitChart:
    """
    birth_cbart: Chart - Birth Chart of a person
    transit_chart: Chart - Chart with the planets current position
    transit_aspects: list[int] - List of aspects to calculate in the transits chart. Default to major aspects
    """
    birth_chart: Chart
    transit_chart: Chart

    # Transit Chart config. It defines which information should be retrieved
    transit_aspects: list[int]

    def __init__(self, birth_chart: Chart = None, transit_chart: Chart = None,
                 transit_aspects: list[int] = const.MAJOR_ASPECTS) -> None:
        super().__init__()
        self.birth_chart = birth_chart
        self.transit_chart = transit_chart
        self.transit_aspects = transit_aspects

    def _get_transit_object_aspects(self, transit_object, birth_objects):
        # Get aspects
        aspects = [getAspect(transit_object, birth_object, self.transit_aspects) for birth_object in birth_objects]

        # Remove no aspects objects before return
        return [aspect for aspect in aspects if aspect.type is not const.NO_ASPECT]

    def get_aspects(self):
        """
        Get the list of all transit aspects.
        """
        # transit_aspects = []
        birth_objects = self.birth_chart.objects
        return sum([self._get_transit_object_aspects(transit_obj, birth_objects) for transit_obj in self.transit_chart.objects], [])


    @staticmethod
    def build_chart(birth_chart: Chart, dt: datetime, transit_objects: list[str] = const.LIST_SEVEN_PLANETS,
                    transit_aspects: list[int] = const.MAJOR_ASPECTS):
        """
            Get transit chart from birth chart
        """
        transit_chart = Chart(
            dt, birth_chart.pos,
            IDs=transit_objects,
            hsys=birth_chart.hsys,
            houses_offset=birth_chart.houses_offset)
        return TransitChart(birth_chart, transit_chart, transit_aspects)