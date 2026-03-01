import { ephem, swe, eph, tools } from '../src/flatlib/ephem/index.js';
import * as consts from '../src/flatlib/const.js';

describe('ephem package', () => {
  test('basic exports are present', () => {
    expect(typeof ephem.getObject).toBe('function');
    expect(typeof ephem.getHouses).toBe('function');
    expect(typeof swe.sweObject).toBe('function');
    expect(typeof eph.getObject).toBe('function');
    expect(typeof tools.pfLon).toBe('function');
  });

  test('object map includes Sun and Moon', () => {
    expect(swe.SWE_OBJECTS[consts.SUN]).toBeDefined();
    expect(swe.SWE_OBJECTS[consts.MOON]).toBeDefined();
  });
});
