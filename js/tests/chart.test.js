import { HOUSES_MORINUS } from '../src/flatlib/const.js';

// Placeholder imports; real implementations will be added once modules are ported
import { Chart } from '../src/flatlib/chart.js';
import { Datetime } from '../src/flatlib/datetime.js';
import { GeoPos } from '../src/flatlib/geopos.js';

describe('Chart', () => {
  let date;
  let pos;

  beforeEach(() => {
    date = new Datetime('2015/03/13', '17:00', '+00:00');
    pos = new GeoPos('38n32', '8w54');
  });

  test('solar return hsys', () => {
    const chart = new Chart(date, pos, { hsys: HOUSES_MORINUS });
    const sr = chart.solarReturn(2018);
    expect(chart.hsys).toBe(sr.hsys);
  });
});