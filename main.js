const cases = require("./cases");

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
    let start = new Date().getMilliseconds();
    let ans = func(null, debugMode);
    let end = new Date().getMilliseconds();

    if (ans) {
      console.log(ans);
    }

    console.log(`Execution time: ${end - start} ms`);
  } else {
    console.error(`Unable to find the entry point for the case ${prog}...\n`);
  }
} else {
  console.error(`No matching case is founded for the case ${prog}...\n`);
}

console.log("\nAll is done...");
