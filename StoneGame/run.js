const game = function(piles, aScore, lScore, cache) {
  if (!piles || piles.length === 0) {
    return aScore > lScore;
  }

  if (piles.length % 2 !== 0) {
    console.error(
      `Illegal input: expecting piles array to be of even length, but getting: ${
        piles.length
      } piles...`
    );
    return false;
  }

  let key = piles.toString();
  if (cache && cache.hasOwnProperty(key)) {
    return cache[key];
  }

  if (piles.length === 2) {
    if (piles[0] > piles[1]) {
      aScore += piles[0];
      lScore += piles[1];
    } else {
      aScore += piles[1];
      lScore += piles[0];
    }

    cache[key] = aScore > lScore;
    return aScore > lScore;
  }

  let len = piles.length;
  let takeOne =
    game(piles.slice(2, len), aScore + piles[0], lScore + piles[1], cache) &&
    game(
      piles.slice(1, len - 1),
      aScore + piles[0],
      lScore + piles[len - 1],
      cache
    );

  if (takeOne) {
    cache[key] = true;
    return true;
  }

  let takeTwo =
    game(
      piles.slice(0, len - 2),
      aScore + piles[len - 1],
      lScore + piles[len - 2],
      cache
    ) &&
    game(
      piles.slice(1, len - 1),
      aScore + piles[len - 1],
      lScore + piles[0],
      cache
    );

  cache[key] = takeTwo;
  return takeTwo;
};

const gameAlt = function(piles, l, r, cache) {
  if (l === r) {
    return piles[l];
  }

  if (cache.hasOwnProperty(l) && cache[l].hasOwnProperty(r)) {
    return cache[l][r];
  }

  if (!cache.hasOwnProperty(l)) {
    cache[l] = {};
  }

  cache[l][r] = Math.max(
    piles[l] - gameAlt(piles, l + 1, r, cache),
    piles[r] - gameAlt(piles, l, r - 1, cache)
  );

  return cache[l][r];
};

const game2 = function(piles) {
  let dp = [];
  let len = piles.length;

  // init -- no longer needed if a 1D array
  for (let i = 0; i < len; i++) {
    dp[i] = 0;
  }

  // DP: `size` is the subarray p[i] ~ p[j]'s size, starting from minimum set of 2 piles,
  //            going up till size of len.
  //     `i` is the head index of the subarray.
  //     `j` is the tail index of the subarray.
  // We need to figure out the solution to the subarray problem, then work from bottom up.
  for (let size = 2; size <= len; size++) {
    for (let i = 0; i < len - size + 1; i++) {
      const j = i + size - 1;
      dp[i] = Math.max(piles[i] - dp[i + 1], piles[j] - dp[i]);
    }
  }

  return dp[0] > 0;
};

const run = function(test, debug) {
  //return game(test, 0, 0, {});

  //let score = gameAlt(test, 0, test.length - 1, {});
  //return score > 0;

  return game2(test);
};

module.exports = {
  run
};
