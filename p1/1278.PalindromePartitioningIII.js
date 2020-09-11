/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var palindromePartition = function (s, k) {
  const dp = Array(s.length);
  const dp2 = Array(s.length);

  for (let i = 0; i < s.length; i++) {
    dp[i] = Array(s.length).fill(-1);
    dp[i][i] = 0;

    dp2[i] = Array(k).fill(-1);
  }

  return palCheck(s, k, 0, s.length - 1, dp, dp2);
}

var palCheck = function (s, k, l, r, dp, dp2) {
  if (dp2[l][k] >= 0) {
    return dp2[l][k];
  }

  if (k === 1) {
    return getCount(s, l, r, dp);
  }

  let n = r - l + 1;
  if (n <= k) {
    return 0;
  }

  let best = -1;
  let lc, rc;

  for (let i = l; i <= r - k + 1; i++) {
    lc = getCount(s, l, i, dp);

    if (best > 0 && lc >= best) {
      continue;
    }

    rc = palCheck(s, k - 1, i + 1, r, dp, dp2);

    if (best < 0 || lc + rc < best) {
      best = lc + rc;
    }
  }

  dp2[l][k] = best;
  return best;
};

var getCount = function (s, l, r, dp) {
  if (dp[l][r] >= 0) {
    return dp[l][r];
  }

  dp[l][r] = countChanges(s, l, r);
  return dp[l][r];
}

var countChanges = function (s, l, r) {
  if (l === r) {
    return 0;
  }

  let count = 0;
  let mid = Math.floor((r - l - 1) / 2);

  for (let i = 0; i <= mid; i++) {
    if (s[l + i] !== s[r - i]) {
      count++;
    }
  }

  return count;
}

const str = "fyhowoxzyrincxivwarjuwxrwealesxsimsepjdqsstfggjnjhilvrwwytbgsqbpnwjaojfnmiqiqnyzijfmvekgakefjaxryyml";

const k = 32;

console.log(palindromePartition(str, k));
