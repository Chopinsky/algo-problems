const cases = {
  freqstack: (testSet, debug) => {
    console.log("Running >> Frequent Stack << \n");

    const freqStack = require("./FreqStack/FreqStackRun");
    freqStack.run(testSet, debug);
  },
  lru: (testSet, debug) => {
    console.log("Running >> Least Recent Used << \n");

    const lru = require("./LRU/LRURun");
    lru.run(testSet, debug);
  },
  binarytreerebuild: (testSet, debug) => {
    console.log("Running >> Rebuild Binary Tree << \n");

    const bt = require("./BinaryTreeRebuild/BinaryTreeRun");
    testSet = testSet
      ? testSet
      : {
          preorder: [1, 2, 4, 5, 3, 6, 7],
          postorder: [4, 5, 2, 6, 7, 3, 1]
        };

    bt.run(testSet, debug);
  },
  alltrees: (testSet, debug) => {
    console.log("Running >> All Possible Trees << \n");

    const at = require("./AllTrees/AllTreesRun");
    testSet = testSet ? testSet : 9;

    at.run2(testSet, debug);
  }
};

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
      for (let p of Object.keys(cases)) {
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
  console.info("(Running in debug mode...)");
}

if (cases.hasOwnProperty(prog)) {
  let func = cases[prog];
  if (typeof func === "function") {
    func(null, debugMode);
  } else {
    console.error(`Unable to find the entry point for the case ${prog}...\n`);
  }
} else {
  console.error(`No matching case is founded for the case ${prog}...\n`);
}

console.log("\nAll is done...");
