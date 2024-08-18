'''
624. Maximum Distance in Arrays
'''

from typing import List

class Solution:
  def maxDistance(self, arrays: List[List[int]]) -> int:
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    dist = 0
    
    for arr in arrays[1:]:
      first, last = arr[0], arr[-1]
      dist = max(
        dist,
        abs(max_val-first),
        abs(last-min_val)
      )
      
      max_val = max(max_val, last)
      min_val = min(min_val, first)
      
    return dist
        