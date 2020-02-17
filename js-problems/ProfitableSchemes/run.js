const run = function(pSize, gSize, profit, group, debug) {
  let size = profit.length;
  let dp = init(pSize, gSize);
  let base = 1000000007;

  dp[0][0] = 1;

  if (debug) {
    console.log(dp);
  }

  // `k`: finishing k tasks at this state: since we always check k vs. k-1, downgrade this dimension.
  // `i`: achieve i profit at this state
  // `j`: using j people at tthis state
  let s = 0;
  while (s < size) {
    let p = profit[s];
    let g = group[s];

    for (let i = pSize; i >= 0; i--) {
      let ip = Math.min(pSize, i + p);

      for (let j = gSize - g; j >= 0; j--) {
        dp[ip][j + g] = (dp[ip][j + g] + dp[i][j]) % base;
      }
    }

    s++;
  }

  if (debug) {
    console.log(dp[pSize]);
  }

  let sum = 0;
  for (let g = 0; g < gSize + 1; g++) {
    sum += dp[pSize][g];
  }

  return sum;
};

const init = function(pSize, gSize) {
  let dp = [];
  for (let i = 0; i < pSize + 1; i++) {
    let base = [];
    for (let j = 0; j < gSize + 1; j++) {
      base.push(0);
    }

    dp.push(base);
  }

  return dp;
};

module.exports = {
  run
};
