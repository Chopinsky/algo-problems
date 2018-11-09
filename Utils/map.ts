export interface Result<V> {
  errMessage: string;
  value: V;
}

export type KeyType = string | number | symbol;

export class Map<V> {
  constructor(readonly _store: object = {}) {}

  add(key: KeyType, val: V): Result<V> {
    return update(this._store, key, val, false);
  }

  insert(key: KeyType, val: V): Result<V> {
    return update(this._store, key, val, true);
  }

  get(key: KeyType): Result<V> {
    if (typeof key === "string" && key.length === 0) {
      return resultFactory("Key cannot be empty");
    }

    if (!this._store.hasOwnProperty(key)) {
      return resultFactory(
        `This key: ${key.toString()} does not exist in the map`
      );
    }

    return resultFactory(null, this._store[key]);
  }

  remove(key: KeyType): Result<V> {
    if (!this._store.hasOwnProperty(key)) {
      return resultFactory(null, null);
    }

    let oldVal: V = this._store[key];
    delete this._store[key];

    return resultFactory(null, oldVal);
  }
}

const update = <V extends {}>(
  store: object,
  key: KeyType,
  val: V,
  override: boolean
): Result<V> => {
  if (typeof key === "string" && key.length === 0) {
    return resultFactory("Key cannot be empty");
  }

  let oldVal: V = undefined;
  if (store.hasOwnProperty(key)) {
    if (!override) {
      return resultFactory(
        "Key already exists; if you wish to update the value, use method `insert()` instead"
      );
    }

    oldVal = store[key];
  }

  store[key] = val;
  return resultFactory(null, oldVal);
};

const resultFactory = <V extends {}>(
  errMessage: string | null,
  value: V | undefined = undefined
): Result<V> => {
  return Object.freeze({
    errMessage,
    value
  });
};
