import { Problem, TestCase, TestCaseFactory } from "../Executor";

export class Subsets implements Problem {
  private debug: boolean;
  private nums: number[];
  private result: number[][];
  private ans: number[][];

  genTestCase(caseNum: number): TestCase {
    let data: any[];
    let result: any;

    switch (caseNum) {
      default:
        data = [1, 2, 3];
        result = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]];
    }

    return TestCaseFactory(data, result);
  }

  make(caseNum: number, debug: boolean): void {
    let testCase = this.genTestCase(caseNum);

    this.result = new Array();
    this.nums = testCase.data;
    this.ans = testCase.target;
  }

  solve(): void {
    for (let n = 0; n <= this.nums.length; n++) {
      this.dfs(n, 0, []);
    }

    this.print("Calculated results:", this.result);
    this.print("Expected results:", this.ans);
  }

  private dfs(size: number, start: number, curr: number[]) {
    if (curr.length === size) {
      this.result.push([...curr]);
      return;
    }

    for (let i = start; i < this.nums.length; i++) {
      curr.push(this.nums[i]);
      this.dfs(size, i + 1, curr);
      curr.pop();
    }
  }

  private print(title: string, ary: number[][] | null) {
    console.log(title);
    if (ary && ary.length > 0) {
      ary.forEach(ary => {
        console.log(ary);
      });
    }
    console.log("\n");
  }
}
