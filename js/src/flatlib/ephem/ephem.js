// Port of flatlib/ephem/ephem.py to JavaScript

import * as eph from './eph.js';

// Classes imported from other modules. For now they are
// simple wrappers that effectively return their input.
import { Datetime } from '../datetime.js';
import { Object, House, FixedStar, GenericObject } from '../object.js';
import { ObjectList, HouseList, FixedStarList, GenericList } from '../lists.js';

// === Objects ===
export function getObject(ID, date, pos) {
  const obj = eph.getObject(ID, date.jd, pos.lat, pos.lon);
  return Object.fromDict(obj);
}

export function getObjectList(IDs, date, pos) {
  const objList = IDs.map((ID) => getObject(ID, date, pos));
  return new ObjectList(objList);
}

// === Houses and angles ===
export function getHouses(date, pos, hsys) {
  const [houses, angles] = eph.getHouses(date.jd, pos.lat, pos.lon, hsys);
  const hList = houses.map((h) => House.fromDict(h));
  const aList = angles.map((a) => GenericObject.fromDict(a));
  return [new HouseList(hList), new GenericList(aList)];
}

export function getHouseList(date, pos, hsys) {
  return getHouses(date, pos, hsys)[0];
}

export function getAngleList(date, pos, hsys) {
  return getHouses(date, pos, hsys)[1];
}

// === Fixed stars ===
export function getFixedStar(ID, date) {
  const star = eph.getFixedStar(ID, date.jd);
  return FixedStar.fromDict(star);
}

export function getFixedStarList(IDs, date) {
  const starList = IDs.map((ID) => getFixedStar(ID, date));
  return new FixedStarList(starList);
}

// === Solar returns ===
export function nextSolarReturn(date, lon) {
  const jd = eph.nextSolarReturn(date.jd, lon);
  return Datetime.fromJD(jd, date.utcoffset);
}

export function prevSolarReturn(date, lon) {
  const jd = eph.prevSolarReturn(date.jd, lon);
  return Datetime.fromJD(jd, date.utcoffset);
}

// === Sunrise and sunsets ===
export function nextSunrise(date, pos) {
  const jd = eph.nextSunrise(date.jd, pos.lat, pos.lon);
  return Datetime.fromJD(jd, date.utcoffset);
}

export function nextSunset(date, pos) {
  const jd = eph.nextSunset(date.jd, pos.lat, pos.lon);
  return Datetime.fromJD(jd, date.utcoffset);
}

export function lastSunrise(date, pos) {
  const jd = eph.lastSunrise(date.jd, pos.lat, pos.lon);
  return Datetime.fromJD(jd, date.utcoffset);
}

export function lastSunset(date, pos) {
  const jd = eph.lastSunset(date.jd, pos.lat, pos.lon);
  return Datetime.fromJD(jd, date.utcoffset);
}
