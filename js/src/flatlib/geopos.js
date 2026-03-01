// Port of flatlib/geopos.py to JavaScript

import * as angle from './angle.js';

export const LAT = 0;
export const LON = 1;

export const SIGN = { N: '+', S: '-', E: '+', W: '-' };
export const CHAR = {
  [LAT]: { '+': 'N', '-': 'S' },
  [LON]: { '+': 'E', '-': 'W' },
};

export function toFloat(value) {
  if (typeof value === 'string') {
    let v = value.toUpperCase();
    for (const char of ['N', 'S', 'E', 'W']) {
      if (v.includes(char)) {
        v = SIGN[char] + v.replace(char, ':');
        break;
      }
    }
    value = v;
  }
  return angle.toFloat(value);
}

export function toList(value) {
  return angle.toList(value);
}

export function toString(value, mode) {
  let string = angle.toString(value);
  const sign = string[0];
  const separator = CHAR[mode][sign];
  string = string.replace(':', separator);
  return string.slice(1);
}

export class GeoPos {
  constructor(lat, lon) {
    this.lat = toFloat(lat);
    this.lon = toFloat(lon);
  }

  slists() {
    return [toList(this.lat), toList(this.lon)];
  }

  strings() {
    return [toString(this.lat, LAT), toString(this.lon, LON)];
  }

  toString() {
    const [la, lo] = this.strings();
    return `<${la} ${lo}>`;
  }
}
