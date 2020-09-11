/**
 * @param {number[]} A
 * @return {number}
 */
var numberOfArithmeticSlices = function (a) {
  if (!a || a.length <= 2) {
    return 0;
  }

  let diff = a[1] - a[0], len = 2, ans = 0;

  for (let i = 2; i < a.length; i++) {
    if (a[i] - a[i - 1] === diff) {
      len++;
      ans += (len - 2);
    } else {
      diff = a[i] - a[i - 1];
      len = 2;
    }
  }

  return ans;
};

console.log(numberOfArithmeticSlices([1, 2, 3, 4]));
