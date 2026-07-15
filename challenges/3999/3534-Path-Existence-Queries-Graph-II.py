'''
3534-Path-Existence-Queries-Graph-II
'''

from typing import List
from functools import cache


class Solution:
  def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
    order = sorted(range(n), key=lambda i: nums[i])
    vals = [nums[i] for i in order]
    pos = [0] * n

    for i, idx in enumerate(order):
      pos[idx] = i

    comp = [0] * n
    cid = 0

    for i in range(1, n):
      if vals[i]-vals[i-1] > maxDiff:
        cid += 1
    
      comp[i] = cid

    nxt: List[int] = list(range(n))
    r = 0

    for l in range(n):
      while r+1 < n and vals[r+1]-vals[l] <= maxDiff:
        r += 1

      nxt[l] = r

    LOG = (n+1).bit_length()
    up = [nxt]
    
    for _ in range(1, LOG):
      prev = up[-1]
      up.append([prev[prev[i]] for i in range(n)])

    ans = []
    for u, v in queries:
      pu, pv = pos[u], pos[v]
      if pu == pv:
        ans.append(0)
        continue

      l, r = (pu, pv) if pu < pv else (pv, pu)
      if comp[l] != comp[r]:
        ans.append(-1)
        continue

      cur = l
      dist = 0

      for k in range(LOG - 1, -1, -1):
        if up[k][cur] < r:
          cur = up[k][cur]
          dist += 1 << k

      ans.append(dist+1)

    return ans

  def pathExistenceQueries0(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
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
