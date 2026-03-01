// Port of flatlib/utils.py to JavaScript

import * as angle from './angle.js';

// One arc-second error for iterative algorithms
export const MAX_ERROR = 0.0003;

// === Diurnal and nocturnal arcs ===
export function ascdiff(decl, lat) {
  const delta = (decl * Math.PI) / 180;
  const phi = (lat * Math.PI) / 180;
  const ad = Math.asin(Math.tan(delta) * Math.tan(phi));
  return (ad * 180) / Math.PI;
}

export function dnarcs(decl, lat) {
  const dArc = 180 + 2 * ascdiff(decl, lat);
  const nArc = 360 - dArc;
  return [dArc, nArc];
}

// === Above horizon ===
export function isAboveHorizon(ra, decl, mcRA, lat) {
  const [dArc] = dnarcs(decl, lat);
  const dist = Math.abs(angle.closestdistance(mcRA, ra));
  return dist <= dArc / 2.0 + 0.0003;
}

// === Coordinate systems ===
export function eqCoords(lon, lat) {
  const _lambda = (lon * Math.PI) / 180;
  const _beta = (lat * Math.PI) / 180;
  const _epson = (23.44 * Math.PI) / 180;

  const decl = Math.asin(
    Math.sin(_epson) * Math.sin(_lambda) * Math.cos(_beta) +
      Math.cos(_epson) * Math.sin(_beta)
  );
  const ED = Math.acos(
    (Math.cos(_lambda) * Math.cos(_beta)) / Math.cos(decl)
  );
  let ra = (lon < 180 ? ED : 2 * Math.PI - ED);

  if (
    Math.abs(angle.closestdistance(lon, 0)) < 5 ||
    Math.abs(angle.closestdistance(lon, 180)) < 5
  ) {
    const a = Math.sin(ra) * Math.cos(decl);
    const b =
      Math.cos(_epson) * Math.sin(_lambda) * Math.cos(_beta) -
      Math.sin(_epson) * Math.sin(_beta);
    if (Math.abs(a - b) > 0.0003) {
      ra = 2 * Math.PI - ra;
    }
  }

  return [(ra * 180) / Math.PI, (decl * 180) / Math.PI];
}
