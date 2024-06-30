'''
3203. Find Minimum Diameter After Merging Two Trees

There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the minimum possible diameter of the resulting tree.

The diameter of a tree is the length of the longest path between any two nodes in the tree.

Example 1:

Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]

Output: 3

Explanation:

We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

Output: 5

Explanation:

We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

Constraints:

1 <= n, m <= 10^5
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.

Test cases:
[[0,1],[0,2],[0,3]]
[[0,1]]
[[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
[[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
[[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]]
[[0,1],[0,2],[0,3]]
[]
[]
'''

from typing import List
from collections import defaultdict

class Solution:
  def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
    def get_min_levels(e):
      if not e:
        return 0, 1
      
      nb = defaultdict(set)
      curr, nxt = [], []
      
      for u, v in e:
        nb[u].add(v)
        nb[v].add(u)
        
      for u, lst in nb.items():
        if len(lst) == 1:
          curr.append(u)
          
      levels = 0
      
      while len(curr) > 1:
        levels += 1
        
        for u in curr:
          if not nb[u]:
            continue
          
          v = nb[u].pop()
          nb[v].discard(u)
          
          if len(nb[v]) == 1:
            nxt.append(v)
        
        curr, nxt = nxt, curr
        nxt.clear()
        
      total = 2*levels
      if not curr:
        total -= 1
        
      return levels, total
    
    l1, d1 = get_min_levels(edges1)
    l2, d2 = get_min_levels(edges2)
    # print((l1, d1), edges1)
    # print((l2, d2), edges2)
    
    return max(d1, d2, l1+l2+1)
        