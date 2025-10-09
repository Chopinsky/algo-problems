'''
3704-count-no-zero-pairs-that-sum-to-n
'''

from functools import cache


class Solution:
  def countNoZeroPairs(self, n: int) -> int:
    ln = len(str(n))
    digits = [int(d) for d in str(n)][::-1]

    @cache
    def solve(pos: int, carry: int, l0: int, l1: int) -> int:
      if pos >= ln:
        return int(carry == 0)

      # if in range, then try 1->10, otherwise default to 0 (not in 
      # the number)
      r0 = range(1, 10) if pos < l0 else [0]
      r1 = range(1, 10) if pos < l1 else [0]
      ways = 0

      for d0 in r0:
        for d1 in r1:
          s0 = d0 + d1 + carry
          if s0 % 10 == digits[pos]:
            ways += solve(pos+1, s0//10, l0, l1)

      return ways

    pairs = 0
    for l0 in range(1, ln+1):
      for l1 in range(1, ln+1):
        pairs += solve(0, 0, l0, l1)

    return pairs
        