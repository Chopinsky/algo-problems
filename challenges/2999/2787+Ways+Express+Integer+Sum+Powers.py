'''
2787. Ways to Express an Integer as Sum of Powers

Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

Example 1:

Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
Example 2:

Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.

Constraints:

1 <= n <= 300
1 <= x <= 5
'''

from functools import lru_cache, cache


class Solution:
  def numberOfWays(self, n: int, x: int) -> int:
    mod = 1_000_000_007
    f = [0] * (n+1)
    f[0] = 1

    for k in range(1, n+1):
      v = k**x
      if v > n:
        break

      for j in range(n, v-1, -1):
        f[j] = (f[j] + f[j-v]) % mod
    
    return f[-1]


  def numberOfWays(self, n: int, x: int) -> int:
    cand = []
    mod = 10**9 + 7

    for base in range(1, n+1):
      val = pow(base, x)
      if val > n:
        break

      cand.append(val)

    ln = len(cand)
    suffix = [val for val in cand]
    for i in range(ln-2, -1, -1):
      suffix[i] += suffix[i+1]

    # print('init:', cand, suffix)

    @cache
    def dp(i: int, rem: int) -> int:
      # print('iter:', i, rem, suffix[i] if i < ln else 0)
      if rem == 0:
        return 1

      if i >= ln or rem < 0 or cand[i] > rem:
        return 0

      if rem >= suffix[i]:
        return 1 if rem == suffix[i] else 0
        
      c1 = dp(i+1, rem - cand[i])
      c2 = dp(i+1, rem)

      return (c1+c2) % mod

    return dp(0, n)


  def numberOfWays(self, n: int, x: int) -> int:
    mod = 10**9 + 7
    
    @lru_cache(None)
    def dp(rem: int, val: int) -> int:
      if val <= 1:
        return 1 if rem == 1 else 0
        
      base = val**x
      # print((rem, val), base)
      
      if rem == 1:
        return 1 if val >= 1 else 0
      
      if base >= rem:
        if base == rem:
          return (1 + dp(rem, val-1)) % mod
        
        top = get_top(rem)
        if top >= val:
          top -= 1
        
        return dp(rem, top)
      
      if val*base <= rem:
        return 0
      
      return (dp(rem-base, val-1) + dp(rem, val-1)) % mod
    
    @lru_cache(None)
    def get_top(val: int) -> int:
      if x == 1:
        return val
      
      if val == 1:
        return 1
      
      l, r = 2, val
      last = l
      
      while l <= r:
        mid = (l + r) // 2
        if mid**x <= val:
          last = mid
          l = mid+1
        else:
          r = mid-1
        
      return last
    
    top = get_top(n)
    # print('init', (n, x), top)
    
    return dp(n, top)
  