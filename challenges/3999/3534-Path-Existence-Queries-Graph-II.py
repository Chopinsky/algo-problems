'''
3534-Path-Existence-Queries-Graph-II
'''

from typing import List
from functools import cache


class Solution:
  def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
    for query in queries:
      if nums[query[0]] > nums[query[1]]:
        query[0], query[1] = query[1], query[0]
        
    pairs = [(nums[q[0]], nums[q[1]], i, q[0], q[1]) for i, q in enumerate(queries)]
    pairs.sort()

    nums.sort()
    big = max(nums)
    far = [i for i in range(big+1)]
    right = 0

    for val in nums:
      while right < n and nums[right]-val <= maxDiff:
        right += 1

      far[val] = nums[right-1]

    @cache
    def dfs(start: int, end: int):
      nxt = far[start]
      if nxt >= end:
        return 1

      # fail
      if nxt == start:
        return -1

      rest = dfs(nxt, end)
      if rest == -1:
        return -1

      return 1+rest

    ans = [0]*len(pairs)
    for start, end, idx, u, v in pairs:
      if u != v:
        ans[idx] = dfs(start, end)

    return ans
