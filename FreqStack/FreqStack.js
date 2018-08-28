const _map = {};
const _stacks = [];

const push = function(x) {
  if (typeof x !== "number") {
    console.error("Input must be a number...");
  }

  let freq = _map[x] && typeof _map[x] === "number" ? _map[x] + 1 : 1;
  _map[x] = freq;

  if (freq <= _stacks.length) {
    _stacks[freq - 1].push(x);
  } else {
    _stacks.push([x]);
  }
};

const pop = function() {
  if (_stacks.length === 0) {
    return null;
  }

  let high = _stacks[_stacks.length - 1];
  let result = high.pop();

  _map[result] -= 1;
  if (high.length === 0) {
    _stacks.pop();
  }

  return result;
};

const dump = function() {
  console.log(_map);
  console.log(_stacks);
};

module.exports = {
  push,
  pop,
  dump
};
