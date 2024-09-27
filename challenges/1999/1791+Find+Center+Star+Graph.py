'''
1791. Find Center of Star Graph
'''

from typing import List

class Solution:
  def findCenter(self, edges: List[List[int]]) -> int:
    a, b = edges[0], edges[1]
    
    return a[0] if a[0] in b else a[1]
        