'''
3558-number-of-ways-to-assign-edge-weights-i
'''

from collections import defaultdict
from typing import List


class Solution:
  def assignEdgeWeights(self, edges: List[List[int]]) -> int:
    mod = 10**9+7
    e = defaultdict(list)
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)

    d = defaultdict(list)

    def dfs(u: int, p: int, depth: int):
      d[depth].append(u)
      for v in e[u]:
        if v == p:
          continue

        dfs(v, u, depth+1)

    dfs(1, 0, 0)
    max_d = max(d.keys())
    c = 1
    # print('init:', max_d, d)

    for _ in range(max_d-1):
      c = (c << 1) % mod

    return c
        