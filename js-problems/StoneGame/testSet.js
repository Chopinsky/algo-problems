const getRandomNum = function(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
};

const generator = function(count, max, min) {
  let res = [];
  let sum = 0;

  while (count > 0) {
    count--;
    let num = getRandomNum(max, min);
    sum += num;
    res.push(num);
  }

  if (sum % 2 === 1) {
    return res;
  }

  return null;
};

module.exports = {
  set: generator(500, 500, 1)
};
