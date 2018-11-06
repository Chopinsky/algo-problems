import { Problem, TestCase } from "./Executor";

export class ThreeSumMulti implements Problem {
  private _combSet: object = {
    largest: -1
  };
  private _testCase: TestCase;

  constructor(caseNum: number, private _debug: boolean) {
    this._testCase = this.genTestCase(caseNum);

    if (this._testCase.data) {
      this._testCase.data.forEach(val => {
        if (this._combSet[val]) {
          this._combSet[val] += 1;
        } else {
          this._combSet[val] = 1;
        }

        if (val > this._combSet["largest"]) {
          this._combSet["largest"] = val;
        }
      });
    }

    if (this._debug) {
      console.log(`Combo set -> ${this._combSet}`);
    }
  }

  solve(): void {
    let ans: number = 0;
    let target: number = this._testCase.target;

    for (let i = 0; i <= target; i++) {
      for (let j = i; j <= target; j++) {
        const k = target - i - j;
        if (k < 0 || k > this._combSet["largest"] || k < j) {
          // 0 <= i <= j <= k <= upper bound
          continue;
        }

        if (!this._combSet[i] || !this._combSet[j] || !this._combSet[k]) {
          // the number is not in the provided array
          continue;
        }

        if (i === j && j === k && this._combSet[i] >= 3) {
          // (1, j, k) where all 3 numbers are the same
          ans +=
            ((this._combSet[i] - 2) *
              (this._combSet[i] - 1) *
              this._combSet[i]) /
            6;
        } else if (i === j && j !== k && this._combSet[i] >= 2) {
          // (i, i, k)
          ans +=
            (this._combSet[i] * (this._combSet[i] - 1) * this._combSet[k]) / 2;
        } else if (i !== j && j === k && this._combSet[j] >= 2) {
          // (i, j, j)
          ans +=
            (this._combSet[i] * (this._combSet[j] - 1) * this._combSet[j]) / 2;
        } else {
          // (i, j, k) are all different numbers
          ans += this._combSet[i] * this._combSet[j] * this._combSet[k];
        }
      }
    }

    console.log(`Solved -- combinations are ${ans}`);
  }

  genTestCase(caseNum: number): TestCase {
    let data: number[] = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5];
    let target: number = 8;

    switch (caseNum) {
      case 0:
        break;
      case 1:
        data = [1, 1, 2, 2, 2, 2];
        target = 5;
        break;
      default:
        break;
    }

    return {
      data,
      target
    };
  }

  private comb = function(n: number, k: number): number {
    let key: string = `${n},${k}`;
    if (this._combSet[key]) {
      return this._combSet[key];
    }

    let top: number = n;
    for (let index = top - 1; index > n - k; index--) {
      top *= index;
    }

    let bottom: number = k;
    for (let index = k - 1; index > 0; index--) {
      bottom *= index;
    }

    this._combSet[key] = Math.floor(top / bottom);
    return this._combSet[key];
  };
}
