'''
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 20 + 30
3 = 21 + 30
4 = 20 + 31
5 = 21 + 31
7 = 22 + 31
9 = 23 + 30
10 = 20 + 32

Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]


Constraints:

1 <= x, y <= 100
0 <= bound <= 106
'''

class Solution:
  def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
    if bound < 2:
      return []

    ans = set()
    x, y = max(x, y), min(x, y)
    a = 1

    while a < bound:
      b = 1
      ans.add(a+b)

      while y > 1 and a+b*y <= bound:
        b *= y
        ans.add(a+b)

      if x <= 1:
        break

      a *= x

    res = []
    for i in ans:
      res.append(i)

    return res
