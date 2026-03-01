// Port of flatlib/angle.py to JavaScript
// Contains utilities for angle manipulation and conversions.

// === Angular utilities ===
export function norm(angle) {
  return ((angle % 360) + 360) % 360;
}

export function znorm(angle) {
  let a = ((angle % 360) + 360) % 360;
  return a <= 180 ? a : a - 360;
}

export function distance(angle1, angle2) {
  return norm(angle2 - angle1);
}

export function closestdistance(angle1, angle2) {
  return znorm(angle2 - angle1);
}

// === Signed list utilities ===
function _fixSlist(slist) {
  while (slist.length < 4) slist.push(0);
  return slist.slice(0, 4);
}

function _roundSlist(slist) {
  slist[slist.length - 1] = slist[slist.length - 1] >= 30 ? 60 : 0;
  for (let i = slist.length - 1; i > 0; i--) {
    if (slist[i] === 60) {
      slist[i] = 0;
      slist[i - 1] += 1;
    }
  }
  return slist.slice(0, slist.length - 1);
}

// === Base conversions ===
export function strSlist(string) {
  const sign = string.startsWith('-') ? '-' : '+';
  const values = string
    .replace(/^[-+]/, '')
    .split(':')
    .map((x) => Math.abs(parseInt(x, 10)));
  return _fixSlist([sign, ...values]);
}

export function slistStr(slist) {
  slist = _fixSlist(slist);
  const string = slist.slice(1).map((x) => String(x).padStart(2, '0')).join(':');
  return slist[0] + string;
}

export function slistFloat(slist) {
  slist = _fixSlist(slist);
  const values = slist.slice(1).map((v, i) => v / 60 ** i);
  const value = values.reduce((a, b) => a + b, 0);
  return slist[0] === '-' ? -value : value;
}

export function floatSlist(value) {
  const slist = ['+', 0, 0, 0, 0];
  if (value < 0) {
    slist[0] = '-';
  }
  let v = Math.abs(value);
  for (let i = 1; i < 5; i++) {
    slist[i] = Math.floor(v);
    v = (v - slist[i]) * 60;
  }
  return _roundSlist(slist);
}

export function strFloat(string) {
  return slistFloat(strSlist(string));
}

export function floatStr(value) {
  return slistStr(floatSlist(value));
}

// === Direct conversions ===
export function toFloat(value) {
  if (typeof value === 'string') return strFloat(value);
  if (Array.isArray(value)) return slistFloat(value);
  return value;
}

export function toList(value) {
  return floatSlist(value);
}

export function toString(value) {
  return floatStr(value);
}
