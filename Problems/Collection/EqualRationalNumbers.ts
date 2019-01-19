import { Problem, TestCase, TestCaseFactory } from "../Executor";

const compare = (one: number, two: number): boolean => {
  return Math.abs(one - two) < Math.pow(10, -9);
};

export class EqualRationalNumbers implements Problem {
  private answer: boolean = false;
  private first: string;
  private second: string;

  genTestCase(caseNum: number): TestCase {
    let data: any[];
    let result: any;

    switch (caseNum) {
      case 1:
        data = ["0.1666(6)", "0.166(66)"];
        result = true;
        break;

      case 2:
        data = ["0.9(9)", "1.0"];
        result = true;
        break;

      default:
        data = ["0.(52)", "0.5(25)"];
        result = true;
        break;
    }

    return TestCaseFactory(data, result);
  }

  make(caseNum: number, debug: boolean): void {
    let testCase = this.genTestCase(caseNum);
    this.first = testCase.data[0];
    this.second = testCase.data[1];
    this.answer = testCase.target;
  }

  solve(): void {
    let f = this.parse(this.first);
    let s = this.parse(this.second);

    console.log(`First: ${f}; Second: ${s}`);
    console.log(`Result: ${compare(f, s)}`);
  }

  private parse(num: string): number {
    if (num.length === 0 || num === ".") {
      return 0;
    }

    let dot = num.indexOf(".");
    let rStart = num.indexOf("(");
    let rEnd = num.lastIndexOf(")");

    let i = 0;
    let n = 0;
    let nLen = 0;
    let r = 0;
    let rLen = 0;

    if (dot < 0) {
      return parseInt(num);
    } else if (dot === num.length - 1) {
      return parseInt(num.substring(0, num.length - 1));
    } else if (dot > 0) {
      i = parseInt(num.substring(0, dot));
    }

    if (rStart > dot + 1) {
      let nStr = num.substring(dot + 1, rStart);
      nLen = nStr.length;
      n = parseInt(nStr);
    }

    if (rEnd > rStart + 1) {
      let rStr = num.substring(rStart + 1, rEnd);
      rLen = rStr.length;
      r = parseInt(rStr);
    }

    let nFactor = n === 0 ? 0 : n / Math.pow(10, nLen);
    let rFactor =
      r === 0 ? 0 : r / Math.pow(10, nLen) / (Math.pow(10, rLen) - 1);

    return i + nFactor + rFactor;
  }
}
