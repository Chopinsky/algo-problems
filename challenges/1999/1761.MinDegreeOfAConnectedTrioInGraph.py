'''
You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges, where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.

A connected trio is a set of three nodes where there is an edge between every pair of them.

The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.

Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.

Example 1:

Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
Output: 3
Explanation: There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.

Example 2:

Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
Output: 0
Explanation: There are exactly three trios:
1) [1,4,3] with degree 0.
2) [2,5,6] with degree 2.
3) [5,6,7] with degree 2.

Constraints:

2 <= n <= 400
edges[i].length == 2
1 <= edges.length <= n * (n-1) / 2
1 <= ui, vi <= n
ui != vi
There are no repeated edges.
'''


from typing import List
from collections import defaultdict
import math


class Solution:
  def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
    if n <= 2:
      return -1
    
    e = defaultdict(list)
    added = set()
    ue = []
    degree = math.inf
    
    # build the unique edges
    for u, v in edges:
      u, v = min(u, v), max(u, v)
      if (u, v) in added:
        continue
        
      ue.append((u, v))
      added.add((u, v))
      
      e[u].append(v)
      e[v].append(u)
    
    # optimize the later iteration -- smaller degree nodes
    # will be checked first
    for u in e:
      e[u] = sorted(e[u], key=lambda x: len(e[x]))
    
    # iterate over all edges and find the 3rd common nodes between
    # u and v, and quit the iteration early if we won't find a better
    # solution than what we already have
    for u, v in ue:
      if len(e[u]) > len(e[v]):
        u, v = v, u
      
      for w in e[u]:
        trio_deg = len(e[u]) + len(e[v]) + len(e[w]) - 6
        
        # quit early if we won't find a better solution
        if trio_deg >= degree:
          break
          
        # not a common neighbor for both u and v
        if (w == v) or (w not in e[v]):
          continue
          
        degree = min(degree, trio_deg)
        if degree == 0:
          return degree
      
    return -1 if degree == math.inf else degree
  