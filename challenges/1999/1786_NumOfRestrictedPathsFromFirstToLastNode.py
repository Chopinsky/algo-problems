'''
There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.

Example 1:

Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5
Example 2:


Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
Output: 1
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The only restricted path is 1 --> 3 --> 7.
 

Constraints:

1 <= n <= 2 * 10^4
n - 1 <= edges.length <= 4 * 10^4
edges[i].length == 3
1 <= ui, vi <= n
ui != vi
1 <= weighti <= 10^5
There is at most one edge between any two nodes.
There is at least one path between any two nodes.
'''


from typing import List
from collections import defaultdict
from heapq import heappush, heappop
import math


class Solution:
  def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
    mod = 10 ** 9 + 7
    dist = defaultdict(lambda: math.inf)
    e = defaultdict(list)
    
    for u, v, w in edges:
      e[u].append((v, w))
      e[v].append((u, w))
      
    # print(e)
    q = [(0, n)]
    
    while q:
      d, u = heappop(q)
      # print(d, u)
      if d >= dist[u]:
        continue
      
      dist[u] = d
      for v, w in e[u]:
        # print('nxt', u, v, dist[v])
        if v == n or d+w >= dist[v]:
          continue
          
        # dist[v] = d + w
        heappush(q, (d+w, v))
        
    # print(dist)
    if dist[1] == math.inf:
      return 0
    
    paths = defaultdict(int)
    paths[1] = 1
    q = [(-dist[1], 1)]
    visited = set()
    
    while q:
      _, u = heappop(q)
      # already visited
      if u in visited:
        continue
        
      # print(u)
      visited.add(u)
      
      for v, _ in e[u]:
        if dist[v] >= dist[u]:
          continue
          
        paths[v] = (paths[v] + paths[u]) % mod
        if v != n:
          heappush(q, (-dist[v], v))
        
    # print(paths)
    return paths[n]
  