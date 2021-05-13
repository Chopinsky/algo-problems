'''
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string s.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: s = "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

Example 2:
Input: s = "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]

Explanation:
0.0, 00, 0001 or 00.01 are not allowed.

Example 3:
Input: s = "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

Example 4:
Input: s = "(100)"
Output: [(10, 0)]

Explanation:
1.0 is not allowed.

Note:

4 <= s.length <= 12.
s[0] = "(", s[s.length - 1] = ")", and the other elements in s are digits.
'''

class Solution:
  def ambiguousCoordinates(self, s: str) -> List[str]:
    s = s[1:-1]
    # print(s)

    def check(seg: str) -> bool:
      if len(seg) < 1:
        return False

      if len(seg) == 1:
        return True

      if seg[0] == '0' and seg[-1] == '0':
        return False

      return True

    def generate(seg: str) -> List[str]:
      nums = []
      if len(seg) == 1 or seg[-1] == '0':
        nums.append(seg)
        return nums

      if seg[0] == '0':
        nums.append("{}.{}".format(seg[0], seg[1:]))
        return nums

      for i in range(len(seg)):
        if i > 0:
          nums.append("{}.{}".format(seg[:i], seg[i:]))
        else:
          nums.append(seg)

      return nums

    ans = []

    for i in range(1, len(s)):
      if check(s[:i]) and check(s[i:]):
        front = generate(s[:i])
        back = generate(s[i:])

        for f in front:
          for b in back:
            ans.append("({}, {})".format(f, b))

    # print(generate(s))

    return ans
