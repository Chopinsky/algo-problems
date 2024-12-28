'''
3372. Maximize the Number of Target Nodes After Connecting Trees I
'''

from typing import List, Dict
from collections import defaultdict


class Solution:
  def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
    if k == 0:
      return [1]*(len(edges1)+1)
    
    def collect(tree: Dict, root: int, dist: int) -> int:
      if dist <= 0:
        return 1 if dist == 0 else 0
      
      count = 0
      curr, nxt = [root], []
      seen = set(curr)
      
      while dist >= 0:
        count += len(curr)
        
        for u in curr:
          for v in tree[u]:
            if v in seen:
              continue
              
            seen.add(v)
            nxt.append(v)
          
        curr, nxt = nxt, curr
        nxt.clear()
        dist -= 1
      
      return count
    
    def build_dist(edges: List, dist: int):
      tree = defaultdict(list)
      for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
        
      ans = []
      for u in range(len(tree)):
        ans.append(collect(tree, u, dist))
        
      return ans
        
    d1 = build_dist(edges1, k)
    d2 = max(build_dist(edges2, k-1))
    # print('init:', d1, d2)
    
    return [val+d2 for val in d1]
    