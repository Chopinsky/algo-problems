import { Problem, TestCase, TestCaseFactory } from "../Executor";

class PairQueue {
  private _queue: string[];
  private _store: object;
  private _count: number;

  constructor() {
    this._queue = [];
    this._store = {};
    this._count = 0;
  }

  insert(ops: number, target: number) {
    let key = `${ops},${target}`;
    if (this._store.hasOwnProperty(key)) {
      return;
    }

    this._queue.push(key);
    this._store[key] = true;
    this._count++;
  }

  remove(ops: number, target: number) {
    this.removeWithKey(`${ops},${target}`);
  }

  removeWithKey(key: string) {
    if (!key || !this._store.hasOwnProperty(key)) {
      return;
    }

    let index = this._queue.indexOf(key);
    this._queue.splice(index, 1);
    delete this._store[key];

    this._count--;
  }

  isEmpty(): boolean {
    return this._count === 0;
  }

  peek(): object {
    if (this._count === 0) {
      return null;
    }

    let raw = this._queue[0].split(",", 2);
    return {
      key: this._queue[0],
      ops: parseInt(raw[0]),
      target: parseInt(raw[1])
    };
  }
}

export class LeastOperators implements Problem {
  private target: number;
  private base: number;
  private answer: number;

  genTestCase(caseNum: number): TestCase {
    let data: any[];
    let result: any;

    switch (caseNum) {
      case 1:
        data = [3, 19];
        result = 5;

      case 2:
        data = [100, 1000000];
        result = 3;

      default:
        data = [5, 501];
        result = 8;
    }

    return TestCaseFactory(data, result);
  }

  make(caseNum: number, debug: boolean): void {
    let testCase = this.genTestCase(caseNum);
    this.base = testCase.data[0];
    this.target = testCase.data[1];
    this.answer = testCase.target;
  }

  solve(): void {
    let result = this.dijSearch();

    console.log(`Needed operatiors: ${result}`);
    console.log(`Expected operatiors: ${this.answer}`);
  }

  // running a Dijkstra graph, possible targets become nodes, and we maintain the counts as the
  // value of each nodes.
  private dijSearch(): number {
    let seen = {};
    let queue = new PairQueue();
    queue.insert(0, this.target);

    while (!queue.isEmpty()) {
      let head = queue.peek();
      let target = head["target"];
      let ops = head["ops"];

      queue.removeWithKey(head["key"]);

      if (target === 0) {
        return ops - 1;
      }

      if (seen.hasOwnProperty(target)) {
        continue;
      }

      seen[target] = true;
      let n = Math.floor(Math.log(target) / Math.log(this.base));

      // possible path 1: plus lower order
      let l = target - Math.pow(this.base, n);
      if (!seen.hasOwnProperty(l)) {
        queue.insert(ops + (n === 0 ? 2 : n), l);
      }

      // possible path 2: minus from higher order
      let r = Math.pow(this.base, n + 1) - target;
      if (!seen.hasOwnProperty(r)) {
        queue.insert(ops + n + 1, r);
      }
    }

    return -1;
  }
}
