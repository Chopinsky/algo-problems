/**
 * @param {number[]} A
 * @return {number}
 */
var numberOfArithmeticSlices = function (a) {
  const n = a.length;

  if (n <= 2) {
    return 0;
  }

  // dp[i][d] == number of sequences ending with `a[i]` and has
  // difference of `d`
  const dp = {};
  let d, ans = 0, pre, curr;

  for (let i = 0; i < n; i++) {
    dp[i] = {};

    for (let j = 0; j < i; j++) {
      d = a[i] - a[j];

      pre = dp[j][d] || 0;    // seq count until a[j] with diff of d
      curr = dp[i][d] || 0;   // count from other a[j] with diff of d

      dp[i][d] = curr + pre + 1; // adding 1, i.e. the (i, j) pair, to the candidates count, because this pair will be lifted to a new subsequence once a later sequence with diff of `d` is found.

      ans += pre;
    }
  }

  // console.log(dp);

  return ans;
};

console.log(numberOfArithmeticSlices([2,4,6,8,10]));
