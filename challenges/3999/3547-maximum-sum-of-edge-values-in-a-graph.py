'''
3547-maximum-sum-of-edge-values-in-a-graph
'''

from collections import defaultdict, deque
from typing import List


class Solution:
  def maxScore(self, n: int, edges: List[List[int]]) -> int:
    g = defaultdict(list)
    for i, j in edges:
      g[i].append(j)
      g[j].append(i)

    seen = [False]*n
    cycles = []
    lines = []

    def find_all(i: int):
      nodes = [i]
      seen[i] = True

      for u in nodes:
        for v in g[u]:
          if not seen[v]:
            seen[v] = True
            nodes.append(v)

      return nodes

    def calc(l: int, r: int, is_cycle: int) -> int:
      d = deque((r, r))
      res = 0

      for v1 in range(r-1, l-1, -1):
        v0 = d.popleft()
        res += v0*v1
        d.append(v1)

      return res + d[0]*d[1]*is_cycle

    for i in range(n):
      if seen[i]:
        continue

      comp = find_all(i)
      if all(len(g[u]) == 2 for u in comp):
        cycles.append(len(comp))
      elif len(comp) > 1:
        lines.append(len(comp))

    res = 0
    lines = sorted(lines)[::-1]
    # print('init:', cycles, lines)

    for cnt in cycles:
      res += calc(n-cnt+1, n, 1)
      n -= cnt

    for cnt in lines:
      res += calc(n-cnt+1, n, 0)
      n -= cnt

    return res
    