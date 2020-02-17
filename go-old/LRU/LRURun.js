const lru = require("./LeastRecentUsed");

const build = function(set) {
  lru.initialize(2);

  if (set && set.length > 0) {
    set.forEach(pair => {
      lru.put(pair.key, pair.value);
    });
  } else {
    lru.put(1, 1);
    lru.put(2, 2);
    lru.get(1);
    lru.put(3, 3);
    lru.get(2);
    lru.put(4, 4);
    lru.get(1);
    lru.get(3);
    lru.get(4);
  }
};

const test = function(set) {
  build(set);

  console.log(lru.get(1));
  console.log(lru.get(3));
  console.log(lru.get(4));
};

const dump = function(set) {
  build(set);
  lru.dump();
};

exports.run = function(set, debug) {
  if (debug) {
    dump(set);
  } else {
    test(set);
  }
};
