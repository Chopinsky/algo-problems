'''
3249. Count the Number of Good Nodes

[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
[[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]
[[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]
[[2,0],[4,2],[1,2],[3,1],[5,1]]
'''

from typing import List
from collections import defaultdict

class Solution:
  def countGoodNodes(self, edges: List[List[int]]) -> int:
    e = defaultdict(list)
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)
    
    def dp(u: int, p: int):
      if u > 0 and len(e[u]) == 1:
        return 1, 1
      
      subtree_sizes = set()
      size = 1
      count = 0
      
      for v in e[u]:
        if v == p:
          continue
          
        c0, s0 = dp(v, u)
        subtree_sizes.add(s0)
        count += c0
        size += s0
      
      if len(subtree_sizes) == 1:
        count += 1
        
      # print('dp:', (u, p), count, size)
      return count, size
      
    cnt, _ = dp(0, -1)
    
    return cnt
      