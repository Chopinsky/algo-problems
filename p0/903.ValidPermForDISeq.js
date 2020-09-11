/**
 * @param {string} S
 * @return {number}
 */
var mod = 1000000007;

var numPermsDISequence = function (S) {
  let n = S.length;
  let dp = new Array(n + 1).fill(1);
  let dp2 = new Array(n);
  let curr;

  for (let i = 0; i < n; i++) {
    if (S[i] === 'I') {
      curr = 0;
      for (let j = 0; j < n - i; j++) {
        curr = (curr + dp[j]) % mod;
        dp2[j] = curr;
      }
    } else {
      curr = 0;
      for (let j = n - i - 1; j >= 0; j--) {
        curr = (curr + dp[j + 1]) % mod;
        dp2[j] = curr;
      }
    }

    // console.log(dp);
    dp = dp2.map(val => val);
  }

  return dp[0];
}

var numPermsDISequence1 = function (S) {
  let size = S.length + 1;
  if (size === 2) {
    return 1;
  }

  const base = new Array(size);
  for (let i = 0; i < size; i++) {
    base[i] = i;
  }

  let c = permut(base, 0, S, {});

  console.log(c);

  return c % mod;
};

var permut = function (arr, idx, word, mem) {
  if (idx === arr.length - 1) {
    return verify(arr, idx - 1, word) ? 1 : 0;
  }

  let count, s, l, k, sum = 0;

  for (let i = idx; i < arr.length; i++) {
    swap(arr, idx, i);

    if (verify(arr, idx - 1, word)) {
      // todo: check if we can read from the mem -->
      //       key = [starts with arr[idx], l smaller, r larger].join(","),
      s = 0;
      l = 0;

      for (let j = idx + 1; j < arr.length; j++) {
        if (arr[idx] < arr[j]) {
          l++;
        } else {
          s++;
        }
      }

      k = `${arr[idx]},${l},${s}`;
      if (mem[k]) {
        count = mem[k];
      } else {
        count = permut(arr, idx + 1, word, mem);
        mem[k] = count;
      }

      //todo: save counts ....

      sum += count;
    }

    swap(arr, i, idx);
  }

  return sum % mod;
}

var swap = function (arr, i, j) {
  const tmp = arr[i];
  arr[i] = arr[j];
  arr[j] = tmp;
}

var verify = function (arr, i, word) {
  if (i >= arr.length - 1 || i < 0) {
    return true;
  }

  if (word[i] === 'D') {
    return arr[i] > arr[i + 1];
  }

  if (word[i] === 'I') {
    return arr[i] < arr[i + 1];
  }

  return false;
}