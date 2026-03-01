// Port of flatlib/ephem/tools.py to JavaScript

import * as swe from './swe.js';
import * as angle from '../angle.js';
import * as consts from '../const.js';
import * as utils from '../utils.js';

export const MAX_ERROR = 0.0003;

// === Object positions ===
export function pfLon(jd, lat, lon) {
  const sun = swe.sweObjectLon(consts.SUN, jd);
  const moon = swe.sweObjectLon(consts.MOON, jd);
  const asc = swe.sweHousesLon(jd, lat, lon, consts.HOUSES_DEFAULT)[1][0];

  if (isDiurnal(jd, lat, lon)) {
    return angle.norm(asc + moon - sun);
  } else {
    return angle.norm(asc + sun - moon);
  }
}

// === Diurnal ===
export function isDiurnal(jd, lat, lon) {
  const sun = swe.sweObject(consts.SUN, jd);
  const mc = swe.sweHousesLon(jd, lat, lon, consts.HOUSES_DEFAULT)[1][1];
  const [ra, decl] = utils.eqCoords(sun.lon, sun.lat);
  const [mcRA] = utils.eqCoords(mc, 0.0);
  return utils.isAboveHorizon(ra, decl, mcRA, lat);
}

// === Iterative algorithms ===
export function syzygyJD(jd) {
  let sun = swe.sweObjectLon(consts.SUN, jd);
  let moon = swe.sweObjectLon(consts.MOON, jd);
  let dist = angle.distance(sun, moon);
  const offset = dist >= 180 ? 180 : 0;
  while (Math.abs(dist) > MAX_ERROR) {
    jd = jd - dist / 13.1833;
    sun = swe.sweObjectLon(consts.SUN, jd);
    moon = swe.sweObjectLon(consts.MOON, jd);
    dist = angle.closestdistance(sun - offset, moon);
  }
  return jd;
}

export function solarReturnJD(jd, lon, forward = true) {
  let sun = swe.sweObjectLon(consts.SUN, jd);
  let dist;
  if (forward) {
    dist = angle.distance(sun, lon);
  } else {
    dist = angle.distance(lon, sun);
  }
  while (Math.abs(dist) > MAX_ERROR) {
    jd = jd + dist / 0.9833;
    sun = swe.sweObjectLon(consts.SUN, jd);
    dist = angle.closestdistance(sun, lon);
  }
  return jd;
}
