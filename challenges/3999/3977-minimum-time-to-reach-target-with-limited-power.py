'''
3977-minimum-time-to-reach-target-with-limited-power
'''

from typing import List
from collections import defaultdict
from math import inf
from heapq import heappush, heappop


class Solution:
  def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
    if source == target:
      return [0, power]

    e = [[] for _ in range(n)]
    for u, v, w in edges:
      e[u].append((v, w))

    dist = [[inf]*(power+1) for _ in range(n)]
    dist[source][power] = 0
    stack = [(0, power, source)]
    best_t, best_p = -1, -1

    while stack:
      t0, p0, u = heappop(stack)
      if t0 != dist[u][p0]:
        continue

      if best_t >= 0 and t0 > best_t:
        break

      if u == target:
        if best_t == -1:
          best_t = t0
        
        best_p = max(best_p, p0)
        continue

      # not enough power to go out
      next_p = p0 - cost[u]
      if next_p < 0:
        continue

      for v, tt in e[u]:
        next_t = t0 + tt
        if next_t < dist[v][next_p]:
          dist[v][next_p] = next_t
          heappush(stack, (next_t, next_p, v))
      
    # print('??', best_t, best_p)
    return [best_t, best_p]

  def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
    if source == target:
      return [0, power]

    e = defaultdict(list)
    for u, v, t in edges:
      e[u].append((v, t))

    s = {}
    stack = [(0, power, source)]
    res = [inf, -inf]
    done = False

    while stack and not done:
      t0, p0, u = heappop(stack)
      c0 = cost[u]
      # print('state:', u, t0, p0)

      if u == target:
        if t0 > res[0]:
          break

        res[0] = min(res[0], t0)
        res[1] = max(res[1], p0)

        continue

      # not enough power
      p1 = p0 - c0
      if p1 < 0:
        continue

      for v, tt in e[u]:
        t1 = t0 + tt

        if v == target:
          # print('reach:', t1, p1)
          if t1 < res[0]:
            res[0] = t1
            res[1] = p1
          elif t1 == res[0]:
            res[1] = max(res[1], p1)

          continue

        if (v, p1) not in s or t1 < s[v, p1]:
          s[v, p1] = t1
          heappush(stack, (t1, p1, v))

    return res if res[0] < inf else [-1, -1]
