'''
4003-minimum-cost-path-with-alternating-directions-iii
'''

from math import inf
from typing import List
from heapq import heappush, heappop


class Solution:
  def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
    d = [inf] * (m*n*2)
    q = [(1, 0, 0, 0)]

    while q:
      w, i, j, p = heappop(q)
      if (i, j) == (m-1, n-1):
        return w

      if w > d[(i*n+j)*2 + p]:
        continue

      k = (i*n+j)*2 + (p^1)
      if w + penalty[i][j] < d[k]:
        d[k] = w + penalty[i][j]
        heappush(q, [w + penalty[i][j], i, j, p^1])

      for dr, dc, rp in ((0,1,0), (1,0,0), (0,-1,1), (-1,0,1)):
        x, y = i+dr, j+dc
        if 0 <= x < m and 0 <= y < n:
          w2 = w + (x+1)*(y+1) + (0 if p == rp else penalty[i][j])
          k = (x*n+y)*2 + (p^1)
          if w2 < d[k]:
            d[k] = w2
            heappush(q, [w2, x, y, p^1])
        