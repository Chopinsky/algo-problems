'''
3144. Minimum Substring Partition of Equal Character Frequency
'''

from functools import lru_cache
from typing import Dict
from collections import defaultdict


class Solution:
  def minimumSubstringsInPartition(self, s: str) -> int:
    n = len(s)
    
    def check(d: Dict) -> bool:
      cnt = -1
      for c in d.values():
        if cnt < 0:
          cnt = c
          continue
          
        if c != cnt:
          return False
        
      return True
    
    @lru_cache(None)
    def divide(i: int) -> int:
      if i >= n:
        return 0
      
      d = defaultdict(int)
      parts = n-i
      
      for j in range(i, n):
        ch = s[j]
        d[ch] += 1
        
        if check(d):
          parts = min(parts, 1 + divide(j+1))
          
      return parts
      
    return divide(0)
        