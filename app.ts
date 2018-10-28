import { cases } from "./cases.js";

class main {
  public static run(): number {
    let prog: string = "";
    let debugMode: boolean = false;

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

    let x: number = 10;
    let y: number = 32;

    console.log("Hello World! The answer is: ", x + y);
    return 0;
  }
}

main.run();
