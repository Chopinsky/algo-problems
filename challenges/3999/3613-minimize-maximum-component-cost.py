'''
3613-minimize-maximum-component-cost
'''

from typing import List


class Solution:
  def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
    # sole node, no weight
    if not edges or k >= n:
      return 0

    edges.sort(key=lambda x: x[2])
    g = [i for i in range(n)]
    rank = [0]*n
    cnt = n
    # print('init:', edges)

    def find(x: int) -> int:
      while g[x] != x:
        x = g[x]

      return x

    def union(x: int, y: int) -> bool:
      px, py = find(x), find(y)
      if px == py:
        return False

      if rank[px] < rank[py]:
        px, py = py, px

      g[py] = px
      if rank[px] == rank[py]:
        rank[px] += 1

      return True
        
    for u, v, w in edges:
      # connecting 2 components
      if union(u, v):
        cnt -= 1

      if cnt == k:
        return w

    return -1
