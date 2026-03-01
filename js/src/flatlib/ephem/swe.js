// Port of flatlib/ephem/swe.py to JavaScript
// This module provides a thin wrapper around the Swiss
// Ephemeris. Node users should install the `swisseph` npm
// package (https://www.npmjs.com/package/swisseph).

// Attempt to load the native Swiss Ephemeris wrapper. If the
// package is not installed (e.g. during early development) we fall
// back to a stubbed object so that the module can still be imported.
import * as angle from '../angle.js';
import * as consts from '../const.js';

import { createRequire } from 'module';
const require = createRequire(import.meta.url);
let swisseph;
try {
  swisseph = require('swisseph');
} catch (err) {
  // stub functions with basic signatures
  swisseph = {
    swe_set_ephe_path: () => {},
    swe_calc_ut: () => [0, 0, 0, 0, 0],
    swe_rise_trans: () => [0, [0, 0]],
    swe_houses: () => [[0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0]],
    swe_fixstar_ut: () => [0, 0],
    swe_fixstar_mag: () => 0,
    CALC_RISE: 0,
    CALC_SET: 1,
  };
}

// Map objects
export const SWE_OBJECTS = {
  [consts.SUN]: 0,
  [consts.MOON]: 1,
  [consts.MERCURY]: 2,
  [consts.VENUS]: 3,
  [consts.MARS]: 4,
  [consts.JUPITER]: 5,
  [consts.SATURN]: 6,
  [consts.URANUS]: 7,
  [consts.NEPTUNE]: 8,
  [consts.PLUTO]: 9,
  [consts.CHIRON]: 15,
  [consts.NORTH_NODE]: 10,
};

// Map house systems
export const SWE_HOUSESYS = {
  [consts.HOUSES_PLACIDUS]: 'P',
  [consts.HOUSES_KOCH]: 'K',
  [consts.HOUSES_PORPHYRIUS]: 'O',
  [consts.HOUSES_REGIOMONTANUS]: 'R',
  [consts.HOUSES_CAMPANUS]: 'C',
  [consts.HOUSES_EQUAL]: 'A',
  [consts.HOUSES_EQUAL_2]: 'E',
  [consts.HOUSES_VEHLOW_EQUAL]: 'V',
  [consts.HOUSES_WHOLE_SIGN]: 'W',
  [consts.HOUSES_MERIDIAN]: 'X',
  [consts.HOUSES_AZIMUTHAL]: 'H',
  [consts.HOUSES_POLICH_PAGE]: 'T',
  [consts.HOUSES_ALCABITUS]: 'B',
  [consts.HOUSES_MORINUS]: 'M',
};

// ==== Internal functions ====
export function setPath(path) {
  swisseph.swe_set_ephe_path(path);
}

// === Object functions ===
export function sweObject(obj, jd) {
  const sweObj = SWE_OBJECTS[obj];
  // `swe_calc_ut` returns an array [lon, lat, distance, speedlon,...]
  const res = swisseph.swe_calc_ut(jd, sweObj);
  // some wrappers return object with error, handle both
  const sweList = Array.isArray(res) ? res : res[0];
  return {
    id: obj,
    lon: sweList[0],
    lat: sweList[1],
    lonspeed: sweList[3],
    latspeed: sweList[4],
  };
}

export function sweObjectLon(obj, jd) {
  const sweObj = SWE_OBJECTS[obj];
  const res = swisseph.swe_calc_ut(jd, sweObj);
  const sweList = Array.isArray(res) ? res : res[0];
  return sweList[0];
}

export function sweNextTransit(obj, jd, lat, lon, flag) {
  const sweObj = SWE_OBJECTS[obj];
  const swFlag = flag === 'RISE' ? swisseph.CALC_RISE : swisseph.CALC_SET;
  const trans = swisseph.swe_rise_trans(jd, sweObj, lon, lat, 0, 0, 0, swFlag);
  // returns [status, [jdRise, jdSet]]
  return trans[1][0];
}

// === Houses and angles ===
export function sweHouses(jd, lat, lon, hsys) {
  const code = SWE_HOUSESYS[hsys];
  const res = swisseph.swe_houses(jd, lat, lon, code);
  // result is [hlist, ascmc]
  const hlist = res[0].slice();
  const ascmc = res[1].slice();
  hlist.push(hlist[0]);
  const houses = [];
  for (let i = 0; i < 12; i++) {
    houses.push({
      id: consts.LIST_HOUSES[i],
      lon: hlist[i],
      size: angle.distance(hlist[i], hlist[i + 1]),
    });
  }
  const angles = [
    { id: consts.ASC, lon: ascmc[0] },
    { id: consts.MC, lon: ascmc[1] },
    { id: consts.DESC, lon: angle.norm(ascmc[0] + 180) },
    { id: consts.IC, lon: angle.norm(ascmc[1] + 180) },
  ];
  return [houses, angles];
}

export function sweHousesLon(jd, lat, lon, hsys) {
  const code = SWE_HOUSESYS[hsys];
  const res = swisseph.swe_houses(jd, lat, lon, code);
  const ascmc = res[1];
  const angles = [
    ascmc[0],
    ascmc[1],
    angle.norm(ascmc[0] + 180),
    angle.norm(ascmc[1] + 180),
  ];
  return [res[0], angles];
}

// === Fixed stars ===
export function sweFixedStar(star, jd) {
  const sweList = swisseph.swe_fixstar_ut(star, jd);
  const mag = swisseph.swe_fixstar_mag(star);
  return {
    id: star,
    mag,
    lon: sweList[0],
    lat: sweList[1],
  };
}
