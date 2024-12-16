'''
3389. Minimum Operations to Make Character Frequencies Equal
'''

from typing import List
from functools import lru_cache
import math


class Solution:
  def makeStringGood(self, s: str) -> int:
    d = [0]*26
    for ch in s:
      d[ord(ch)-ord('a')] += 1
      
    def check(arr: List) -> bool:
      freq = 0
      for val in arr:
        if val == 0:
          continue
          
        if freq == 0:
          freq = val
          continue
          
        if val != freq:
          return False
        
      return True
    
    if check(d):
      return 0
    
    top = max(d)
    # print('init:', top, d)
    
    @lru_cache(None)
    def dp(i: int, c: int):
      if i >= 26:
        return 0
      
      if c > top:
        return math.inf
      
      # already done
      curr = d[i]
      if curr == 0 or curr == c:
        return dp(i+1, c)
      
      # if reduce to 0
      ops = curr + dp(i+1, c)
      
      if curr > c:
        # reduce to c
        diff0 = curr-c
        ops = min(ops, diff0+dp(i+1, c))
        
        # we can average
        if i+1 < 26 and d[i+1] < c:
          diff1 = c-d[i+1]
          diff2 = min(diff0, diff1)
          ops = min(ops, diff0+diff1-diff2+dp(i+2, c))
        
      if curr < c:
        # increase to c
        diff0 = c-curr
        ops = min(ops, diff0+dp(i+1, c))
        
        # we can shift: curr->0, d[i+1]->c
        if i+1 < 26 and d[i+1] < c:
          diff1 = c-d[i+1]
          diff2 = min(curr, diff1)
          ops = min(ops, curr+diff1-diff2+dp(i+2, c))
      
      # if i == 6:
      #   print('iter:', c, ops)
        
      return ops
      
    return min(dp(0, c) for c in range(top+1))
  