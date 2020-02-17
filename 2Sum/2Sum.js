const calc = function(arr, debug) {
  if (!arr || arr.length === 0) {
    return 0;
  }

  if (arr.length === 1) {
    return arr[0];
  }

  let max = arr[0];
  let ans = [arr[0]];
  let loc = [0, 0];

  for (let i = 1; i < arr.length; i++) {
    ans.push(0);

    ans = ans.map((val, j) => {
      let temp = val + arr[i];
      if (temp > max) {
        max = temp;
        loc = [j, i];
      }

      return temp;
    });

    if (debug) {
      console.log(`${i}:`, ans);
    }
  }

  if (debug) {
    console.log(loc);
  }

  return {
    max,
    subarray: arr.slice(loc[0], loc[1] + 1)
  };
};

module.exports = {
  calc
};
