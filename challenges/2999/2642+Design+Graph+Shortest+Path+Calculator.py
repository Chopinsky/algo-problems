'''
2642. Design Graph With Shortest Path Calculator

There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:

Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.

Example 1:

Input
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
Output
[null, 6, -1, null, 6]

Explanation
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.

Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1)
edges[i].length == edge.length == 3
0 <= fromi, toi, from, to, node1, node2 <= n - 1
1 <= edgeCosti, edgeCost <= 106
There are no repeated edges and no self-loops in the graph at any point.
At most 100 calls will be made for addEdge.
At most 100 calls will be made for shortestPath.
'''

from typing import List
from collections import defaultdict
from heapq import heappush, heappop
import math

class Graph:
  def __init__(self, n: int, edges: List[List[int]]):
    self.n = n
    self.c = defaultdict(list)
    
    for u, v, c in edges:
      self.c[u].append((v, c))
      

  def addEdge(self, edge: List[int]) -> None:
    u, v, c = edge
    self.c[u].append((v, c))


  def shortestPath(self, u: int, v: int) -> int:
    stack = [(0, u)]
    seen = set()
    
    while stack:
      c0, w0 = heappop(stack)
      if w0 == v:
        return c0
      
      if w0 in seen:
        continue
        
      seen.add(w0)
      for w1, c1 in self.c[w0]:
        if w1 in seen:
          continue
          
        heappush(stack, (c0+c1, w1))
      
    return -1


class Graph0:
  def __init__(self, n: int, edges: List[List[int]]):
    self.dist = {}
    self.e = defaultdict(list)
    self.n = n
    
    for u, v, w in edges:
      self.e[u].append((v, w))
    
    def calc_dist(root):
      d = {}
      stack = [(0, root)]
      
      while stack:
        cost, u = heappop(stack)
        if cost >= d.get(u, math.inf):
          continue
          
        d[u] = cost
        for v, w in self.e[u]:
          if cost+w >= d.get(v, math.inf):
            continue
            
          heappush(stack, (cost+w, v))
          
      self.dist[root] = d
      
    for i in range(n):
      calc_dist(i)
      
    # print(self.dist, self.e)


  def addEdge(self, edge: List[int]) -> None:
    u, v, w = edge
    self.e[u].append((v, w))
    
    # nothing to update here
    if u not in self.dist:
      d = {}
      d[v] = w
      
      if v in self.dist:
        for k, w0 in self.dist[v].items():
          d[k] = min(d.get(k, math.inf), w+w0)
      
      self.dist[u] = d
      return
    
    # nothing to update here
    d = self.dist[u]
    if d.get(v, math.inf) <= w:
      return
    
    for i in self.dist:
      di = self.dist[i]

      # check if we can get to `v` via `u` with a shorter distance
      if u not in di:
        continue

      # update the min-distance for `i` -> `v`
      di[v] = min(di.get(v, math.inf), di[u]+w)
      if v not in self.dist:
        continue

      # update all nodes that can be reachable from `v`, since we
      # may have a shorter route just found
      dv = self.dist[v]
      for j in dv:
        if j == v or j == i:
          continue

        di[j] = min(di.get(j, math.inf), di[v]+dv[j])


  def shortestPath(self, node1: int, node2: int) -> int:
    if node1 not in self.dist:
      return -1
    
    if node2 not in self.dist[node1]:
      return -1
      
    return self.dist[node1][node2]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)