import { Cases, Executor } from "./executor";

interface Command {
  prog: string;
  debug: boolean;
}

class main {
  public static run(): number {
    let cases: any = require("./cases.js");
    let { prog, debug } = this.parseCommand(cases);

    if (debug) {
      console.info("(Running in debug mode...)");
    }

    if (cases && cases.hasOwnProperty(prog)) {
      let func = cases[prog];
      if (typeof func === "function") {
        let start = new Date().getMilliseconds();
        let ans = func(null, debug);
        let end = new Date().getMilliseconds();

        if (ans) {
          console.log(ans);
        }

        console.log(`Execution time: ${end - start} ms`);
      } else {
        console.error(
          `Unable to find the entry point for the case ${prog}...\n`
        );
      }
    } else {
      console.error(`No matching case is founded for the case ${prog}...`);
    }

    console.log("\nAll is done...");
    return 0;
  }

  static parseCommand(cases: any): Command {
    let prog: string;
    let debugMode: boolean;

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
            if (p.indexOf(command) === 0) {
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

    return {
      prog,
      debug: debugMode
    };
  }
}

main.run();
