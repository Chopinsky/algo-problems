'''
3310-remove-methods-from-project
'''

from collections import defaultdict, deque
from typing import List


class Solution:
  def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
    dg = defaultdict(list)
    g = defaultdict(list)
    m = {}
    curr = 0

    def g_cnt(u: int) -> int:
      q = deque([u])
      seen = set(q)

      while q:
        u = q.popleft()
        for v in g[u]:
          if v in seen:
            continue

          seen.add(v)
          q.append(v)

      return seen

    def dg_cnt(u: int):
      q = deque([u])
      seen = set(q)

      while q:
        u = q.popleft()
        for v in dg[u]:
          if v in seen:
            continue

          seen.add(v)
          q.append(v)

      return seen

    for a, b in invocations:
      dg[a].append(b)
      g[a].append(b)
      g[b].append(a)

    all_nodes = g_cnt(k)
    sus_nodes = dg_cnt(k)
    can_remove = len(all_nodes) == len(sus_nodes)
    res = []
    # print('init:', all_nodes, sus_nodes, can_remove)

    for u in range(n):
      if can_remove and u in sus_nodes:
        continue

      res.append(u)

    return res
        