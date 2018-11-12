import { ThreeSumMulti } from "./3SumWithMulti";
import { KnightDialer } from "./KnightDialer";

export interface Problem {
  solve: () => void;
  make: (caseNum: number, debug: boolean) => void;
  genTestCase: (caseNum: number) => TestCase;
}

export interface TestCase {
  data: any[];
  target: any;
}

export function TestCaseFactory(data: any[], target: any): TestCase {
  return { data, target };
}

export const Problems: object = {
  "3SumWithMulti": ThreeSumMulti,
  KnightDialer: KnightDialer
};

export class Executor {
  static run(problem: string, caseNum: number, debug: boolean) {
    let prog: any = Problems[problem];
    if (!prog) {
      console.error(`Unable to run the problem...`);
      return;
    }

    let exec: Problem = new prog();
    if (exec) {
      console.log(`Running problem: ${problem}...\n`);

      exec.make(caseNum, debug);
      exec.solve();
    }
  }
}
