'''
Write an API that generates fancy sequences using the append, addAll, and multAll operations.

Implement the Fancy class:

Fancy() Initializes the object with an empty sequence.
void append(val) Appends an integer val to the end of the sequence.
void addAll(inc) Increments all existing values in the sequence by an integer inc.
void multAll(m) Multiplies all existing values in the sequence by an integer m.
int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.

Example 1:

Input
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
Output
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

Explanation
Fancy fancy = new Fancy();
fancy.append(2);   // fancy sequence: [2]
fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
fancy.append(7);   // fancy sequence: [5, 7]
fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10);  // fancy sequence: [13, 17, 10]
fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20

Constraints:

1 <= val, inc, m <= 100
0 <= idx <= 105
At most 105 calls total will be made to append, addAll, multAll, and getIndex.
'''

mod = 10**9 + 7

class Fancy:
  def __init__(self):
    self._vals = []
    self._plus = [0]
    self._mult = [1]


  def append(self, val: int) -> None:
    self._vals.append(val)
    self._plus.append(self._plus[-1])
    self._mult.append(self._mult[-1])


  def addAll(self, inc: int) -> None:
    self._plus[-1] += inc


  def multAll(self, m: int) -> None:
    self._plus[-1] = (self._plus[-1] * m) % mod
    self._mult[-1] = (self._mult[-1] * m) % mod


  def getIndex(self, i: int) -> int:
    if i >= len(self._vals):
      return -1

    # inverse multi with mod: (1 / a) % mod is equivalent
    # to a ** (mod-2) % mod, as a math principle, hence
    # `(self._mult[-1] / self._mult[i]) % mod` is equivalent to
    # `self._mult[-1] * (self._mult[i] ** (mod-2) % mod)`
    m = self._mult[-1] * pow(self._mult[i], mod-2, mod)

    # the tail part of the sum: prevSum * m + tailSum == finalSum, hence
    # we shall take out the prevSum * m from finalSum to get the tail sum
    inc = self._plus[-1] - self._plus[i] * m

    return (self._vals[i] * m + inc) % mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)