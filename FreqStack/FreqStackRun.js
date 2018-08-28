const freqStack = require("./FreqStack");

exports.run = function() {
  freqStack.push(5);
  freqStack.push(7);
  freqStack.push(5);
  freqStack.push(7);
  freqStack.push(4);
  freqStack.push(5);

  let num = freqStack.pop();
  while (num !== null) {
    console.log(num);
    num = freqStack.pop();
  }
};

exports.dump = function() {
  freqStack.push(5);
  freqStack.push(7);
  freqStack.push(5);
  freqStack.push(7);
  freqStack.push(4);
  freqStack.push(5);

  freqStack.dump();
};
