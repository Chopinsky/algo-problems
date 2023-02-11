'''
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
'''

from typing import List
from collections import defaultdict
import math


class Solution:
  def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    b = defaultdict(set)  
    r = defaultdict(set)
    curr, nxt = [], []
    
    for u, v in redEdges:
      r[u].add(v)
      if u == 0:
        curr.append((v, 0))
      
    for u, v in blueEdges:
      b[u].add(v)
      if u == 0:
        curr.append((v, 1))
      
    seen = set(curr)
    dist = [math.inf] * n
    dist[0] = 0
    d = 0
    
    while curr:
      d += 1
      # print(curr, d)
      
      for u, c in curr:
        dist[u] = min(dist[u], d)
        children = b[u] if c == 0 else r[u]
        nc = 1-c
        
        for v in children:
          if (v, nc) in seen:
            continue
            
          nxt.append((v, nc))
          seen.add((v, nc))
      
      curr, nxt = nxt, curr
      nxt.clear()
      
    return [d if d != math.inf else -1 for d in dist]
  
  
  def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    r, b = defaultdict(set), defaultdict(set)
    for u, v in redEdges:
      r[u].add(v)
      
    for u, v in blueEdges:
      b[u].add(v)
      
    dist = [math.inf] * n
    stack, nxt = [(0, 0), (0, 1)], []
    visited = set(stack)
    d = 0
    
    while stack:
      for u, c in stack:
        dist[u] = min(dist[u], d)
        cand = r[u] if c == 0 else b[u]
        nc = 1 - c
        
        for v in cand:
          if (v, nc) in visited:
            continue
            
          nxt.append((v, nc))
          visited.add((v, nc))
          
      # print(d, stack, nxt)
      stack, nxt = nxt, stack
      nxt.clear()
      d += 1
      
    ans = [-1 if d == math.inf else d for d in dist]
    ans[0] = 0
    
    return ans