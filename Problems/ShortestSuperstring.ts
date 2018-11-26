import { Problem, TestCase, TestCaseFactory } from "./Executor";

interface BFSResult {
  ary: number[];
  score: number;
}

const BFSResultSpread = (result: BFSResult) => {
  return {
    ary: [...result.ary],
    score: result.score
  };
};

export class ShortestSuperstring implements Problem {
  private debug: boolean;
  private g: number[][];
  private dataSet: string[];
  private answer: string;

  solve(): void {
    let ans: BFSResult = {
      ary: undefined,
      score: Infinity
    };

    let len = this.dataSet.length;
    for (let i = 0; i < len; i++) {
      let temp = this.bfs(
        i,
        i,
        {
          ary: [],
          score: 0
        },
        new Array(len)
      );

      if (this.debug) {
        console.log(temp);
      }

      if (temp.score < ans.score) {
        ans = temp;
      }
    }

    if (this.debug) {
      console.log(ans);
    }

    //todo: create the parsed string...
    let result = this.dataSet[ans.ary[0]];
    for (let i = 1; i < ans.ary.length; i++) {
      let parentIndex = ans.ary[i - 1];
      let index = ans.ary[i];
      let word = this.dataSet[index];

      result += word.substring(word.length - this.g[parentIndex][index]);
    }

    console.log(`
      Answer:   ${result} (length: ${result.length})
      Expected: ${this.answer} (length: ${this.answer.length})
    `);
  }

  make(caseNum: number, debug: boolean): void {
    let testCase = this.genTestCase(caseNum);
    if (!testCase || !testCase.data) {
      return;
    }

    this.dataSet = testCase.data;
    this.answer = testCase.target;
    this.debug = debug;

    let len: number = this.dataSet.length;
    this.g = new Array(len);

    for (let i = 0; i < len; i++) {
      this.g[i] = new Array(len);
      for (let j = 0; j < len; j++) {
        this.g[i][j] =
          i === j
            ? this.dataSet[i].length
            : this.calcOverlap(this.dataSet[i], this.dataSet[j]);
      }
    }

    if (this.debug) {
      console.log(this.g);
    }
  }

  genTestCase(caseNum: number): TestCase {
    switch (caseNum) {
      case 1:
        return TestCaseFactory(
          ["alex", "loves", "leetcode"],
          "alexlovesleetcode"
        );

      case 2:
        return TestCaseFactory(["ads", "bad", "dsg", "gg"], "badsgg");

      default:
        return TestCaseFactory(
          ["catg", "ctaagt", "gcta", "ttca", "atgcatc"],
          "gctaagttcatgcatc"
        );
    }
  }

  private calcOverlap(a: string, b: string): number {
    if (!a || a.length === 0 || !b || b.length === 0) {
      return 0;
    }

    let ans: number = b.length;
    let head = a.length >= b.length ? a.length - b.length : 0;
    let len = a.length - head;

    for (let i = head; i < a.length; i++) {
      if (a.substring(i) === b.substr(0, len)) {
        return b.length - len;
      }

      len--;
    }

    return ans;
  }

  private bfs(
    parent: number,
    node: number,
    result: BFSResult,
    visited: boolean[]
  ): BFSResult {
    if (visited[node] === true) {
      return result;
    }

    result.score += this.g[parent][node];
    result.ary.push(node);
    visited[node] = true;

    let ans: BFSResult = result;
    let minScore = Infinity;

    for (let i = 0; i < this.dataSet.length; i++) {
      if (!visited[i]) {
        let temp = this.bfs(node, i, BFSResultSpread(result), [...visited]);
        if (temp.score < minScore) {
          ans = temp;
          minScore = temp.score;
        }
      }
    }

    return ans;
  }
}
