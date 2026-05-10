'''
3924-minimum-threshold-path-with-limited-heavy-edges
'''

from typing import List
from collections import defaultdict
from heapq import heappush, heappop
import math


class Solution:
  def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
    if source == target:
      return 0

    e = defaultdict(list)
    low = math.inf
    high = -math.inf

    for u, v, w in edges:
      e[u].append((v, w))
      e[v].append((u, w))
      low = min(low, w)
      high = max(high, w)

    def path_exists(th: int) -> bool:
      count = {source: 0}
      q = [(0, source)]

      while q:
        s, u = heappop(q)

        # better solution exists
        if count[u] < s:
          continue

        for v, w in e[u]:
          nxt = s + (1 if w > th else 0)

          # can't reach v
          if nxt > k:
            continue

          # reached the target
          if v == target:
            return True

          # better solution exists
          if v in count and count[v] <= nxt:
            continue

          count[v] = nxt
          heappush(q, (nxt, v))

      return False

    # no path exists
    if not path_exists(high):
      return -1

    while low <= high:
      mid = (low + high) // 2
      if path_exists(mid):
        high = mid-1
      else:
        low = mid+1

    return low
  