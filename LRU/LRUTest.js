var assert = require("assert");
var lru = require("./LeastRecentUsed");

describe("Basics", function() {
  beforeEach(function() {
    lru.reset();
  });

  it("Null in, null out", function() {
    assert.equal(lru.get(1), null);
  });

  it("Checks", function() {
    lru.put(1, 1);
    lru.put(2, 2);
    assert.equal(lru.get(1), 1);

    lru.put(3, 3);
    assert.equal(lru.get(2), null);

    lru.put(4, 4);
    assert.equal(lru.get(1), null);

    assert.equal(lru.get(3), 3);

    assert.equal(lru.get(4), 4);
  });
});
