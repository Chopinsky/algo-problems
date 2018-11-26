import { Problem, TestCase, TestCaseFactory } from "./Executor";

export class ShortestSuperstring implements Problem {
  private g: number[][];
  private testCase: TestCase;

  solve(): void {}

  make(caseNum: number, debug: boolean): void {
    this.testCase = this.genTestCase(caseNum);
    if (!this.testCase) {
      return;
    }

    let testData: string[] = this.testCase.data;
    let len: number = testData.length;
    this.g = new Array(len);

    for (let i = 0; i < len; i++) {
      this.g[i] = new Array(len);
      for (let j = 0; j < len; j++) {
        this.g[i][j] = this.calcOverlap(testData[i], testData[j]);
      }
    }

    console.log(this.g);
  }

  genTestCase(caseNum: number): TestCase {
    switch (caseNum) {
      case 1:
        return TestCaseFactory(
          ["alex", "loves", "leetcode"],
          "alexlovesleetcode"
        );

      default:
        return TestCaseFactory(
          ["catg", "ctaagt", "gcta", "ttca", "atgcatc"],
          "gctaagttcatgcatc"
        );
    }
  }

  calcOverlap(a: string, b: string): number {
    if (!a || a.length === 0 || !b || b.length === 0) {
      return 0;
    }

    let ans: number = 0;
    for (let i = 0; i < a.length && i < b.length; i++) {
      if (a.charAt(a.length - i - 1) === b.charAt(i)) {
        ans = i + 1;
      } else {
        break;
      }
    }

    return ans;
  }
}
