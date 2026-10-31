'''
3970-shortest-path-with-at-most-k-consecutive-identical-characters
'''

from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
  def shortestPath(self, n: int, edges: List[List[int]], lbl: str, k: int) -> int:
    e = defaultdict(list)
    for u, v, w in edges:
      e[u].append((v, w))
        
    stack = [(0, 0, lbl[0], 1)]
    seen = {
      (0, lbl[0], 1): 0
    }

    while stack:
      w0, u, c0, cnt = heappop(stack)
      if u == n-1:
        return w0

      for v, w in e[u]:
        c1 = lbl[v]
        cnt1 = 1 + (cnt if c0 == c1 else 0)

        if cnt1 > k:
          # too many cons identical char
          continue

        w1 = w0+w
        if (v, c1, cnt1) in seen and w1 >= seen[v, c1, cnt1]:
          # visited
          continue

        # push to the stack
        seen[v, c1, cnt1] = w1
        heappush(stack, (w1, v, c1, cnt1))

    return -1
