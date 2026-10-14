'''
3693-climbing-stairs-ii
'''

from math import inf


class Solution:
  def climbStairs(self, n: int, costs: list[int]) -> int:
    c = [inf]*(n+1)
    c[0] = 0

    for i in range(1, n+1):
      base = costs[i-1]

      for d in range(1, 4):
        if i-d < 0:
          break

        c[i] = min(c[i], c[i-d]+base+d*d)

    return c[-1]
