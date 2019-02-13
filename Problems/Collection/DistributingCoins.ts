import { Problem, TestCase, TestCaseFactory } from "../Executor";

export class DistributingCoins implements Problem {
  private data: number[];
  private len: number;
  private answer: number;
  private result: number;

  genTestCase(caseNum: number): TestCase {
    let data: number[];
    let result: number;

    switch (caseNum) {
      case 1:
        data = [0, 3, 0];
        result = 3;
        break;

      case 2:
        data = [1, 0, 2];
        result = 2;
        break;

      case 3:
        data = [1, 0, 0, 3];
        result = 4;
        break;

      default:
        data = [3, 0, 0];
        result = 2;
    }

    return TestCaseFactory(data, result);
  }

  make(caseNum: number, debug: boolean): void {
    let test = this.genTestCase(caseNum);
    this.data = test.data;
    this.len = this.data.length;
    this.result = test.target;
    this.answer = 0;
  }

  solve(): void {
    // upside-down balancing... overall net-flow is 0.
    this.balance(0);

    console.log(`Calculated steps: ${this.answer}`);
    console.log(`Expected steps: ${this.result}`);
  }

  private balance(node: number): number {
    if (node >= this.len) {
      return 0;
    }

    // pre-iterating the tree, stored in the form of a balanced tree
    let left = 2 * node + 1 < this.len ? this.balance(2 * node + 1) : 0;
    let right = 2 * node + 2 < this.len ? this.balance(2 * node + 2) : 0;

    // answer is the flow required from or to the left and right branches to balance the tree
    this.answer += Math.abs(left) + Math.abs(right);

    // return the net-flow through this node, which is what to give/ask for from the parent
    return this.data[node] - 1 + left + right;
  }
}
