'''
3636-threshold-majority-queries
'''

from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right


class Solution:
  def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    vals = defaultdict(list)
    for i, v in enumerate(nums):
      vals[v].append(i)

    cand = sorted((len(l), v) for v, l in vals.items())
    ans = []

    for l, r, th in queries:
      x = bisect_left(cand, (th, -1))
      if x >= len(cand):
        ans.append(-1)
        continue

      curr = (0, 0)
      for i in range(len(cand)-1, x-1, -1):
        cand_info = cand[i]
        if cand_info[0] < curr[0]:
          break

        i1 = bisect_right(vals[cand_info[1]], r)
        i2 = bisect_left(vals[cand_info[1]], l)
        diff = i1 - i2
        curr = max(curr, (diff, -cand_info[1]))

        if curr[0] > (r-l+1)//2:
          break

      if curr[0] >= th:
        ans.append(-curr[1])
      else:
        ans.append(-1)

    return ans
