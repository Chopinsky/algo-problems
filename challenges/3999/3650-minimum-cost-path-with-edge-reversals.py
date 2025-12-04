'''
3650-minimum-cost-path-with-edge-reversals
'''


from typing import List
from heapq import heappop, heappush


class Solution:
  def minCost(self, n: int, edges: List[List[int]]) -> int:
    e = [[] for _ in range(n)]
    re = [[] for _ in range(n)]

    for u, v, w in edges:
      e[u].append((v, w))
      re[v].append((u, 2*w))

    cost = {}
    q = [(0, 0)]

    while q:
      c, u = heappop(q)
      if u == n-1:
        return c

      # print('iter:', u, c)
      if u not in cost or c < cost[u]:
        cost[u] = c
        for v, w in e[u]:
          heappush(q, (c+w, v))

        for v, w in re[u]:
          heappush(q, (c+w, v))

    return -1
    
        