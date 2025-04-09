'''
3387. maximize-amount-after-two-days-of-conversions
'''

from typing import List
from collections import defaultdict


class Solution:
  def maxAmount(self, init: str, p1: List[List[str]], r1: List[float], p2: List[List[str]], r2: List[float]) -> float:
    def iter(src: str, p: List, r: List):
      edges = defaultdict(list)
      nodes = {}

      for [u, v], w in zip(p, r):
        edges[u].append((v, w))
        edges[v].append((u, 1.0/w))
        nodes[u] = 0
        nodes[v] = 0

      nodes[src] = 1.0
      curr, nxt = [src], []
      # print('onboard:', edges)

      while curr:
        for u in curr:
          v0 = nodes[u]
          for v, w in edges[u]:
            v1 = v0*w
            if v1 > nodes[v]:
              nodes[v] = v1
              nxt.append(v)

        curr, nxt = nxt, curr
        nxt.clear()

      return nodes

    d1 = iter(init, p1, r1)
    final = 1.0

    for c, amount in d1.items():
      d2 = iter(c, p2, r2)
      # print('convert:', (c, amount), d2)
      final = max(final, amount*d2.get(init, 0))

    return final

        