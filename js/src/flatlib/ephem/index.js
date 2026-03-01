// Entry point for ephem subpackage

import * as swe from './swe.js';
import * as eph from './eph.js';
import * as tools from './tools.js';
import * as ephem from './ephem.js';

export { swe, eph, tools, ephem };

// Set default path; user may override using setPath
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// default sweepath, mimicking Python's flatlib.PATH_RES + 'swefiles'
export function setPath(p) {
  swe.setPath(p);
}

// immediately set path to a reasonable default (needs adjustment)
// For now leave empty or require user to call explicitly.
