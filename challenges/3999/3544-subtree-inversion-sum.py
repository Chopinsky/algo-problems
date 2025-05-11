'''
3544-subtree-inversion-sum
'''

from typing import List
from functools import cache


class Solution:
  def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
    n = len(edges)+1
    p = [-1 for _ in range(n)]
    g = [[] for _ in range(n)]
    for u, v in edges:
      g[u].append(v)
      g[v].append(u)

    @cache
    def dfs(curr: int, last: int, flipped: bool) -> int:
      # not taking ops 
      res = -nums[curr] if flipped else nums[curr]

      # *if* taking ops here
      opp = -res

      for v in g[curr]:
        if v == p[curr]:
          continue

        p[v] = curr
        res += dfs(v, min(last+1, k), flipped)

        # allowed to take ops
        if last >= k:
          opp += dfs(v, 1, not flipped)

      return max(res, opp) if last >= k else res

    return dfs(0, k, False)
        