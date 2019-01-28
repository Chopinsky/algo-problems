import { Problem, TestCase, TestCaseFactory } from "../Executor";

export class OddEvenJump implements Problem {
  private data: number[];
  private ans: number;

  genTestCase(caseNum: number): TestCase {
    let data: any[];
    let result: any;

    switch (caseNum) {
      case 1:
        data = [2, 3, 1, 1, 4];
        result = 3;
        break;

      case 2:
        data = [5, 1, 3, 4, 2];
        result = 3;
        break;

      default:
        data = [10, 13, 12, 14, 15];
        result = 2;
    }

    return TestCaseFactory(data, result);
  }

  make(caseNum: number, debug: boolean): void {
    let test = this.genTestCase(caseNum);
    this.data = test.data;
    this.ans = test.target;
  }

  solve(): void {
    let dp = new Array(this.data.length);
    let map = {};
    let len = this.data.length;
    let res = 1;

    map[this.data[len - 1]] = len - 1;

    for (let i = 0; i < len; i++) {
      if (i === len - 1) {
        dp[i] = [1, 1];
      } else {
        dp[i] = [0, 0];
      }
    }

    for (let i = len - 2; i >= 0; i--) {
      let keys: number[] = Object.keys(map).map(val => parseInt(val));
      let val: number = this.data[i];
      let upper: number = Number.MAX_VALUE;
      let lower: number = Number.MIN_VALUE;

      for (let j = 0; j < keys.length; j++) {
        if (keys[j] > lower && keys[j] < val) {
          lower = keys[j];
        } else if (keys[j] < upper && keys[j] >= val) {
          upper = keys[j];
        }
      }

      if (lower > Number.MIN_VALUE) {
        let lower_index = map[lower];
        dp[i][1] = dp[lower_index][0];
      }

      if (upper < Number.MAX_VALUE) {
        let upper_index = map[upper];
        dp[i][0] = dp[upper_index][1];

        if (dp[i][0] === 1) {
          res++;
        }
      }

      map[this.data[i]] = i;
    }

    console.log(`Possible routes: ${res}`);
    console.log(`Expected routes: ${this.ans}`);
  }
}
