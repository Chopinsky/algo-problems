import { Problem, TestCase, TestCaseFactory } from "../Executor";
import DSU from "../../Utils/dsu";

export class RegionsCut implements Problem {
  private dsu: DSU;
  private debug: boolean;
  private grid: string[][];
  private ans: number;

  genTestCase(caseNum: number): TestCase {
    let data: any[];
    let result: any;

    switch (caseNum) {
      case 1:
        data = [];
        result = "";

      default:
        data = [[" ", "/"], ["/", " "]];
        result = 2;
    }

    return TestCaseFactory(data, result);
  }

  make(caseNum: number, debug: boolean): void {
    let test = this.genTestCase(caseNum);

    this.ans = test.target;
    this.grid = test.data;

    let len = this.grid.length;
    this.dsu = new DSU(4 * len * len);
    this.debug = debug;
  }

  solve(): void {
    let len = this.grid.length;

    // loop over cubics
    for (let c = 0; c < len; c++) {
      // loop over triangles
      for (let t = 0; t < len; t++) {
        let base = 4 * (c * len + t);
        switch (this.grid[c][t]) {
          case "/":
            this.dsu.merge(base + 0, base + 3);
            this.dsu.merge(base + 1, base + 2);
            break;

          case "\\":
            this.dsu.merge(base + 0, base + 1);
            this.dsu.merge(base + 2, base + 3);
            break;

          case " ":
            this.dsu.merge(base + 0, base + 1);
            this.dsu.merge(base + 1, base + 2);
            this.dsu.merge(base + 2, base + 3);
            break;

          default:
            break;
        }

        if (c + 1 < len) {
          // merge 2 and 0 from the cubic below
          this.dsu.merge(base + 2, base + 4 * len + 0);
        }

        if (t + 1 < len) {
          // merge 1 and 3 from the cubic to the right
          this.dsu.merge(base + 1, base + 4 + 3);
        }
      }
    }

    if (this.debug) {
      this.dsu.debug();
    }

    let ans = 0;
    for (let i = 0; i < 4 * len * len; i++) {
      if (this.debug) {
        console.log(`${i} -- ${this.dsu.find(i)}`);
      }

      if (this.dsu.find(i) === i) {
        ans++;
      }
    }

    console.log(`Result: ${ans}`);
    console.log(`Expected: ${this.ans}`);
  }
}
