// Port of flatlib/ephem/eph.py to JavaScript

import * as swe from './swe.js';
import * as angle from '../angle.js';
import * as consts from '../const.js';

// Helper for sign information
function _signInfo(obj) {
  const lon = obj.lon;
  obj.sign = consts.LIST_SIGNS[Math.floor(lon / 30)];
  obj.signlon = lon % 30;
}

// === Objects ===
export function getObject(ID, jd, lat, lon) {
  let obj;
  if (ID === consts.SOUTH_NODE) {
    obj = swe.sweObject(consts.NORTH_NODE, jd);
    obj.id = consts.SOUTH_NODE;
    obj.lon = angle.norm(obj.lon + 180);
  } else if (ID === consts.PARS_FORTUNA) {
    const pflon = tools.pfLon(jd, lat, lon);
    obj = {
      id: ID,
      lon: pflon,
      lat: 0,
      lonspeed: 0,
      latspeed: 0,
    };
  } else if (ID === consts.SYZYGY) {
    const szjd = tools.syzygyJD(jd);
    obj = swe.sweObject(consts.MOON, szjd);
    obj.id = consts.SYZYGY;
  } else {
    obj = swe.sweObject(ID, jd);
  }
  _signInfo(obj);
  return obj;
}

// === Houses ===
export function getHouses(jd, lat, lon, hsys) {
  const [houses, angles] = swe.sweHouses(jd, lat, lon, hsys);
  houses.forEach(_signInfo);
  angles.forEach(_signInfo);
  return [houses, angles];
}

// === Fixed stars ===
export function getFixedStar(ID, jd) {
  const star = swe.sweFixedStar(ID, jd);
  _signInfo(star);
  return star;
}

// === Solar returns ===
export function nextSolarReturn(jd, lon) {
  return tools.solarReturnJD(jd, lon, true);
}

export function prevSolarReturn(jd, lon) {
  return tools.solarReturnJD(jd, lon, false);
}

// === Sunrises/sunsets ===
export function nextSunrise(jd, lat, lon) {
  return swe.sweNextTransit(consts.SUN, jd, lat, lon, 'RISE');
}

export function nextSunset(jd, lat, lon) {
  return swe.sweNextTransit(consts.SUN, jd, lat, lon, 'SET');
}

export function lastSunrise(jd, lat, lon) {
  return nextSunrise(jd - 1.0, lat, lon);
}

export function lastSunset(jd, lat, lon) {
  return nextSunset(jd - 1.0, lat, lon);
}

// import tools at bottom to avoid circular dependency
import * as tools from './tools.js';
