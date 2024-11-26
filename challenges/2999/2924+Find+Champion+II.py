'''
2924. Find Champion II
'''

from typing import List

class Solution:
  def findChampion(self, n: int, edges: List[List[int]]) -> int:
    p = [0]*n
    
    for u, v in edges:
      p[v] += 1
    
    # print('done:', p)
    if p.count(0) > 1:
      return -1
    
    return p.index(0)
        