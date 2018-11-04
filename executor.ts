export interface Problem {
  runner: (testCase: any, debug: boolean) => void;
}

export const Cases: [string] = ["3SumWithMulti"];

export class Executor {
  static run(problem: string, debug: boolean) {
    const len: number = problem.length;

    Cases.forEach(val => {
      if (val.toLowerCase().substr(0, len) === problem) {
        const p = require(`./Problems/${val}.ts`);
        if (p) {
          console.log(`Running problem: ${problem}...`);
        }

        return;
      }
    });
  }
}
