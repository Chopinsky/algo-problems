'''
3488-closest-equal-element-queries
'''

from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution:
  def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
    ans = []
    idx = defaultdict(list)
    n = len(nums)

    for i in range(n):
      idx[nums[i]].append(i)

    # print('init:', idx)
    for q in queries:
      val = nums[q]

      # no other idx
      if len(idx[val]) <= 1:
        ans.append(-1)
        continue

      cand = idx[val]
      pos = bisect_left(cand, q)
      m = len(cand)

      if 0 < pos < m-1:
        res = min(q-cand[pos-1], cand[pos+1]-q)
      elif pos == m-1:
        res = min(n-q+cand[0], q-cand[pos-1])
      else:
        res = min(cand[pos+1]-q, q+n-cand[-1])

      ans.append(res)

    return ans
        