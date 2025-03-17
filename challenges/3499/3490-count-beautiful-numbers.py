'''
3490-count-beautiful-numbers
'''

from functools import lru_cache


class Solution:
  def beautifulNumbers(self, l: int, r: int) -> int:
    def count(x: int):
      if x <= 10:
        return x

      digits = [int(ch) for ch in str(x)]
      n = len(digits)
      
      @lru_cache(None)
      def dp(pos, tight, started, has_zero, s, p):
        if pos >= n:
          if not started:
            return 0
              
          if has_zero:
            return 1

          return 1 if (p % s == 0) else 0

        cnt = 0
        limit = digits[pos] if tight else 9
        
        if started and has_zero and not tight:
          return 10 ** (n-pos)
        
        for d in range(0, limit+1):
          nxt_tight = tight and (d == limit)
          if not started:
            if d == 0:
              cnt += dp(pos+1, nxt_tight, False, False, 0, 1)
            else:
              cnt += dp(pos+1, nxt_tight, True, False, d, d)

          else:
            cnt += dp(pos+1, nxt_tight, True, has_zero or d == 0, s+d, p*d)

        return cnt
      
      return dp(0, True, False, False, 0, 1)
        
    return count(r) - count(l-1)
      