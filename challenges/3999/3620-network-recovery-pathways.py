'''
3620-network-recovery-pathways
'''

from typing import List
from heapq import heappush, heappop
import math


class Solution:
  def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
    n = len(online)

    def dijk(src: int, tgt: int, nb: List):
      dist = [math.inf]*n
      dist[src] = 0
      q = [(0, src)]

      while q:
        d, u = heappop(q)
        if d > dist[u]:
          continue

        if u == tgt:
          return d

        for v, w in nb[u]:
          if dist[v] > d+w:
            dist[v] = d+w
            heappush(q, (dist[v], v))

      return math.inf
    
    l, h = 0, 10**9+7
    best = -1

    while l <= h:
      mid = (l+h) // 2
      nb = [[] for _ in range(n)]

      # build allowed path graph given the min-edge cost
      # is `mid`
      for u, v, c in edges:
        if c >= mid and online[u] and online[v]:
          nb[u].append((v, c))

      # check if this min-cost is allowed
      dist = dijk(0, n-1, nb)
      if dist <= k:
        best = mid
        l = mid+1
      else:
        h = mid-1

    return best
          