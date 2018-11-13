import { Problem, TestCase, TestCaseFactory } from "./Executor";

export class Knapsack implements Problem {
  private _testCase: TestCase | null = null;
  private _debug: boolean = false;
  private _dp: number[][];

  solve(): void {
    if (!this._testCase) {
      console.error(`No test case is valid or provided...`);
      return;
    }

    let maxVal: number = 0;
    let maxWeight: number = this._testCase.data[2];
    let itemWeight: number[] = this._testCase.data[1];
    let itemVal: number[] = this._testCase.data[0];
    let itemLen: number = itemVal.length;

    for (let i = 1; i <= itemLen; i++) {
      let itemIndex: number = i - 1;

      for (let j = itemWeight[itemIndex]; j <= maxWeight; j++) {
        if (this._debug) {
          console.log(
            `dp[${i}][${j}] = ${this._dp[i - 1][j]} vs. ${this._dp[i - 1][
              j - itemWeight[itemIndex]
            ] + itemVal[itemIndex]}`
          );
        }

        this._dp[i][j] = Math.max(
          this._dp[i - 1][j],
          this._dp[i - 1][j - itemWeight[itemIndex]] + itemVal[itemIndex]
        );

        if (i === itemLen && this._dp[i][j] > maxVal) {
          maxVal = this._dp[i][j];
        }
      }
    }

    if (this._debug) {
      console.log("\n", this._dp, "\n");
    }

    console.log(
      `The largest amount of values that can be placed in the pack is ${maxVal}...\nExpected value is: ${
        this._testCase.target
      }...
      `
    );
  }

  make(caseNum: number, debug: boolean): void {
    this._testCase = this.genTestCase(caseNum);

    if (
      this._testCase.data.length !== 3 ||
      !this._testCase.data[0] ||
      !this._testCase.data[1] ||
      this._testCase.data[0].length !== this._testCase.data[1].length
    ) {
      console.error(
        `Invalid test data: the weight and value array must have the same length: ${
          this._testCase.data[0].length
        } vs. ${this._testCase.data[1].length}`
      );

      this._testCase = null;
      return;
    }

    let itemLen: number = this._testCase.data[0].length + 1;
    let weightLen: number = this._testCase.data[2] + 1;

    this._dp = new Array(itemLen);
    for (let i = 0; i < itemLen; i++) {
      this._dp[i] = new Array(weightLen);
      for (let j = 0; j < weightLen; j++) {
        this._dp[i][j] = 0;
      }
    }
  }

  genTestCase(caseNum: number): TestCase {
    switch (caseNum) {
      case 0:
      default:
        return TestCaseFactory([[1, 2, 4, 5], [1, 1, 2, 2], 4], 9);
    }
  }
}
