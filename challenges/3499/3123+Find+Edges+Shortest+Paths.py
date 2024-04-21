'''

Test cases:

6
[[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]
4
[[2,0,1],[0,1,1],[0,3,4],[3,2,2]]
3
[[2,1,6]]
'''

from typing import List, Dict
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
  def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
    def add(graph, u, v, w):
      if u not in graph:
        graph[u] = {}
        
      graph[u][v] = w

    def create_graph(edges: List[List[int]]) -> Dict:
      graph = defaultdict(list)
        
      for u, v, w in edges:
        add(u, v, w)
        add(v, u, w)

      return graph

    def dist(graph: Dict, src: int):
      e = {k:v.copy() for k, v in graph.items()}
      d = [float('inf')]*n
      d[src] = 0
      stack = [(0, src)]
      
      while stack:
        d0, u = heappop(stack)
        if u not in e:
          continue
        
        for v, w in e[u].items():
          if d[v] <= d0+w:
            continue
          
          # the (u, v) edge yield a new connection
          d[v] = d0+w
          heappush(stack, (d[v], v))
          
          # the (u, v) edge is used, retire it from future 
          # iterations
          if u in e[v]:
            del e[v][u]
      
      return d
    
    # build the graph and min-dist helpers
    g = create_graph(edges)
    d0 = dist(g, 0)
    d1 = dist(g, n-1)

    # constants
    tgt = d0[n-1]
    m = len(edges)
    # print(d0, d1)
    
    if tgt == float('inf'):
      return [False]*m
    
    def check(u: int, v: int, w: int) -> bool:
      if d0[u] + d1[u] != tgt:
        return False
      
      if d0[v] + d1[v] != tgt:
        return False
      
      min_dist = min(d0[u], d0[v])
      max_dist = max(d0[u], d0[v])
      
      return min_dist + w == max_dist
    
    return [check(u, v, w) for u, v, w in edges]
    