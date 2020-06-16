'use strict';

const test = [1, 2, [4, 5, [7], 8], 9];

const calc = (arr, level) => {
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    if (typeof arr[i] === "number") {
      sum += arr[i];
    } else {
      sum += calc(arr[i], level + 1);
    }
  }

  return sum * level;
}

console.log(calc(test, 1));
