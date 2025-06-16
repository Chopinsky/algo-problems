'''
3585-find-weighted-median-node-in-tree
'''

from collections import defaultdict
from typing import List


class LCA:
  def __init__(self, graph, root=0):
    self.graph = graph
    self.ancestors = defaultdict(list)
    self.time_in = dict()
    self.time_out = dict()
    self.timer = 0
    self.depth = dict()
    self.dist = dict()
    self.dfs(root, root, [root])
      
  def dfs(self, v, parent, path, d=0):
    self.timer += 1
    self.time_in[v] = self.timer
    up = 1

    while len(path) >= up:
      self.ancestors[v].append(path[-up])
      up *= 2

    self.depth[v] = len(path)
    self.dist[v] = d
    path.append(v)
    
    for u, w in self.graph[v].items():
      if u != parent:
        self.dfs(u, v, path, d + w)

    path.pop()
    self.timer += 1
    self.time_out[v] = self.timer

  def is_ancestor(self, u, v):
    return self.time_in[u] <= self.time_in[v] and self.time_out[u] >= self.time_out[v]
          
  def lca(self, u, v):
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

  def distance(self, u, v):
    a = self.lca(u, v)
    if a in {u, v}:
      return abs(self.dist[v] - self.dist[u])
    return (self.dist[u] - self.dist[a]) + (self.dist[v] - self.dist[a])

  def find_node_dist(self, u, distance, mode=0):
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

  def median(self, u, v):
    goal = (self.distance(u, v)) / 2
    a = self.lca(u, v)
    if u == a:
      return self.find_node_dist(v, goal + self.dist[u])
    if v == a:
      return self.find_node_dist(u, goal + self.dist[v], 1)

    d = self.distance(a, u)
    if d >= goal:
      return self.find_node_dist(u, d - goal + self.dist[a], 1)

    return self.find_node_dist(v, goal - d + self.dist[a])
                
class Solution:
  def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    graph = defaultdict(dict)
    for u, v, w in edges:
      graph[u][v] = graph[v][u] = w

    lca = LCA(graph)
    return [lca.median(u, v) for u, v in queries]  
