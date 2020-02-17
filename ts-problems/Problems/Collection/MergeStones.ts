import { Problem, TestCase, TestCaseFactory } from "../Executor";

export class MergeStones implements Problem {
  private data: number[];
  private step: number;
  private result: number;
  private debug: boolean;

  genTestCase(caseNum: number): TestCase {
    let data: number[][];
    let result: number;

    switch (caseNum) {
      case 1:
        data = [[3, 2, 4, 1], [3]];
        result = -1;
        break;

      case 2:
        data = [[3, 5, 1, 2, 6], [3]];
        result = 25;
        break;

      default:
        data = [[3, 2, 4, 1], [2]];
        result = 20;
    }

    return TestCaseFactory(data, result);
  }

  make(caseNum: number, debug: boolean): void {
    let test = this.genTestCase(caseNum);
    this.data = test.data[0];
    this.step = test.data[1][0];
    this.result = test.target;
    this.debug = debug;
  }

  solve(): void {
    let answer = this.merge();
    console.log(`Calculated result: ${answer}`);
    console.log(`Expected result: ${this.result}`);
  }

  private merge(): number {
    if ((this.data.length - 1) % (this.step - 1) !== 0) {
      return -1;
    }

    let total = 0;
    while (this.data.length >= this.step) {
      let sum = this.data
        .slice(0, this.step)
        .reduce((sum, curr) => sum + curr, 0);

      let min = sum;
      let pos = [0];

      for (let i = this.step; i < this.data.length; i++) {
        // use sliding window to find the smallest consecutive-k subarray
        sum = sum + this.data[i] - this.data[i - this.step];

        if (this.debug) {
          console.log(
            `${this.data} with ${min}, @ ${i} = ${sum} (+${
              this.data[this.step]
            } - ${this.data[i - this.step]})`
          );
        }

        if (sum < min) {
          pos = [i - this.step + 1];
          min = sum;
        } else if (sum === min) {
          pos.push(i - this.step + 1);
        }
      }

      // combine all the non-overlapping steps
      for (let j = pos.length - 1; j >= 0; j--) {
        if (j === pos.length - 1 || pos[j] + this.step <= pos[j + 1]) {
          total += this.updateDataArray(pos[j]);
        }
      }
    }

    if (this.data.length === 1) {
      return total;
    } else {
      return -1;
    }
  }

  private updateDataArray(index: number) {
    let elem = this.data
      .slice(index, index + this.step)
      .reduce((sum, curr) => sum + curr, 0);

    this.data = [
      ...this.data.slice(0, index),
      elem,
      ...this.data.slice(index + this.step)
    ];

    if (this.debug) {
      console.log(`Index: ${index}, Length: ${this.data}`);
    }

    return elem;
  }
}
