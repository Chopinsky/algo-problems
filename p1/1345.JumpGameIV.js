/**
 * @param {number[]} arr
 * @return {number}
 */
var minJumps = function(arr) {
  if (arr.length <= 1) {
    return 0;
  }

  if (arr.length == 2) {
    return 1;
  }

  const last = arr.length - 1;
  if (arr[0] === arr[last]) {
    return 1;
  }

  let ans = 0;
  let stack = [0];
  let val, pos, nextJumps, nextPos;

  const jumps = {};
  const visited = new Set();
  visited.add(0);

  for (let i = 0; i < arr.length; i++) {
    val = arr[i];

    if (jumps[val]) {
      jumps[val].push(i);
    } else {
      jumps[val] = [i];
    }
  }

  while (stack && stack.length > 0) {
    const next = [];

    for (let i = 0; i < stack.length; i++) {
      pos = stack[i];
      if (pos === last-1) {
        return ans + 1;
      }

      if (pos > 0 && !visited.has(pos-1)) {
        next.push(pos-1);
        visited.add(pos-1);
      }

      if (pos < last-1 && !visited.has(pos+1)) {
        if (pos === last-2) {
          return ans + 2;
        }

        next.push(pos+1);
        visited.add(pos+1);
      }

      val = arr[pos];
      nextJumps = jumps[val];

      for (let j = 0; j < nextJumps.length; j++) {
        nextPos = nextJumps[j];

        if (nextPos === last) {
          return ans + 1;
        }

        if (nextPos === last - 1) {
          return ans + 2;
        }

        if (visited.has(nextPos)) {
          continue;
        }

        next.push(nextPos);
        visited.add(nextPos);
      }
    }

    stack = next;
    ans++
  }

  return ans;
};