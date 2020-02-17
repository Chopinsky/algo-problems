const find = function(arr) {
  if (!arr || arr.length < 2) {
    return 0;
  }

  const len = arr.length;
  const dp = build(len, len, 2);

  let max = 2;
  for (let k = 2; k < len; k++) {
    for (let j = 1; j < k; j++) {
      if (arr[k] - arr[j] === arr[k - j - 1]) {
        dp[j][k] = dp[k - j - 1][j] + 1;

        if (dp[j][k] > max) {
          max = dp[j][k];
        }
      }
    }
  }

  return max;
};

const build = function(x, y, val) {
  const dp = Array(x);

  for (let i = 0; i < x; i++) {
    dp[i] = Array(y);

    for (let j = 0; j < y; j++) {
      dp[i][j] = val;
    }
  }

  return dp;
};

exports.run = function(test, debug) {
  return find(test);
};
