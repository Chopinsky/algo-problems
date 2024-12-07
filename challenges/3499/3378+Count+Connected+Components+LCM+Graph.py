'''
3378. Count Connected Components in LCM Graph
'''

from collections import Counter
from typing import List


class Solution:
  def countComponents(self, nums: List[int], threshold: int) -> int:
    c = Counter(nums)
    if 1 in c:
      return 1 + sum(1 if val > threshold else 0 for val in nums)
    
    nodes = [i for i in range(threshold+1)]
    
    def find(u: int):
      # print('find:', u)
      if u > threshold:
        return u
      
      while nodes[u] != u:
        u = nodes[u]
        
      return u
        
    def union(u: int, v: int):
      # print('union:', u, v)
      r0 = find(u)
      r1 = find(v)
      
      if r0 <= r1:
        nodes[r1] = r0
      else:
        nodes[r0] = r1
    
    for v0 in sorted(c):
      if v0 > threshold:
        break
        
      for v1 in range(2*v0, threshold+1, v0):
        union(v0, v1)  
        
    # print(nodes)
    comp = set()
    for val in c:
      comp.add(find(val))
    
    return len(comp)
    