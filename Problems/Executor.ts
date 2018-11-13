import { ThreeSumMulti } from "./3SumWithMulti";
import { KnightDialer } from "./KnightDialer";
import { Knapsack } from "./Knapsack";

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
  "3SumWithMulti": new ThreeSumMulti(),
  KnightDialer: new KnightDialer(),
  Knapsack: new Knapsack()
};

export class Executor {
  static run(problem: string, caseNum: number, debug: boolean) {
    let prog: Problem = Problems[problem];
    if (!prog) {
      console.error(`Unable to run the problem...`);
    } else {
      console.log(`Running problem: {${problem}}\n>>>>>>>\n`);

      prog.make(caseNum, debug);
      prog.solve();
    }
  }
}
