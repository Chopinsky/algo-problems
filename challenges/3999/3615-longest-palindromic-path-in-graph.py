'''
3615-longest-palindromic-path-in-graph
'''

from typing import List
from collections import defaultdict
from functools import cache


class Solution:
  def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
    g = defaultdict(list)
    for u, v in edges:
      g[u].append(v)
      g[v].append(u)

    nb = {}
    for u, lst in g.items():
      if u not in nb:
        nb[u] = {}

      for v in lst:
        ch = label[v]
        if ch not in nb[u]:
          nb[u][ch] = []

        nb[u][ch].append(v)

    @cache
    def dp(u, v, seen):
      if u > v:
        return dp(v, u, seen)

      curr = 1 if u == v else 2
      res = curr
      seen |= 1 << u
      seen |= 1 << v

      if u not in nb:
        return res

      for n1, lst in nb[u].items():
        if n1 not in nb[v]:
          continue

        for nxt1 in lst:
          for nxt2 in nb[v][n1]:
            if nxt1 == nxt2 or (seen & (1 << nxt1)) or (seen & (1 << nxt2)):
              continue

            res = max(res, curr + dp(nxt1, nxt2, seen))

      return res

    res = 0
    visited = set()

    for u in range(n):
      # odd length
      res = max(res, dp(u, u, 0))
      visited.add(u)

      # even length
      for v in g[u]:
        if v in visited:
          continue

        if label[u] == label[v]:
          res = max(res, dp(u, v, 0))

    return res
