'''
3275-k-th-nearest-obstacle-queries
'''

from typing import List
from heapq import heappush, heappushpop


class Solution:
  def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
    cand = []
    ans = []

    for x, y in queries:
      dist = abs(x) + abs(y)
      if len(cand) < k:
        heappush(cand, -dist)
      else:
        heappushpop(cand, -dist)

      if len(cand) < k:
        ans.append(-1)
      else:
        ans.append(-cand[0])

    return ans
        