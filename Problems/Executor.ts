import { ThreeSumMulti } from "./3SumWithMulti";

export interface Problem {
  solve: () => void;
  genTestCase: (caseNum: number) => TestCase;
}

export interface TestCase {
  data: any[];
  target: any;
}

export const Problems: [string] = ["3SumWithMulti"];

export class Executor {
  static run(problem: string, caseNum: number, debug: boolean) {
    let exec: Problem;

    switch (problem) {
      case "3SumWithMulti":
        exec = new ThreeSumMulti(caseNum, debug);
        break;

      default:
        break;
    }

    if (exec) {
      console.log(`Running problem: ${problem}...`);
      exec.solve();
    }
  }
}
