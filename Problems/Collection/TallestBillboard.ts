import { Problem, TestCase, TestCaseFactory } from "../Executor";

export class TallestBillboard implements Problem {
  genTestCase(caseNum: number): TestCase {
    let data: any[];
    let result: any;

    switch (caseNum) {
      case 1:
        data = [];
        result = "";

      default:
        data = [1, 2, 3, 6];
        result = 6;
    }

    return TestCaseFactory(data, result);
  }

  make(caseNum: number, debug: boolean): void {}

  solve(): void {}
}
