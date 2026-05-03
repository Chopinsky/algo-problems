'''
3920-maximize-fixed-points-after-deletions
'''

from bisect import bisect_left


class Solution:
  def maxFixedPoints(self, nums: list[int]) -> int:
    lis = []
    cand = sorted([i-x, x] for i, x in enumerate(nums) if i >= x)

    for _, val in cand:
      idx = bisect_left(lis, val)
      if idx >= len(lis):
        lis.append(0)

      lis[idx] = val

    return len(lis)
        