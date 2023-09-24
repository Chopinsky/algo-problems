'''
2867. Count Valid Paths in a Tree

There is an undirected tree with n nodes labeled from 1 to n. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree.

Return the number of valid paths in the tree.

A path (a, b) is valid if there exists exactly one prime number among the node labels in the path from a to b.

Note that:

The path (a, b) is a sequence of distinct nodes starting with node a and ending with node b such that every two adjacent nodes in the sequence share an edge in the tree.
Path (a, b) and path (b, a) are considered the same and counted only once.

Example 1:

Input: n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]
Output: 4
Explanation: The pairs with exactly one prime number on the path between them are: 
- (1, 2) since the path from 1 to 2 contains prime number 2. 
- (1, 3) since the path from 1 to 3 contains prime number 3.
- (1, 4) since the path from 1 to 4 contains prime number 2.
- (2, 4) since the path from 2 to 4 contains prime number 2.
It can be shown that there are only 4 valid paths.
Example 2:

Input: n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
Output: 6
Explanation: The pairs with exactly one prime number on the path between them are: 
- (1, 2) since the path from 1 to 2 contains prime number 2.
- (1, 3) since the path from 1 to 3 contains prime number 3.
- (1, 4) since the path from 1 to 4 contains prime number 2.
- (1, 6) since the path from 1 to 6 contains prime number 3.
- (2, 4) since the path from 2 to 4 contains prime number 2.
- (3, 6) since the path from 3 to 6 contains prime number 3.
It can be shown that there are only 6 valid paths.

Constraints:

1 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
The input is generated such that edges represent a valid tree.
'''

from typing import List
from collections import defaultdict


class Solution:
  def countPaths(self, n: int, edges: List[List[int]]) -> int:
    s = [i for i in range(n+1)]
    p = set()
    for v0 in range(2, n+1):
      if s[v0] < v0:
        continue

      p.add(v0)
      for v1 in range(v0*v0, n+1, v0):
        s[v1] = v0
      
    e = defaultdict(list)
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)
      
    # print('init:', p, e)
    branch = {}
    outbound = defaultdict(int)
    cand = []
    
    # dfs to get the count of non-prime nodes between prime number 
    # nodes, add the counts to the `branch` and `outbound`
    def dfs(u: int, parent: int):
      if u in p:
        cand.append((u, parent))
        return 0
        
      cc = 1
      for v in e[u]:
        if v == parent:
          continue
          
        cc += dfs(v, u)
      
      return cc
    
    for u in sorted(p):
      for v in e[u]:
        if (u, v) in branch:
          continue
          
        if v in p:
          branch[u, v] = 0
          branch[v, u] = 0
          continue
          
        cand.clear()
        cand.append((u, v))
        nodes = dfs(v, u)
        
        for u0, v0 in cand:
          branch[u0, v0] = nodes
          outbound[u0] += nodes
    
    # print('update:', branch, outbound)
    cnt = 0
    for u in sorted(p):
      if outbound[u] == 0:
        continue
        
      cnt += outbound[u]
      c0 = 0
      
      for v in e[u]:
        if (u, v) not in branch:
          continue

        # c1 is the number of non-prime nodes in this branch
        c1 = branch[u, v]

        # add the number of paths starting from this branch 
        # and ending in non-prime nodes in other branches, passing
        # through prime-node `u`
        c0 += c1 * (outbound[u] - c1)
      
      # pair (a, b) and (b, a) are the same path
      cnt += c0 // 2
      # print('pairs:', u, c0)
    
    return cnt
        