const cache = {};

const breakDown = function(number) {
  if (number <= 0) {
    return null;
  }

  let digit = 0;
  let ans = [];

  while (number > 0) {
    digit = number % 10;
    ans.splice(0, 0, digit);

    number = Math.floor(number / 10);
  }

  return ans;
};

const count = function(digits, limit) {
  if (!digits || !Array.isArray(digits) || digits.length === 0 || limit <= 0) {
    return 0;
  }

  if (limit > 9) {
    return digits.length;
  }

  if (digits[0] > limit) {
    return 0;
  }

  if (digits[0] === limit) {
    return 1;
  }

  if (cache[limit]) {
    return cache[limit];
  }

  let left = 0;
  let right = digits.length;

  while (left < right) {
    let mid = left + Math.floor((right - left) / 2);

    if (digits[mid] <= limit) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  cache[limit] = left;
  return left;
};

const reduce = function(digits, numbers) {
  if (!digits || !numbers || !digits.length || !numbers.length) {
    return 0;
  }

  let ans = 0;
  let less = 0;

  for (let i = 0; i < digits.length; i++) {
    if (digits[i] >= numbers[0]) {
      break;
    }

    less++;
  }

  ans = less * Math.pow(digits.length, numbers.length - 1);
  if (debug) {
    console.log(`Count: ${less}, answer: ${ans}`);
  }

  let top = 1;
  for (let i = 0; i < numbers.length; i++) {
    let res = count(digits, numbers[i]);

    if (res === 0) {
      top = 0;
      break;
    }

    top *= res;
  }

  return ans + top;
};

exports.run = function(digits, limit, debug) {
  if (limit <= 0 || digits.length === 0) {
    return 0;
  }

  if (limit < 10) {
    return count(digits, limit);
  }

  let numbers = breakDown(limit);
  let base = numbers.length - 1;
  let ans = 0;

  while (base > 0) {
    ans += Math.pow(digits.length, base);
    base--;
  }

  let res = reduce(digits, numbers, debug);
  if (debug) {
    console.log(`Reduce result: ${res}`);
  }

  return ans + res;
};
