import { Executor } from "./Problems/Executor";
import "./Utils/support";

interface Command {
  prog: string;
  caseNum: number;
  debug: boolean;
}

class main {
  public static run(): number {
    let { prog, caseNum, debug } = this.parseCommand();

    if (debug) {
      console.info("(Running in debug mode...)");
    }

    Executor.Run(prog, caseNum, debug);

    return 0;
  }

  static parseCommand(): Command {
    let prog: string;
    let caseNum: number = 2;
    let debugMode: boolean = false;

    if (process.argv && process.argv.length > 2) {
      let params = process.argv.slice(2);

      for (const val of params) {
        let command = val.toLowerCase();

        if (command === "-d" || command === "--debug") {
          debugMode = true;
          continue;
        }

        if (!prog) {
          for (const problem of Executor.ProblemKeys()) {
            if (problem.toLowerCase().startsWith(command)) {
              prog = problem;
              break;
            }
          }
        }
      }
    }

    if (!prog) {
      prog = "3SumWithMulti";
    }

    return {
      prog,
      caseNum,
      debug: debugMode
    };
  }
}

main.run();
