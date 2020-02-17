import { Problem, TestCase, TestCaseFactory } from "../Executor";

export class MinRefuelingStops implements Problem {
  genTestCase(caseNum: number): TestCase {
    return TestCaseFactory([], "");
  }

  make(caseNum: number, debug: boolean): void {}

  solve(): void {}
}
