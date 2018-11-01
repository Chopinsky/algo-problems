export interface Problem {
  runner: (testCase: any, debug: boolean) => void;
}

export const Cases: [string] = ["3SumWithMulti"];

export class Executor {
  static run(problem: string, debug: boolean) {
    switch (problem) {
      case "value":
        break;

      default:
        console.error(`No matching case is founded for the case ${problem}...`);
        break;
    }
  }
}
