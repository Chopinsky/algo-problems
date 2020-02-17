import { Problem, TestCase, TestCaseFactory } from "../Executor";

const ROW: number = 4;
const COLUMN: number = 3;

const boardMap: number[][][] = [
  [[1, 0], [1, 2]],
  [[1, 2], [2, 1]],
  [[2, 0], [2, 2]],
  [[1, 0], [2, 1]],
  [[0, 2], [2, 2], [3, 1]],
  [],
  [[0, 0], [2, 0], [3, 1]],
  [[0, 1], [1, 2]],
  [[0, 0], [0, 2]],
  [[0, 1], [1, 0]]
];

export class KnightDialer implements Problem {
  private _testCase: TestCase;
  private _debug: boolean;

  make(caseNum: number, debug: boolean) {
    this._testCase = this.genTestCase(caseNum);
    this._debug = debug;
  }

  solve(): void {
    let steps: number = this._testCase.data[0];
    if (steps <= 0) {
      console.error(
        `Unable to initialize the DP array: expecting more than 1 step, but get ${steps}`
      );
    }

    let dp: number[][][] | null = this.initAry(steps);
    if (dp === null || dp.length === 0) {
      console.error(
        `Unable to initialize the DP array: expecting more than 1 step, but get ${steps}`
      );
    }

    for (let k = 1; k < steps; k++) {
      for (let i = 0; i < ROW; i++) {
        for (let j = 0; j < COLUMN; j++) {
          dp[k][i][j] = 0;
          let lastMoves: number[][] = this.lastMoves(i, j);

          if (lastMoves && lastMoves.length > 0) {
            lastMoves.forEach(board => {
              let lastMove: number | undefined = dp[k - 1][board[0]][board[1]];
              dp[k][i][j] += typeof lastMove === "number" ? lastMove : 0;
            });
          }
        }
      }
    }

    let ans: number = 0;
    dp[steps - 1].forEach(board => {
      if (Array.isArray(board) && board.length > 0) {
        board.forEach(count => {
          ans += count;
        });
      }
    });

    console.log(`Unique numbers are: ${ans}`);
    console.log(`Expected numbers are: ${this._testCase.target}`);
  }

  genTestCase(caseNum: number): TestCase {
    switch (caseNum) {
      case 1:
        return TestCaseFactory([2], 20);
      case 2:
        return TestCaseFactory([3], 46);
      default:
        return TestCaseFactory([1], 10);
    }
  }

  private initAry(steps: number): number[][][] | null {
    if (steps <= 0) {
      return null;
    }

    let dp: number[][][] = new Array(steps);

    for (let k = 0; k < steps; k++) {
      dp[k] = new Array(ROW);
      for (let i = 0; i < ROW; i++) {
        dp[k][i] = new Array(COLUMN);

        if (k === 0) {
          for (let j = 0; j < COLUMN; j++) {
            if (i === 3 && (j === 0 || j === 2)) {
              dp[0][i][j] = 0;
            } else {
              dp[0][i][j] = 1;
            }
          }
        }
      }
    }

    return dp;
  }

  private lastMoves(row, column: number): number[][] {
    let num: number | undefined = this.boardToNum(row, column);
    if (num === undefined) {
      return [];
    }

    return boardMap[num];
  }

  private boardToNum(row, column: number): number | undefined {
    if (row >= ROW || column >= COLUMN) {
      return undefined;
    }

    if (row === 3) {
      if (column === 1) {
        return 0;
      } else {
        return undefined;
      }
    }

    return row * 3 + column + 1;
  }
}
