'use strict';

const testArr = [
  { val: "aaa", idx: 4, },
  { val: "aaa", idx: 10, },
  { val: "aaa", idx: 2, },
  { val: "aaa", idx: 0, },
];

const less = function (a, b) {
  return a.idx < b.idx;
}

const heap = require('./heap.js');
const h = heap(testArr, less);

h.push({ val: "bbb", idx: 3, });
h.push({ val: "bbb", idx: 7, });
h.push({ val: "bbb", idx: 1, });
h.push({ val: "bbb", idx: 9, });
h.push({ val: "bbb", idx: 5, });

console.log(h.pop());
console.log(h.pop());
console.log(h.pop());
console.log(h.pop());

h.push({ val: "ccc", idx: 2, });
h.push({ val: "ccc", idx: 0, });
h.push({ val: "ccc", idx: 1, });

console.log(h.toSortedArr());
