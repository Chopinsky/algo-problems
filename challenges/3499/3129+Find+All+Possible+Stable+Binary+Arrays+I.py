'''
3129. Find All Possible Stable Binary Arrays I
'''

from functools import lru_cache
from math import comb


class Solution:
  def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
    mod = 10**9 + 7
    
    @lru_cache(None)
    def dp(c0: int, c1: int, ans: int = 0)-> int:
      '''
      c0 is the count of the digit to be used for this segment, c1 is
      the other digit's count
      '''
      if c0 == 0:
        return 0

      if c1 == 0: 
        return 1 if c0 <= limit else 0

      # use cnt of the digit, then switch to use the other digit
      for cnt in range(1, min(c0, limit)+1):
        ans += dp(c1, c0-cnt)

      return ans % mod

    start_zero = dp(zero, one)
    start_one = dp(one, zero)

    return (start_zero + start_one) % mod
  
  def numberOfStableArrays0(self, zero: int, one: int, limit: int) -> int:
    mod = 10**9 + 7
    n = zero+one
    
    # can put numbers freely
    if n <= limit:
      return comb(n, zero) % mod
    
    @lru_cache(None)
    def count(z: int, o: int, cnt: int, is_zero: bool) -> int:
      # print('iter:', (z, o), (cnt, is_zero))
      if z < 0 or o < 0 or cnt > limit:
        return 0

      if z == 0 and o == 0:
        return 1
      
      if z == 0:
        return 0 if o > limit else 1
      
      if o == 0:
        return 0 if z > limit else 1
      
      more = max(z, o)
      less = max(z, o)
      if more/less > limit:
        return 0
      
      i = (zero-z) + (one-o)
      if i == 0:
        prev_zero = -1
        prev_one = -1
      elif is_zero:
        prev_zero = i-1
        prev_one = i-cnt-1
      else:
        prev_zero = i-cnt-1
        prev_one = i-1
      
      if i-prev_zero > limit:
        # must be zero
        cnt = cnt+1 if is_zero else 1
        return count(z-1, o, cnt, True) if z > 0 else 0
      
      if i-prev_one > limit:
        # must be one
        cnt = cnt+1 if not is_zero else 1
        return count(z, o-1, cnt, False) if o > 0 else 0
      
      # can be either case
      zc = 0
      if z > 0:
        nc = cnt+1 if is_zero else 1
        zc = count(z-1, o, nc, True)
        
      oc = 0
      if o > 0:
        nc = cnt+1 if not is_zero else 1
        oc = count(z, o-1, nc, False)
        
      return (zc + oc) % mod
      
    return count(zero, one, 0, True)
    