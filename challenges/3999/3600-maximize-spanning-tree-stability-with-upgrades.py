'''
3600-maximize-spanning-tree-stability-with-upgrades
'''

from typing import List
import math


class DSU:
  def __init__(self, n: int):
    self.par = list(range(n))
    self.size = [1]*n

  def find(self, x: int):
    if self.par[x] != x:
      self.par[x] = self.find(self.par[x])

    return self.par[x]

  def union(self, x: int, y :int):
    rx, ry = self.find(x), self.find(y)
    if rx == ry:
      return False

    if self.size[rx] < self.size[ry]:
      rx, ry = ry, rx

    self.par[ry] = rx
    self.size[rx] += self.size[ry]

    return True


class Solution:
  def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
    used = 0
    ans = math.inf
    dsu = DSU(n)

    # add must edges
    for u, v, s, m in edges:
      if m == 0:
        continue

      if not dsu.union(u, v):
        return -1

      used += 1
      ans = min(ans, s)

    edges.sort(key=lambda x: -x[2])
    wt = []

    # add upgradable edges
    for u, v, s, m in edges:
      if m == 1:
        continue

      if dsu.union(u, v):
        used += 1
        wt.append(s)

    # print('added:', wt)
    for i in range(min(k, len(wt))):
      wt[~i] *= 2
      # print('upgrade:', i, ~i, wt[~i])

    if used != n-1:
      return -1

    return min((ans, *wt))
        