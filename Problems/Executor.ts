import { Problems } from "./Problems";

export interface Problem {
  genTestCase: (caseNum: number) => TestCase;
  make: (caseNum: number, debug: boolean) => void;
  solve: () => void;
}

export interface TestCase {
  data: any[];
  target: any;
}

export function TestCaseFactory(data: any[], target: any): TestCase {
  return { data, target };
}

export class Executor {
  static Run(problem: string, caseNum: number = 0, debug: boolean = false) {
    let prog: Problem = Problems[problem];

    if (!prog) {
      console.error(`Unable to run the problem...`);
    } else {
      console.log(`Running problem: {${problem}}\n>>>>>>>\n`);

      prog.make(caseNum, debug);
      prog.solve();
    }
  }

  static ProblemKeys(): string[] {
    return Object.keys(Problems);
  }
}
