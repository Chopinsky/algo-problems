'''
3559-number-of-ways-to-assign-edge-weights-ii
'''

from typing import List
from collections import defaultdict


class LCA:
  def __init__(self, n: int, e: List[int] , root: int = 1):
    self.n = n
    self.log = n.bit_length()
    self.g = defaultdict(list)

    for u, v in e:
      self.g[u].append(v)
      self.g[v].append(u)

    self.depth = [0] * (n+1)
    self.p = [[-1]*self.log for _ in range(n+1)]
    
    self.dfs(root, -1)
    self.build()

  def get_depth(self, u: int):
    return self.depth[u]

  def dfs(self, u: int, p: int):
    self.p[u][0] = p
    for v in self.g[u]:
      if v == p:
        continue

      self.depth[v] = self.depth[u]+1
      self.dfs(v, u)

  def build(self):
    for k in range(1, self.log):
      for u in range(1, self.n+1):
        prev = self.p[u][k-1]
        if prev != -1:
          self.p[u][k] = self.p[prev][k-1]

  def query(self, u: int, v: int) -> int:
    if self.depth[u] < self.depth[v]:
      u, v = v, u

    for k in reversed(range(self.log)):
      if self.depth[u] - (1<<k) >= self.depth[v]:
        u = self.p[u][k]

    if u == v:
      return u

    for k in reversed(range(self.log)):
      if self.p[u][k] != self.p[v][k]:
        u = self.p[u][k]
        v = self.p[v][k]

    return self.p[u][0]


mod = 10**9+7
mx = 10**5 + 1
fac = [1]*mx
inv = [1]*mx
inv[-1] = pow(fac[-1], mod-2, mod)

for val in range(1, mx):
  fac[val] = (val * fac[val-1]) % mod

for val in range(mx-2, -1, -1):
  inv[val] = ((val+1) * inv[val+1]) % mod


class Solution:
  def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    n = len(edges) + 1
    deep = [0]*(n+1)
    g = [[] for _ in range(n+1)]
    q = [[] for _ in range(n+1)]

    ans = [0]*len(queries)
    res = [0]*len(queries)
    visited = [False]*(n+1)
    parent = [i for i in range(n+1)]

    for u, v in edges:
      g[u].append(v)
      g[v].append(u)

    for idx, [u, v] in enumerate(queries):
      q[u].append((v, idx))
      q[v].append((u, idx))

    def find(x: int):
      while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

      return parent[x]

    def tarjan(u: int, p: int):
      visited[u] = True
      for v in g[u]:
        if v == p:
          continue

        tarjan(v, u)
        parent[v] = u

      for v, idx in q[u]:
        if visited[v]:
          ans[idx] = find(v)

    def f(u: int, p: int, d: int):
      deep[u] = d
      for v in g[u]:
        if v == p:
          continue

        f(v, u, d+1)

    def comb(n: int, a: int):
      return (fac[n]*inv[a]*inv[v-a]) % mod

    def f1(x: int):
      res = 0
      for i in range(1, x+1, 2):
        res = (res + comb(x, i)) % mod

      return res

    tarjan(1, 0)
    f(1, 0, 0)

    for i, [a, b] in enumerate(queries):
      lca = ans[i]
      x = deep[a] + deep[b] - 2*deep[lca]

      if x == 0:
        res[i] = 0
      else:
        res[i] = pow(2, x-1, mod)

    return res

  def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    mod = 10**9 + 7
    n = len(edges)
    lca = LCA(n+1, edges)
    res = []

    for u, v in queries:
      r = lca.query(u, v)
      ln = lca.get_depth(u) + lca.get_depth(v) - 2*lca.get_depth(r)
      if ln == 0:
        res.append(0)
      else:
        res.append(2**(ln-1) % mod)

    return res
      