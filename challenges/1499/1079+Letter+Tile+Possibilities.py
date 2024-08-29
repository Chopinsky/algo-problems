'''
1079. Letter Tile Possibilities
'''

from collections import Counter
from functools import lru_cache
from math import comb

class Solution:
  def numTilePossibilities(self, tiles: str) -> int:
    c = Counter(tiles)
    n = len(tiles)
    
    if len(tiles) == 1:
      return 1
    
    if len(c) == 1:
      return n
    
    cand = list(c.values())
    total = 0
    stack = []
    # print(cand)
    
    @lru_cache(None)
    def update(s):
      if len(s) == 0:
        return 0
      
      pos = sum(s)
      cnt = 1
      
      for val in s:
        cnt *= comb(pos, val)
        pos -= val
        
      return cnt
    
    def build(i: int):
      nonlocal total

      if i >= len(cand):
        print('?', i, stack)
        total += update(tuple(sorted(stack)))
        return
      
      build(i+1)

      for c0 in range(1, cand[i]+1):
        stack.append(c0)
        build(i+1)
        stack.pop()
    
    build(0)
    
    return total
  