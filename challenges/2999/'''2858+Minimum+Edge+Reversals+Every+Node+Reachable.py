'''
2858. Minimum Edge Reversals So Every Node Is Reachable

There is a simple directed graph with n nodes labeled from 0 to n - 1. The graph would form a tree if its edges were bi-directional.

You are given an integer n and a 2D integer array edges, where edges[i] = [ui, vi] represents a directed edge going from node ui to node vi.

An edge reversal changes the direction of an edge, i.e., a directed edge going from node ui to node vi becomes a directed edge going from node vi to node ui.

For every node i in the range [0, n - 1], your task is to independently calculate the minimum number of edge reversals required so it is possible to reach any other node starting from node i through a sequence of directed edges.

Return an integer array answer, where answer[i] is the minimum number of edge reversals required so it is possible to reach any other node starting from node i through a sequence of directed edges.

Example 1:

Input: n = 4, edges = [[2,0],[2,1],[1,3]]
Output: [1,1,0,2]
Explanation: The image above shows the graph formed by the edges.
For node 0: after reversing the edge [2,0], it is possible to reach any other node starting from node 0.
So, answer[0] = 1.
For node 1: after reversing the edge [2,1], it is possible to reach any other node starting from node 1.
So, answer[1] = 1.
For node 2: it is already possible to reach any other node starting from node 2.
So, answer[2] = 0.
For node 3: after reversing the edges [1,3] and [2,1], it is possible to reach any other node starting from node 3.
So, answer[3] = 2.

Example 2:

Input: n = 3, edges = [[1,2],[2,0]]
Output: [2,0,1]
Explanation: The image above shows the graph formed by the edges.
For node 0: after reversing the edges [2,0] and [1,2], it is possible to reach any other node starting from node 0.
So, answer[0] = 2.
For node 1: it is already possible to reach any other node starting from node 1.
So, answer[1] = 0.
For node 2: after reversing the edge [1, 2], it is possible to reach any other node starting from node 2.
So, answer[2] = 1.

Constraints:

2 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ui == edges[i][0] < n
0 <= vi == edges[i][1] < n
ui != vi
The input is generated such that if the edges were bi-directional, the graph would be a tree.
'''

from typing import List
from collections import defaultdict


class Solution:
  '''
  the idea is for different node-u as the tree root, we can calculate the reversals (e.g., r0) required for its
  parent node-p, and the reversals required is `r0 + (1 if u->v else -1)`, that's to say, only update the 1 edge
  between (u, v), since that's the only one that would differ between the reversals for root-u and reversals for
  root-p.
  '''
  def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
    e = defaultdict(list)
    d = {}
    
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)
      d[u, v] = 1
      d[v, u] = -1
      
    dp = [0]*n
    stack = []
    curr, nxt = [(0, -1)], []
    
    # iter-1: bottom-up BFS to get the edge reversals for tree
    #         rooted @ node-0
    while curr:
      for u, p in curr:
        for v in e[u]:
          if v == p:
            continue
            
          nxt.append((v, u))
      
      stack.append(curr)
      curr = nxt
      nxt = []
      
    while stack:
      curr = stack.pop()
      for u, p in curr:
        if p < 0:
          continue
          
        dp[p] += dp[u] + (1 if d[p, u] < 0 else 0)
        
    # iter-2: top-down BFS to calculate reversals needed to have
    #         the tree rooted @ node-v for the branch that's a
    #         subtree rooted @ node-u, where (u, v) if the traversal
    curr, nxt = [(0, -1)], []
    ans = [0] * n
    ans[0] = dp[0]
    
    while curr:
      for u, p in curr:
        for v in e[u]:
          if v == p:
            continue
            
          nxt.append((v, u))
          ans[v] += ans[u] + (1 if d[u, v] > 0 else -1)
          
      curr, nxt = nxt, curr
      nxt.clear()
    
    return ans
        