'''
3493-properties-graph
'''

from typing import List


class Solution:
  def numberOfComponents(self, p: List[List[int]], k: int) -> int:
    n = len(p)
    g = [i for i in range(n)]
    vals = [set(p[i]) for i in range(n)]

    def find(x: int):
      while g[x] != x:
        x = g[x]

      return x

    def union(x: int, y: int):
      rx, ry = find(x), find(y)
      if rx <= ry:
        g[ry] = rx
      else:
        g[rx] = ry
        
    comp = set()

    def count(a: int, b: int):
      return len(vals[a] & vals[b])

    for i in range(n):
      for j in range(i+1, n):
        if count(i, j) >= k:
          union(i, j)

    for i in range(n):
      root = find(i)
      comp.add(root)
      
    return len(comp)
