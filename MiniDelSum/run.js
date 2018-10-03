const dp = {};

const find = function(s1, s2) {
  const key = s1 + "-" + s2;
  if (dp.hasOwnProperty(key)) {
    return dp[key];
  }

  if (!s1 && !s2) {
    dp[key] = 0;
    return 0;
  }

  const len1 = s1.length;
  const len2 = s2.length;

  if (!s1) {
    dp[key] = calcVal(s2);
  } else if (!s2) {
    dp[key] = calcVal(s1);
  } else {
    if (s1[len1 - 1] === s2[len2 - 1]) {
      dp[key] = find(s1.slice(0, len1 - 1), s2.slice(0, len2 - 1));
    } else {
      let ans1 = find(s1.slice(0, len1 - 1), s2) + s1.charCodeAt(len1 - 1);
      let ans2 = find(s1, s2.slice(0, len2 - 1)) + s2.charCodeAt(len2 - 1);
      dp[key] = ans1 > ans2 ? ans2 : ans1;
    }
  }

  return dp[key];
};

const calcVal = function(s) {
  if (!s) {
    return 0;
  }

  let ans = 0;
  for (let i = 0; i < s.length; i++) {
    ans += s.charCodeAt(i);
  }

  return ans;
};

exports.run = function(test, debug) {
  return find(test.s1, test.s2);
};
