/**
 * The rand7() API is already defined for you.
 * var rand7 = function() {}
 * @return {number} a random integer in the range 1 to 7
 */
var rand10 = function () {
  let r, c, idx = 99;

  while (idx > 40) {
    r = rand7();
    c = rand7();
    idx = c + (r - 1) * 7;
  }

  return 1 + (idx - 1) % 10;
};

var rand7 = function () {
  return Math.floor(Math.random() * 7) + 1;
}
