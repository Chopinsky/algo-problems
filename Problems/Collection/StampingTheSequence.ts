import { Problem, TestCase, TestCaseFactory } from "../Executor";

export class StampingTheSequence implements Problem {
  private target: string[];
  private stamp: string[];
  private answer: number[];
  private debug: boolean;

  genTestCase(caseNum: number): TestCase {
    switch (caseNum) {
      case 1:
        return TestCaseFactory(["aabcaca", "abca"], [3, 0, 1]);

      case 2:
        return TestCaseFactory(["aaaaabc", "abc"], [0, 1, 2, 3, 4]);

      case 3:
        return TestCaseFactory(["eyeeye", "abc"], []);

      default:
        return TestCaseFactory(["ababc", "abc"], [0, 2]);
    }
  }

  make(caseNum: number, debug: boolean): void {
    let testCase = this.genTestCase(caseNum);

    this.debug = debug;
    this.target = testCase.data[0].split("");
    this.stamp = testCase.data[1].split("");
    this.answer = testCase.target;

    if (this.debug) {
      console.log(this.target);
      console.log(this.stamp);
    }
  }

  solve(): void {
    if (this.target.length < this.stamp.length) {
      console.log(`Target length must be longer than the stamp length`);
      return;
    }

    if (this.target.length === this.stamp.length && !this.matchFrom(0)) {
      console.log(`No match has been found`);
      return;
    }

    let result = this.run();

    if (this.validate(this.target)) {
      console.log(`Success! Index: [${result}]`);
      console.log(`Expected array: [${this.answer}]`);
    } else {
      console.log(`Unable to find the match!`);
    }
  }

  private matchFrom(start: number): boolean {
    if (this.stamp.length + start > this.target.length) {
      return false;
    }

    for (let i = 0; i < this.stamp.length; i++) {
      if (
        this.target[start + i] === "*" ||
        this.target[start + i] === this.stamp[i]
      ) {
        continue;
      } else {
        return false;
      }
    }

    return true;
  }

  private maskFrom(start: number): number {
    let count = 0;
    for (let i = 0; i < this.stamp.length; i++) {
      if (this.target[start + i] !== "*") {
        this.target[start + i] = "*";
        count++;
      }
    }

    return count;
  }

  private validate(result: string[]): boolean {
    for (let i = 0; i < result.length; i++) {
      if (result[i] !== "*") {
        return false;
      }
    }

    return true;
  }

  private run(): number[] {
    let start = this.target.length - this.stamp.length;
    let count = 0;
    let result = [];
    let masked = {};
    let toContinue = true;

    while (toContinue) {
      toContinue = false;

      for (let i = start; i >= 0; i--) {
        if (masked[i]) {
          continue;
        }

        if (this.matchFrom(i)) {
          count += this.maskFrom(i);
          result.push(i);
          masked[i] = true;
          toContinue = true;

          if (this.debug) {
            console.log(`Mask at ${i}: ${this.target} with ${count}`);
          }

          if (count === this.target.length) {
            return result.reverse();
          }
        }
      }
    }

    return [];
  }
}
