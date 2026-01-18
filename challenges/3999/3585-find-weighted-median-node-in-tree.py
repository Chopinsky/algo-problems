'''
3585-find-weighted-median-node-in-tree
'''

from collections import defaultdict
from typing import Any, List


class LCA:
  def __init__(self, graph, root=0):
    self.graph = graph
    self.ancestors = defaultdict[int, List[int]](list)
    self.time_in = dict[int, int]()
    self.time_out = dict[int, int]()
    self.timer = 0
    self.dist = dict[int, int]()
    self.dfs(root, root, [root])
      
  def dfs(self, v: int, parent: int, path: List[int], d: int = 0) -> None:
    self.timer += 1
    self.time_in[v] = self.timer
    up = 1

    while up <= len(path):
      self.ancestors[v].append(path[-up])
      up <<= 1

    self.dist[v] = d
    path.append(v)
    
    for u, w in self.graph[v].items():
      if u != parent:
        self.dfs(u, v, path, d + w)

    path.pop()
    self.timer += 1
    self.time_out[v] = self.timer

  def is_ancestor(self, u: int, v: int) -> bool:
    return self.time_in[u] <= self.time_in[v] and self.time_out[u] >= self.time_out[v]
          
  def lca(self, u: int, v: int) -> int:
    if self.is_ancestor(u, v):
      return u
    
    if self.is_ancestor(v, u):
      return v
    
    d = len(self.ancestors[u]) - 1
    while d >= 0:
      d = min(d, len(self.ancestors[u]) - 1)
      if not self.is_ancestor(self.ancestors[u][d], v):
        u = self.ancestors[u][d]

      d -= 1
    
    return self.ancestors[u][0]

  def distance(self, u: int, v: int) -> int:
    a = self.lca(u, v)
    if a in {u, v}:
      return abs(self.dist[v] - self.dist[u])
    return (self.dist[u] - self.dist[a]) + (self.dist[v] - self.dist[a])

  def find(self, u: int, distance: int, mode: int = 0) -> int:
    d = len(self.ancestors[u]) - 1
    m = u
    while d >= 0:
      d = min(d, len(self.ancestors[u]) - 1)
      v = self.ancestors[u][d]
      if self.dist[v] >= distance:
        m = v
        u = self.ancestors[u][d]
      d -= 1

    if mode == 0 or self.dist[m] == distance:
      return m

    return self.ancestors[m][0]

  def median(self, u: int, v: int) -> int:
    goal = (self.distance(u, v)) / 2
    a = self.lca(u, v)
    if u == a:
      return self.find(v, goal + self.dist[u])
    
    if v == a:
      return self.find(u, goal + self.dist[v], 1)

    d = self.distance(a, u) 
    if d >= goal:
      return self.find(u, d - goal + self.dist[a], 1)

    return self.find(v, goal - d + self.dist[a])
                
class Solution:
  def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[float]:
    graph = defaultdict[Any, dict](dict)
    for u, v, w in edges:
      graph[u][v] = w
      graph[v][u] = w

    lca = LCA(graph)

    return [lca.median(u, v) for u, v in queries]  
