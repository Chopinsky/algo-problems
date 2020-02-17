import { Problem, TestCase, TestCaseFactory } from "../Executor";

export class ShortestBridges implements Problem {
  private debug: boolean = false;
  private queue: number[][] = new Array();
  private bridges: number[][];
  private result: number;

  solve(): void {
    let steps = this.findSteps();
    console.log(`Steps to connect all the islands: ${steps}`);
    console.log(`Expected steps: ${this.result}\n`);
  }

  make(caseNum: number, debug: boolean): void {
    let testCase: TestCase = this.genTestCase(caseNum);

    this.bridges = testCase.data;
    this.result = testCase.target;
    this.debug = debug;

    if (this.bridges.length === 0 || this.bridges[0].length === 0) {
      console.error(`Wrong data set size for ${this.bridges}`);
      return;
    }

    let found: boolean = false;

    for (let i = 0; i < this.bridges.length && !found; i++) {
      for (let j = 0; j < this.bridges[0].length && !found; j++) {
        if (this.bridges[i][j]) {
          this.dfs(j, i);
          found = true;
        }
      }
    }

    if (this.debug) {
      console.log(this.queue);
    }
  }

  genTestCase(caseNum: number): TestCase {
    switch (caseNum) {
      case 1:
        return TestCaseFactory(
          [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
          ],
          1
        );
      case 2:
        return TestCaseFactory([[0, 1, 0], [0, 0, 0], [0, 0, 1]], 2);
      default:
        return TestCaseFactory([[1, 0], [0, 1]], 1);
    }
  }

  private dfs(x, y: number): void {
    if (
      x < 0 ||
      y < 0 ||
      x >= this.bridges[0].length ||
      y >= this.bridges.length ||
      this.bridges[y][x] !== 1
    ) {
      return;
    }

    this.bridges[y][x] = 2;
    this.queue.push([x, y]);

    this.dfs(x - 1, y);
    this.dfs(x + 1, y);
    this.dfs(x, y - 1);
    this.dfs(x, y + 1);
  }

  private findSteps(): number {
    let steps: number = 0;
    let dirs: number[] = [0, 1, 0, -1, 0];

    while (this.queue.length > 0) {
      let len: number = this.queue.length;

      while (len > 0) {
        let x: number = this.queue[0][0];
        let y: number = this.queue[0][1];

        if (this.debug) {
          console.log(this.queue);
        }

        this.queue.splice(0, 1);
        len--;

        for (let i = 0; i < 4; i++) {
          let tx: number = x + dirs[i];
          let ty: number = y + dirs[i + 1];

          if (
            tx < 0 ||
            ty < 0 ||
            tx >= this.bridges[0].length ||
            ty >= this.bridges.length ||
            this.bridges[ty][tx] === 2
          ) {
            continue;
          }

          if (this.bridges[ty][tx] === 1) {
            return steps;
          }

          this.bridges[ty][tx] = 2;
          this.queue.push([ty, tx]);
        }
      }

      steps++;
    }

    return steps;
  }
}
