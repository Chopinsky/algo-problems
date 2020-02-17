import { Problem, TestCase, TestCaseFactory } from "../Executor";

export class UniquePaths implements Problem {
  private dp: number[][][];
  private map: number[][];
  private ans: number;
  private m: number;
  private n: number;

  genTestCase(caseNum: number): TestCase {
    let data: any[];
    let result: any;

    switch (caseNum) {
      case 1:
        data = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]];
        result = 4;

      default:
        data = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]];
        result = 2;
    }

    return TestCaseFactory(data, result);
  }

  make(caseNum: number, debug: boolean): void {
    let test = this.genTestCase(caseNum);
    this.map = test.data;
    this.ans = test.target;

    this.m = this.map.length;
    this.n = this.map[0].length;

    this.dp = new Array(this.m);
    let size = Math.pow(2, this.m * this.n);

    for (let i = 0; i < this.m; i++) {
      this.dp[i] = new Array(this.n);
      for (let j = 0; j < this.n; j++) {
        this.dp[i][j] = new Array(size);
      }
    }
  }

  solve(): void {
    let state = 0; // state is a series of 0s, each node in the map denotes to 1 bit in the state
    let sx = -1;
    let sy = -1;

    for (let y = 0; y < this.m; y++) {
      for (let x = 0; x < this.n; x++) {
        if (this.map[y][x] === 0 || this.map[y][x] === 2) {
          // if we need to visit this node, add it to the state -- the nodes waiting to be visited
          state += this.calcKey(x, y);
        } else if (this.map[y][x] === 1) {
          // starting point
          sx = x;
          sy = y;
        }
      }
    }

    let res = this.dfs(sx, sy, state);
    console.log(`The final count of possible paths are: ${res}`);
    console.log(`Expected count of possible paths are: ${this.ans}`);
  }

  private dfs(x: number, y: number, state: number) {
    if (!!this.dp[y][x][state]) {
      // if the path has already been calculated, return the result.
      return this.map[y][x][state];
    }

    if (this.map[y][x] === 2) {
      // if we reached the destination and all other possible paths are exhausted (meaning
      // there is no more unvisited nodes for this state), return the result;
      return state === 0;
    }

    let paths = 0;
    let dirs = [-1, 0, 1, 0, -1];

    for (let i = 0; i < 4; i++) {
      let tx = x + dirs[i];
      let ty = y + dirs[i + 1];

      if (
        tx < 0 ||
        tx === this.n ||
        ty < 0 ||
        ty === this.m ||
        this.map[ty][tx] === -1
      ) {
        continue;
      }

      // find out the bit pos of this node in the state
      let key = this.calcKey(tx, ty);
      if (!(state & key)) {
        // if the path has been visited already, continue
        continue;
      }

      // otherwise, mark the node as visited and then iterate
      paths += this.dfs(tx, ty, state ^ key);
    }

    // finally, visited all possible directions, store the paths back to the states (unvisited nodes)
    // from this node -- (x, y).
    this.dp[y][x][state] = paths;
    return this.dp[y][x][state];
  }

  private calcKey(x: number, y: number): number {
    // find the node position in the state series
    return Math.pow(2, y * this.n + x);
  }
}
