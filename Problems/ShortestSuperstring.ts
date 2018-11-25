import { Problem, TestCase, TestCaseFactory } from "./Executor";

export class ShortestSuperstring implements Problem {
  solve(): void {}

  make(caseNum: number, debug: boolean): void {}

  genTestCase(caseNum: number): TestCase {
    return TestCaseFactory([], "");
  }
}
