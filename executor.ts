export interface Problem {
  runner: (testCase: [any], debug: boolean) => void;
  getTestCase: (caseNum: number) => [any];
}

export const Cases: [string] = ["3SumWithMulti"];

export class Executor {
  static run(problem: string, caseNum: number, debug: boolean) {
    const len: number = problem.length;

    Cases.forEach(val => {
      if (val.toLowerCase().substr(0, len) === problem) {
        const p: Problem = require(`./Problems/${val}.ts`);
        if (p) {
          console.log(`Running problem: ${problem}...`);

          const testCase: [any] = p.getTestCase(caseNum);
          p.runner(testCase, debug);
        }

        return;
      }
    });
  }
}
