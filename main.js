// Freq-Stack problem
const freqStack = function(debug) {
  const freqTest = require("./FreqStack/FreqStackRun");
  if (debug) {
    freqTest.dump();
  } else {
    freqTest.run();
  }
};

freqStack();

console.log("Done...");
