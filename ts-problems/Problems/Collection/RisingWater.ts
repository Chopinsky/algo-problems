import { Problem, TestCase, TestCaseFactory } from "../Executor";

const makeNode = (): object => {
  return {
    val: Number.MAX_VALUE,
    visited: false
  };
};

export class RisingWater implements Problem {
  private data: number[][];
  private result: number;
  private debug: boolean;

  genTestCase(caseNum: number): TestCase {
    let data: any[];
    let result: any;

    switch (caseNum) {
      case 1:
        data = [
          [0, 1, 2, 3, 4],
          [24, 23, 22, 21, 5],
          [12, 13, 14, 15, 16],
          [11, 17, 18, 19, 20],
          [10, 9, 8, 7, 6]
        ];
        result = 16;
        break;

      default:
        data = [[0, 2], [1, 3]];
        result = 3;
    }

    return TestCaseFactory(data, result);
  }

  make(caseNum: number, debug: boolean): void {
    let test = this.genTestCase(caseNum);
    this.data = test.data;
    this.result = test.target;
    this.debug = debug;
  }

  solve(): void {
    let len = this.data.length;
    let dp = new Array(len);

    for (let i = 0; i < len; i++) {
      dp[i] = new Array(len);

      for (let j = 0; j < len; j++) {
        dp[i][j] = makeNode();
      }
    }

    let queue = [];
    let currX = 0;
    let currY = 0;

    dp[0][0].val = this.data[0][0];
    queue.push([0, 0]);

    while (queue.length > 0) {
      let node = queue.splice(0, 1);
      currX = node[0][0];
      currY = node[0][1];

      dp[currX][currY].visited = true;

      let currVal = dp[currX][currY].val;
      let neighbors = this.neighbors(currX, currY);

      neighbors.forEach(coord => {
        let x = coord[0];
        let y = coord[1];

        if (dp[x][y].val === Number.MAX_VALUE || currVal < dp[x][y].val) {
          // first visit or we have a better path
          dp[x][y].val = Math.max(currVal, this.data[x][y]);
          if (!this.isInQueue(queue, coord)) {
            queue.push(coord);
          }
        }
      });

      if (this.debug) {
        console.log(`======= ${[currX, currY]} =======`);
        for (let i = 0; i < len; i++) {
          let row = [];
          for (let j = 0; j < len; j++) {
            row.push(dp[i][j].val);
          }

          console.log(row);
        }
      }
    }

    console.log(`Final val: ${dp[len - 1][len - 1].val}`);
    console.log(`Expected val: ${this.result}`);
  }

  private neighbors(x: number, y: number): number[][] {
    let neighbors = [];
    let boundary = this.data.length;

    if (x > 0) {
      neighbors.push([x - 1, y]);
    }

    if (x < boundary - 1) {
      neighbors.push([x + 1, y]);
    }

    if (y > 0) {
      neighbors.push([x, y - 1]);
    }

    if (y < boundary - 1) {
      neighbors.push([x, y + 1]);
    }

    return neighbors;
  }

  private isInQueue(queue: number[][], coord: number[]): boolean {
    for (let i = 0; i < queue.length; i++) {
      if (queue[i][0] === coord[0] && queue[i][1] === coord[1]) {
        return true;
      }
    }

    return false;
  }
}
