const bfs = function(set, score, cache) {
  if (!set || set.length === 0) {
    return 0;
  }

  if (set.length === 1) {
    return score + 1;
  }

  if (cache && cache[set.toString()]) {
    return cache[set.toString()];
  }

  let max = score;
  let pos = 0;

  while (pos < set.length) {
    let next = [...set];
    let skip = removeBoxes(next, pos);
    let newScore = score + skip * skip + bfs(next, score, cache);

    if (newScore > max) {
      max = newScore;
    }

    pos += skip;
  }

  cache[set.toString()] = max;
  return max;
};

const removeBoxes = function(source, pos) {
  let skip = 1;
  let index = pos + 1;

  while (index < source.length) {
    if (source[index] !== source[pos]) {
      break;
    }

    skip++;
    index++;
  }

  source.splice(pos, skip);
  return skip;
};

const run = function(set, debug) {
  let start = new Date().getMilliseconds();
  let ans = bfs(set, 0, {});
  let end = new Date().getMilliseconds();

  console.log(`Execution time: ${end - start}`);
  return ans;
};

module.exports = {
  run
};
