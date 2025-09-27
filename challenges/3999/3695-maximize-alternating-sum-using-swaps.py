'''
3695-maximize-alternating-sum-using-swaps
'''

from typing import List
from collections import defaultdict


class Solution:
  def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
    n = len(nums)
    g = [i for i in range(n)]

    if not swaps:
      v0 = sum(nums[x] for x in range(0, n, 2))
      v1 = sum(nums[x] for x in range(1, n, 2))
      return v0-v1

    def find(x: int) -> int:
      while g[x] != x:
        x = g[x]

      return x

    def union(x: int, y: int):
      rx = find(x)
      ry = find(y)

      if rx <= ry:
        g[ry] = rx
      else:
        g[rx] = ry

    for x, y in swaps:
      union(x, y)

    vals = defaultdict(list)
    idx = defaultdict(int)

    for x in range(n):
      root = find(x)
      val = nums[x]
      vals[root].append(val)
      if x%2 == 0:
        idx[root] += 1

    res = 0
    # print('done:', vals, idx)

    for r, v in vals.items():
      v.sort()
      while v:
        val = v.pop()
        if idx[r] > 0:
          res += val
          idx[r] -= 1
        else:
          res -= val

    return res

