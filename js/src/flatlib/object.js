// Port of flatlib/object.py to JavaScript

import * as consts from './const.js';
import * as angle from './angle.js';
import * as utils from './utils.js';

// For now props is stubbed; real implementation should mirror Python's props
import { objectProps, houseProps } from './props.js';

// ------------------ //
//   Generic Object   //
// ------------------ //

export class GenericObject {
  constructor() {
    this.id = consts.NO_PLANET;
    this.type = consts.OBJ_GENERIC;
    this.lon = 0.0;
    this.lat = 0.0;
    this.sign = consts.ARIES;
    this.signlon = 0.0;
  }

  static fromDict(dict) {
    const obj = new this();
    Object.assign(obj, dict);
    return obj;
  }

  copy() {
    return this.constructor.fromDict({ ...this });
  }

  toString() {
    return `<${this.id} ${this.sign} ${angle.toString(this.signlon)}>`;
  }

  orb() {
    return -1.0;
  }

  isPlanet() {
    return this.type === consts.OBJ_PLANET;
  }

  eqCoords(zerolat = false) {
    const lat = zerolat ? 0.0 : this.lat;
    return utils.eqCoords(this.lon, lat);
  }

  relocate(lon) {
    this.lon = angle.norm(lon);
    this.signlon = this.lon % 30;
    this.sign = consts.LIST_SIGNS[Math.floor(this.lon / 30.0)];
  }

  antiscia() {
    const obj = this.copy();
    obj.type = consts.OBJ_GENERIC;
    obj.relocate(360 - obj.lon + 180);
    return obj;
  }

  cantiscia() {
    const obj = this.copy();
    obj.type = consts.OBJ_GENERIC;
    obj.relocate(360 - obj.lon);
    return obj;
  }
}

// -------------------- //
//   Astrology Object   //
// -------------------- //

export class Object extends GenericObject {
  constructor() {
    super();
    this.type = consts.OBJ_PLANET;
    this.lonspeed = 0.0;
    this.latspeed = 0.0;
  }

  toString() {
    const base = super.toString().slice(0, -1);
    return `${base} ${angle.toString(this.lonspeed)}>`;
  }

  orb() {
    return objectProps.orb[this.id];
  }

  meanMotion() {
    return objectProps.meanMotion[this.id];
  }

  movement() {
    if (Math.abs(this.lonspeed) < 0.0003) {
      return consts.STATIONARY;
    } else if (this.lonspeed > 0) {
      return consts.DIRECT;
    }
    return consts.RETROGRADE;
  }

  gender() {
    return objectProps.gender[this.id];
  }

  faction() {
    return objectProps.faction[this.id];
  }

  element() {
    return objectProps.element[this.id];
  }

  isDirect() {
    return this.movement() === consts.DIRECT;
  }

  isRetrograde() {
    return this.movement() === consts.RETROGRADE;
  }

  isStationary() {
    return this.movement() === consts.STATIONARY;
  }

  isFast() {
    return Math.abs(this.lonspeed) >= this.meanMotion();
  }
}

// ------------------ //
//     House Cusp     //
// ------------------ //

export class House extends GenericObject {
  static _OFFSET = 0.0;

  constructor() {
    super();
    this.type = consts.OBJ_HOUSE;
    this.size = 30.0;
  }

  toString() {
    const base = super.toString().slice(0, -1);
    return `${base} ${this.size}>`;
  }

  num() {
    return parseInt(this.id.slice(5), 10);
  }

  condition() {
    return houseProps.condition[this.id];
  }

  gender() {
    return houseProps.gender[this.id];
  }

  isAboveHorizon() {
    return houseProps.aboveHorizon.includes(this.id);
  }

  inHouse(lon) {
    const dist = angle.distance(this.lon + House._OFFSET, lon);
    return dist < this.size;
  }

  hasObject(obj) {
    return this.inHouse(obj.lon);
  }
}

// ------------------ //
//     Fixed Star     //
// ------------------ //

export class FixedStar extends GenericObject {
  constructor() {
    super();
    this.type = consts.OBJ_FIXED_STAR;
    this.mag = 0.0;
  }

  toString() {
    const base = super.toString().slice(0, -1);
    return `${base} ${this.mag}>`;
  }

  orb() {
    const ORBS = [[2, 7.5], [3, 5.5], [4, 3.5], [5, 1.5]];
    for (const [mag, orb] of ORBS) {
      if (this.mag < mag) {
        return orb;
      }
    }
    return 0.5;
  }

  aspects(obj) {
    const dist = angle.closestdistance(this.lon, obj.lon);
    return Math.abs(dist) < this.orb();
  }
}
