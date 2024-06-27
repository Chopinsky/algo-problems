'''
2497. Maximum Star Sum of a Graph

There is an undirected graph consisting of n nodes numbered from 0 to n - 1. You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node.

You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A star graph is a subgraph of the given graph having a center node containing 0 or more neighbors. In other words, it is a subset of edges of the given graph such that there exists a common node for all edges.

The image below shows star graphs with 3 and 4 neighbors respectively, centered at the blue node.

The star sum is the sum of the values of all the nodes present in the star graph.

Given an integer k, return the maximum star sum of a star graph containing at most k edges.

Example 1:


Input: vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2
Output: 16
Explanation: The above diagram represents the input graph.
The star graph with the maximum star sum is denoted by blue. It is centered at 3 and includes its neighbors 1 and 4.
It can be shown it is not possible to get a star graph with a sum greater than 16.
Example 2:

Input: vals = [-5], edges = [], k = 0
Output: -5
Explanation: There is only one possible star graph, which is node 0 itself.
Hence, we return -5.

Constraints:

n == vals.length
1 <= n <= 10^5
-10^4 <= vals[i] <= 10^4
0 <= edges.length <= min(n * (n - 1) / 2, 10^5)
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
0 <= k <= n - 1
'''


from heapq import heappush, heappop
from collections import defaultdict
from typing import List

class Solution:
  def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
    if k == 0:
      return max(vals)
    
    n = len(vals)
    cand = []
    graph = [val for val in vals]
    edges_count = [0]*n
    
    for u, v in edges:
      if vals[v] > 0:
        cand.append((vals[v], u))
        
      if vals[u] > 0:
        cand.append((vals[u], v))
    
    cand.sort()
    while cand:
      val, root = cand.pop()
      if edges_count[root] < k:
        graph[root] += val
        edges_count[root] += 1
    
    return max(graph)
  
  def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
    n = len(vals)
    if k == 0:
      return max(vals)
    
    scores = defaultdict(list)
    for u, v in edges:
      # add to the u-centered graph
      if vals[v] >= 0:
        heappush(scores[u], vals[v])
        if len(scores[u]) > k:
          heappop(scores[u])

      # add to the v-centered graph
      if vals[u] >= 0:
        heappush(scores[v], vals[u])
        if len(scores[v]) > k:
          heappop(scores[v])
        
    ans = vals[0]
    for i in range(n):
      ans = max(ans, vals[i]+sum(scores[i]))
      
    return ans
  