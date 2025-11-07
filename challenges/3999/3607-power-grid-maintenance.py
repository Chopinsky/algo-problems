'''
3607-power-grid-maintenance
'''

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
  def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
    offline = set()
    grid = [i for i in range(c+1)]

    def find(x: int) -> int:
      if grid[x] != x:
        grid[x] = find(grid[x])

      return grid[x]

    def union(x: int, y: int) -> int:
      rx, ry = find(x), find(y)
      if rx < ry:
        grid[ry] = rx
      else:
        grid[rx] = ry

    for x, y in connections:
      union(x, y)

    groups = defaultdict(list)
    for x in range(1, c+1):
      base = find(x)
      heappush(groups[base], x)

    ans = []

    for tp, x in queries:
      if tp == 2:
        offline.add(x)
        continue

      # resolve by itself
      if x not in offline:
        ans.append(x)
        continue

      # find the station that can resolve this station
      base = find(x)
      # print('iter:', x, base)

      while groups[base] and groups[base][0] in offline:
        heappop(groups[base])

      if not groups[base]:
        ans.append(-1)
      else:
        ans.append(groups[base][0])

    return ans

        

