'''
2608. Shortest Cycle in a Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1. The edges in the graph are represented by a given 2D integer array edges, where edges[i] = [ui, vi] denotes an edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

Return the length of the shortest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node, and each edge in the path is used only once.

Example 1:

Input: n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
Output: 3
Explanation: The cycle with the smallest length is : 0 -> 1 -> 2 -> 0 
Example 2:

Input: n = 4, edges = [[0,1],[0,2]]
Output: -1
Explanation: There are no cycles in this graph.

Constraints:

2 <= n <= 1000
1 <= edges.length <= 1000
edges[i].length == 2
0 <= ui, vi < n
ui != vi
There are no repeated edges.
'''

from collections import defaultdict
from typing import List
import math


class Solution:
  '''
  a cycle in a graph can be found in DFS or BFS, but BFS is easier to manage, since we can add
  the depth between 2 paths (1 of which is the shortest) from root to node u when the 2 paths 
  cross each other to calculate the nunber of nodes in the cycle
  '''
  def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
    e = defaultdict(set)
    for u, v in edges:
      e[u].add(v)
      e[v].add(u)
      
    def find_cycle(root: int) -> int:
      # print('='*8)
      # print('check:', root)
      
      d = 1
      ln = math.inf
      depth = {root:0}
      curr, nxt = set([(root, -1)]), set()
      
      while curr:
        # print(d, curr)
        for u, p in curr:
          for v in e[u]:
            if v == p:
              continue
              
            if v in depth:
              # print('cycle:', v, (d, depth[v]))
              ln = min(ln, d + depth[v])
            else:
              nxt.add((v, u))
              depth[v] = d
          
        curr, nxt = nxt, curr
        nxt.clear()
        d += 1
      
      return ln
    
    short = math.inf
    for u in range(n):
      short = min(short, find_cycle(u))
      
    return -1 if short == math.inf else short
 