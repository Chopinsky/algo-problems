import { Problem, TestCase, TestCaseFactory } from "../Executor";

export class LargestCommonFactor implements Problem {
  private _factors: object = {};
  private _store: number[][] = new Array();
  private _dsu: number[];
  private _data: number[];
  private _answer: number[];

  genTestCase(caseNum: number): TestCase {
    switch (caseNum) {
      case 1:
        return TestCaseFactory([9, 20, 50, 63], 2);

      case 2:
        return TestCaseFactory([2, 3, 4, 6, 7, 12, 21, 39], 8);

      default:
        return TestCaseFactory([4, 6, 15, 35], 4);
    }
  }

  make(caseNum: number, debug: boolean): void {
    let testCase = this.genTestCase(caseNum);
    if (!testCase || !testCase.data) {
      console.error("Unable to generate test cases...");
      return;
    }

    this._data = testCase.data;
    this._answer = testCase.target;

    this._dsu = new Array(this._data.length);
    for (let i = 0; i < this._data.length; i++) {
      this._dsu[i] = i;
    }

    this._data
      .sort(
        (a: number, b: number): number => {
          return a - b;
        }
      )
      .forEach((val, idx) => {
        let factors = this.findFactors(val);

        if (factors.length > 0) {
          factors.forEach(factor => {
            if (!this._factors.hasOwnProperty(factor)) {
              this._factors[factor] = new Array();
            }

            this._factors[factor].push(idx);
          });
        }

        this._store.push(factors);
      });

    if (debug) {
      console.log(this._factors);
      console.log(this._store);
      console.log(this._dsu);
    }
  }

  solve(): void {
    // let dyes: number[] = new Array(this._data.length);
    // let group = 1;

    let ans = 1;
    let c = {};

    this._data.forEach(val => {
      let idx = this.dsuFind(val);
      if (!c.hasOwnProperty(idx)) {
        c[idx] = 0;
      }

      c[idx] += 1;
      ans = Math.max(ans, c[idx]);
    });

    console.log(`The answer is: ${ans}`);
    console.log(`Expected answer is: ${this._answer}`);
  }

  private findFactors(num: number, includeSelf: boolean = false): number[] {
    if (num <= 0) {
      return [];
    } else if (num === 1) {
      return [num];
    }

    let bound = Math.floor(Math.sqrt(num));
    let result = includeSelf ? [1, num] : [];

    for (let i = 2; i <= bound; i++) {
      if (num % i === 0) {
        result.push(i);
        this.dsuUnion(num, i);

        let pair = num / i;
        if (i !== pair) {
          result.push(pair);
          this.dsuUnion(num, pair);
        }
      }
    }

    return result.sort(
      (a: number, b: number): number => {
        return a - b;
      }
    );
  }

  private dsuFind(x: number): number {
    if (this._dsu[x] !== x) {
      this._dsu[x] = this.dsuFind(this._dsu[x]);
    }

    return this._dsu[x];
  }

  private dsuUnion(x: number, y: number) {
    this._dsu[this.dsuFind(x)] = this._dsu[this.dsuFind(y)];
  }
}
