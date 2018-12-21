import { Problem, TestCase, TestCaseFactory } from "../Executor";
import { copyFile } from "fs";

export class TallestBillboard implements Problem {
  private rods: number[];
  private ans: number;
  private debug: boolean;
  private sum: number;
  private dp: number[];

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

  make(caseNum: number, debug: boolean): void {
    const testCase = this.genTestCase(caseNum);
    if (testCase) {
      this.rods = testCase.data.sort((a: number, b: number) => a - b);
      this.ans = testCase.target;
    }

    this.debug = debug;

    if (this.rods && this.rods.length > 0) {
      this.sum = this.rods.reduce((sum, curr) => {
        return sum + curr;
      }, 0);

      this.dp = new Array(this.sum + 1);
      for (let i = 0; i < this.dp.length; i++) {
        this.dp[i] = i === 0 ? 0 : -1;
      }

      if (this.debug) {
        console.log(`Rods: ${this.rods}`);
      }
    }
  }

  solve(): void {
    const rows = this.rods.length;
    for (let i = 0; i < rows; i++) {
      const curr = this.dp.map(val => val);
      const rod = this.rods[i];

      for (let j = 0; j <= this.sum - rod; j++) {
        if (curr[j] < 0) {
          continue;
        }

        const idxAdd = j + rod;
        const idxMinus = Math.abs(j - rod);

        this.dp[idxAdd] = Math.max(this.dp[idxAdd], curr[j]);
        this.dp[idxMinus] = Math.max(
          this.dp[idxMinus],
          curr[j] + Math.min(rod, j)
        );
      }
    }

    console.log(`Answer: ${this.dp[0]}`);
  }
}
