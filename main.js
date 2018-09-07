let prog = "";
let debugMode = false;

if (process.argv && process.argv.length > 2) {
  let params = process.argv.slice(2);

  for (let val of params) {
    let command = val.toLowerCase();
    if (command === "-d" || command === "--debug") {
      debugMode = true;
      continue;
    }

    if (!prog) {
      for (let p of ["freqstack", "lru", "binarytreerebuild"]) {
        if (p.startsWith(command)) {
          prog = p;
          break;
        }
      }
    }
  }
}

if (!prog) {
  prog = "lru";
}

if (debugMode) {
  console.info("(In debug mode...)");
}

switch (prog) {
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
    break;

  case "binarytreerebuild":
    console.log("Running Binary Tree from Traveseral:\n");

    const bt = require("./BinaryTreeRebuild/BinaryTreeRun");
    bt.run([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1], debugMode);
    break;

  default:
    break;
}

console.log("\nAll is done...");
