/**
 * @param {string} s1
 * @param {number} n1
 * @param {string} s2
 * @param {number} n2
 * @return {number}
 */
var getMaxRepetitions = function (s1, n1, s2, n2) {
  if (n1 === 0) {
    return 0;
  }

  const idx = new Array(s2.length + 1).fill(0);
  const cnt = new Array(s2.length + 1).fill(0);

  // idx[0] = 0;
  // cnt[0] = 0;

  let ptr = 0, c = 0;

  for (let i = 0; i < n1; i++) {
    for (let j = 0; j < s1.length; j++) {
      if (s1[j] === s2[ptr]) {
        ptr++;
      }

      // reset ptr, as we're starting the 2nd iteration
      if (ptr === s2.length) {
        ptr = 0;
        c++;
      }
    }

    cnt[i] = c;
    idx[i] = ptr;

    for (let k = 0; k < i; k++) {
      if (idx[k] === ptr) {
        let pre = cnt[k];
        let curr = (cnt[i] - cnt[k]) * Math.floor((n1 - 1 - k) / (i - k));
        let rem = cnt[k + ((n1 - 1 - k) % (i - k))] - cnt[k];

        return Math.floor((pre + curr + rem) / n2);
      }
    }
  }

  return Math.floor(cnt[n1 - 1] / n2);
};

const ans = getMaxRepetitions("aaa", 20, "aaaaa", 1);
console.log(ans);
