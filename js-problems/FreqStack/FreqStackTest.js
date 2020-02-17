var assert = require("assert");
var freqStack = require("./FreqStack");

describe("Basics", function() {
  beforeEach(function() {
    freqStack.reset();
  });

  it("Null in, null out", function() {
    assert.equal(freqStack.pop(), null);
  });

  it("Basic test -> in: [5, 7, 5, 7, 4, 5]; out: [5, 7, 5, 4, 7, 5]", function() {
    freqStack.push(5);
    freqStack.push(7);
    freqStack.push(5);
    freqStack.push(7);
    freqStack.push(4);
    freqStack.push(5);

    assert.equal(freqStack.pop(), 5);
    assert.equal(freqStack.pop(), 7);
    assert.equal(freqStack.pop(), 5);
    assert.equal(freqStack.pop(), 4);
    assert.equal(freqStack.pop(), 7);
    assert.equal(freqStack.pop(), 5);

    assert.equal(freqStack.pop(), null);
  });

  it("Basic test -> in: [5, 7, 5, 7, 4, 3]; out: [7, 5, 3, 4, 7, 5]", function() {
    freqStack.push(5);
    freqStack.push(7);
    freqStack.push(5);
    freqStack.push(7);
    freqStack.push(4);
    freqStack.push(3);

    assert.equal(freqStack.pop(), 7);
    assert.equal(freqStack.pop(), 5);
    assert.equal(freqStack.pop(), 3);
    assert.equal(freqStack.pop(), 4);
    assert.equal(freqStack.pop(), 7);
    assert.equal(freqStack.pop(), 5);

    assert.equal(freqStack.pop(), null);
  });
});
