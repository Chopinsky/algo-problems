let runParam =
  process.argv && process.argv.length > 2
    ? process.argv[2].toLowerCase()
    : "freqstack";

let runDebug =
  process.argv && process.argv.length > 3 ? process.argv[3].toLowerCase() : "";

let debugMode = false;

if (runDebug === "-d" || runDebug === "--debug") {
  debugMode = true;
}

switch (runParam) {
  // Freq-Stack problem
  case "freqstack":
    console.log("Running Freq_Stack:\n");

    const freqStack = require("./FreqStack/FreqStackRun");
    freqStack.run(null, debugMode);

    break;

  case "lru":
    console.log("Running LRU:\n");

    const lru = require("./LRU/LRURun");
    lru.run(null, debugMode);

  default:
    break;
}

console.log("\nAll is done...");
