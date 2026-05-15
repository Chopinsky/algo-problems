'''
3928-minimum-cost-to-buy-apples-ii
'''

from typing import List
from heapq import heappush, heappop
from math import inf


class Solution:
  def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
    e = [[] for _ in range(n)]
    c = [[] for _ in range(n)]

    for u, v, cost, tax in roads:
      e[u].append((v, cost))
      e[v].append((u, cost))
      
      carry_cost = cost * tax
      c[u].append((v, carry_cost))
      c[v].append((u, carry_cost))

    ans = prices.copy()
    empty = [inf]*n
    carry = [inf]*n

    def find_best(src: int) -> int:
      for i in range(n):
        empty[i] = inf
        carry[i] = inf

      # build empty travel graph
      empty[src] = 0
      q = [(0, src)]

      while q:
        p, u = heappop(q)

        # better solution exists
        if p > empty[u]:
          continue

        for v, w in e[u]:
          if p+w < empty[v]:
            empty[v] = p+w
            heappush(q, (empty[v], v))

      # build carry travel graph
      carry[src] = 0
      q = [(0, src)]

      while q:
        p, u = heappop(q)
        
        # better solution exists
        if p > carry[u]:
          continue

        for v, w in c[u]:
          if p+w < carry[v]:
            carry[v] = p+w
            heappush(q, (carry[v], v))

      # find best pricing to all shops from the src
      best = prices[src]
      for shop in range(n):
        # can't reach
        if empty[shop] == inf or carry[shop] == inf:
          continue

        # total = {travel_empty} + {travel_back_with_apple} + {apple_cost}
        total = empty[shop] + carry[shop] + prices[shop]
        best = min(best, total)

      return best

    for u in range(n):
      ans[u] = find_best(u)

    return ans
