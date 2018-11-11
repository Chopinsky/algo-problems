import { ThreeSumMulti } from "./3SumWithMulti";
import { KnightDialer } from "./KnightDialer";

export interface Problem {
  solve: () => void;
  genTestCase: (caseNum: number) => TestCase;
}

export interface TestCase {
  data: any[];
  target: any;
}

export function TestCaseFactory(data: any[], target: any): TestCase {
  return { data, target };
}

export const Problems: string[] = ["3SumWithMulti", "KnightDialer"];

export class Executor {
  static run(problem: string, caseNum: number, debug: boolean) {
    let exec: Problem;

    switch (problem) {
      case "3SumWithMulti":
        exec = new ThreeSumMulti(caseNum, debug);
        break;

      case "KnightDialer":
        exec = new KnightDialer(caseNum, debug);
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
