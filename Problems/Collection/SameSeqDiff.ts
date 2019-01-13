import { Problem, TestCase, TestCaseFactory } from "../Executor";

export class SameSeqDiff implements Problem {
  private n: number;
  private k: number;

  genTestCase(caseNum: number): TestCase {
    let data: any[];
    let result: any;

    switch (caseNum) {
      case 1:
        data = [2, 1];
        result = [
          10,
          12,
          21,
          23,
          32,
          34,
          43,
          45,
          54,
          56,
          65,
          67,
          76,
          78,
          87,
          89,
          98
        ];

      default:
        data = [3, 7];
        result = [181, 292, 707, 818, 929];
    }

    return TestCaseFactory(data, result);
  }

  make(caseNum: number, debug: boolean): void {
    let testCase = this.genTestCase(caseNum);
    this.n = testCase.data[0];
    this.k = testCase.data[1];
  }

  solve(): void {
    let ans: number[] = new Array();
    if (this.n === 1) {
      ans.push(0);
    }

    for (let i = 1; i <= 9; i++) {
      this.dfs(this.n - 1, i, ans);
    }

    console.log(ans);
  }

  private dfs(n: number, cur: number, ans: number[]) {
    if (n === 0) {
      ans.push(cur);
    }

    let l = cur % 10;
    if (l + this.k <= 9) {
      this.dfs(n - 1, cur * 10 + l + this.k, ans);
    }

    if (l - this.k >= 0 && this.k !== 0) {
      this.dfs(n - 1, cur * 10 + l - this.k, ans);
    }
  }
}
