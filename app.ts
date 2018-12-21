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
    let caseNum: number;
    let debugMode: boolean = false;

    if (process.argv && process.argv.length > 2) {
      let params = process.argv.slice(2);

      for (const val of params) {
        let command = val.toLowerCase();

        if (command.indexOf("-d") >= 0 || command.indexOf("debug") >= 0) {
          debugMode = true;
          continue;
        }

        if (command.startsWith("case=")) {
          let num = parseInt(command.substring(5));
          if (num !== NaN && num >= 0) {
            caseNum = num;
          }

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
