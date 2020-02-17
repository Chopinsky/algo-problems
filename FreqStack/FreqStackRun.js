const freqStack = require("./FreqStack");

const biuldStack = function(set) {
  if (set && set.length > 0) {
    set.forEach(num => {
      freqStack.push(num);
    });
  } else {
    freqStack.push(5);
    freqStack.push(7);
    freqStack.push(5);
    freqStack.push(7);
    freqStack.push(4);
    freqStack.push(5);
  }
};

const test = function(set) {
  biuldStack(set);

  let num = freqStack.pop();
  while (num !== null) {
    console.log(num);
    num = freqStack.pop();
  }
};

const dump = function(set) {
  biuldStack(set);

  freqStack.dump();
};

exports.run = function(set, debug) {
  if (debug) {
    dump(set);
  } else {
    test(set);
  }
};
