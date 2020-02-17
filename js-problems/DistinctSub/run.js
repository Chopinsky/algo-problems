const solve = function(s, t, debug) {
  const sLen = s.length;
  const tLen = t.length;

  // sanity checks
  if (!sLen || !tLen || s.length < t.length) {
    return 0;
  }

  if (sLen === tLen) {
    return s === t ? 1 : 0;
  }

  // init
  const dp = new Array(tLen + 1);
  for (let i = 0; i < tLen + 1; i++) {
    dp[i] = new Array(sLen + 1);
  }

  for (let j = 0; j < sLen + 1; j++) {
    dp[0][j] = 1;
  }

  for (let i = 1; i < tLen + 1; i++) {
    dp[i][0] = 0;
  }

  // transitions: if s's j-th char matches t's i-th char, all possible matches are 1) matching on this char,
  //              or 2) skipping this match and look at the next one, and add these 2 cases together.
  for (let i = 1; i < tLen + 1; i++) {
    for (let j = 1; j < sLen + 1; j++) {
      if (t[i] === s[j]) {
        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1];
      } else {
        dp[i][j] = dp[i][j - 1];
      }
    }
  }

  return dp[tLen][sLen];
};

exports.run = function(test, debug) {
  return solve(test.s, test.t, debug);
};
