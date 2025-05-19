'''
3553-minimum-weighted-subgraph-with-the-required-paths-ii

find the LCA between triplet (s1, s2, dest), calculate and sum edge weigths
between each pair of them, the answer if half of the sum (because each edge 
is counted 2x during the dist calc) 
'''

from typing import List


class Solution:
  def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    n = len(edges) + 1
    size = n.bit_length()
    e = [[] for _ in range(n)]
    for u, v, w in edges:
      e[u].append((v, w))
      e[v].append((u, w))

    up = [[-1]*n for _ in range(size)]
    depth = [0]*n
    dist = [0]*n
    q = [0]

    for u in q:
      for v, w in e[u]:
        if v == up[0][u]:
          continue

        up[0][v] = u
        depth[v] = depth[u]+1
        dist[v] = dist[u]+w
        q.append(v)

    for k in range(size-1):
      for v in range(n):
        p = up[k][v]
        up[k+1][v] = -1 if p < 0 else up[k][p]

    def lca(u: int, v: int) -> int:
      if depth[u] < depth[v]:
        u, v = v, u

      diff = depth[u]-depth[v]
      for k in range(size):
        if (diff>>k) & 1:
          u = up[k][u]

      if u == v:
        return u

      for k in reversed(range(size)):
        if up[k][u] != up[k][v]:
          u = up[k][u]
          v = up[k][v]

      return up[0][u]
        
    def calc_dist(u: int, v: int) -> int:
      p = lca(u, v)
      return dist[u] + dist[v] - 2*dist[p]

    ans = []
    for s1, s2, d in queries:
      d0 = calc_dist(s1, s2)
      d1 = calc_dist(s1, d)
      d2 = calc_dist(s2, d)
      ans.append((d0+d1+d2) // 2)

    return ans
    

