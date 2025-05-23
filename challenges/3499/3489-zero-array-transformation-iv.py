'''
3489-zero-array-transformation-iv
'''

from typing import List


class Solution:
  def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
    if all(val == 0 for val in nums):
      return 0

    n = len(nums)
    m = len(queries)
    done = [val == 0 for val in nums]
    ds = [set([0]) for _ in range(n)]

    def apply(l: int, r: int, v0: int):
      for i in range(l, r+1):
        if done[i]:
          continue

        d = ds[i]
        nxt = set()
        for v1 in d:
          if v0+v1 > nums[i]:
            continue

          if v0+v1 == nums[i]:
            done[i] = True
            break

          nxt.add(v0+v1)

        ds[i] |= nxt

    for i in range(m):
      l, r, val = queries[i]
      apply(l, r, val)
      if all(v for v in done):
        return i+1

    return -1
        