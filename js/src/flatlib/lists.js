// Port of flatlib/lists.py to JavaScript

// The Python version defines specialized list classes; here we
// provide simple wrappers that behave like arrays but also
// carry a type identifier if needed.

export class GenericList extends Array {
  constructor(items = []) {
    super(...items);
  }
}

export class ObjectList extends GenericList {}
export class HouseList extends GenericList {}
export class FixedStarList extends GenericList {}
