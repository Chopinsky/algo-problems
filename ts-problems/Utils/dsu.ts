export default class DSU {
  private dsu: number[];

  constructor(count: number = 1) {
    this.dsu = new Array(count);
    for (let i = 0; i < count; i++) {
      this.dsu[i] = i;
    }
  }

  find(x: number): number {
    if (this.dsu[x] !== x) {
      this.dsu[x] = this.find(this.dsu[x]);
    }

    return this.dsu[x];
  }

  union(x: number, y: number) {
    this.dsu[this.find(x)] = this.dsu[this.find(y)];
  }

  merge(x: number, y: number) {
    this.dsu[this.find(x)] = this.find(y);
  }

  debug() {
    console.log(this.dsu);
  }
}
