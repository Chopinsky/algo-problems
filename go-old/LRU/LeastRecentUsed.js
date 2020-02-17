let _capacity = 1;
let _size = 0;
let _cacheHead = null;
let _cacheMap = {};

const initialize = function(size) {
  if (typeof size !== "number" || size <= 0) {
    console.error(`New size must be a positive integer, but now it's ${size}`);
    return;
  }

  setCapacity(size);
};

const reset = function() {
  _cacheHead = null;
  _cacheMap = {};
  _size = 0;
};

const shrinkToSize = function(size) {
  if (typeof size !== "number" || size < 1) {
    console.error(`Size must be a positive integer, but now it's ${capacity}`);
    return;
  }

  let count = 1;
  let node = _cacheHead;

  while (node) {
    const next = node.next;

    if (count === size) {
      node.next = null;
    }

    if (count > size && _cacheMap.hasOwnProperty(node.key)) {
      delete _cacheMap[node.key];
    }

    node = next;
    count++;
  }
};

const setCapacity = function(capacity) {
  if (typeof capacity !== "number" || capacity < 1) {
    console.error(
      `New capacity must be a positive integer, but now it's ${capacity}`
    );
    return;
  }

  if (capacity === _capacity) {
    return;
  }

  if (capacity < _capacity && _cacheHead !== null) {
    shrinkToSize(capacity);
  }

  _capacity = capacity;
};

const find = function(key) {
  if (_cacheMap.hasOwnProperty(key)) {
    let node = _cacheMap[key];
    if (!node) {
      console.error(`Bad data for key: ${key}.`);
      return null;
    }

    // if already at the head, no more to be done
    if (_cacheHead.key === node.key) {
      return node;
    }

    // delete the node from the double-linked list
    let prev = node.prev;
    let next = node.next;

    if (prev) {
      prev.next = next;
    }

    if (next) {
      next.prev = prev;
    }

    // add the node to the cache head
    node.next = _cacheHead;
    node.prev = null;
    _cacheHead.prev = node;
    _cacheHead = node;

    return _cacheHead;
  }

  return null;
};

const get = function(key) {
  let node = find(key);
  if (node) {
    return node.value;
  }

  return null;
};

const put = function(key, value) {
  if (typeof key !== "number" || typeof value !== "number") {
    console.error(
      `The key and value must be integers, but they are: ${key}, ${value}.`
    );

    return;
  }

  if (_cacheMap.hasOwnProperty(key)) {
    // if already in the cache, bring it to the head
    let node = find(key);
    node.value = value;
  } else {
    // if not in the cache, add it to the head and the cache map, pop and remove the last element
    // if at the capacity.
    let node = Object.assign(
      {},
      {
        key,
        value,
        prev: null,
        next: _cacheHead
      }
    );

    _cacheMap[key] = node;
    if (_cacheHead) {
      _cacheHead.prev = node;
    }

    _cacheHead = node;
    _size++;

    if (_size > _capacity) {
      shrinkToSize(_capacity);
      _size = _capacity;
    }
  }
};

const dump = function() {
  console.log(`\nMap:`);
  Object.keys(_cacheMap).forEach(key => {
    let node = _cacheMap[key];
    console.log(`* ${key}: ${node.value};`);
  });

  console.log("\nCache:\n head ->");
  let node = _cacheHead;
  while (node) {
    console.log(` {key: ${node.key}; Value: ${node.value}} ->`);
    node = node.next;
  }
  console.log(" tail");
};

module.exports = {
  initialize,
  reset,
  setCapacity,
  get,
  put,
  dump
};
