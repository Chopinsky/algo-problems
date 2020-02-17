const calcSpan = function(prices, debug) {
  if (!prices || prices.length === 0) {
    return null;
  }

  if (prices.length === 1) {
    return [1];
  }

  const ans = Array(prices.length);
  const temp = [];

  while (prices.length > 0) {
    let index = prices.length - 1;
    let base = prices.pop();
    let count = 1;

    while (prices.length > 0) {
      let last = prices.pop();
      temp.push(last);

      if (base >= last) {
        count++;
      } else {
        break;
      }
    }

    ans[index] = count;

    // add the elements back
    while (temp.length > 0) {
      prices.push(temp.pop());
    }
  }

  return ans;
};

const calcGreedy = function(prices, debug) {
  let ans = [1];
  let stack = [
    {
      val: prices[0],
      count: 1
    }
  ];

  for (let i = 1; i < prices.length; i++) {
    let count = 1;
    let last = null;

    while (stack.length > 0) {
      last = stack.pop();

      if (last && last.val < prices[i]) {
        count += last.count;
      } else {
        stack.push(last);
        break;
      }
    }

    ans.push(count);
    stack.push({
      val: prices[i],
      count
    });
  }

  return ans;
};

const run = function(prices, debug) {
  //calcSpan(prices, debug);
  return calcGreedy(prices, debug);
};

module.exports = {
  run
};
