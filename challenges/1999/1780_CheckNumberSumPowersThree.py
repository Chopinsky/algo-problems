'''
1780. Check if Number is a Sum of Powers of Three

Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 3^1 + 3^2
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 3^0 + 3^2 + 3^4
Example 3:

Input: n = 21
Output: false

Constraints:

1 <= n <= 10^7
'''

from functools import lru_cache, cache
from bisect import bisect_right


val = 1
cand = []

while val <= 10**7:
  cand.append(val)
  val *= 3

class Solution:
  def checkPowersOfThree(self, n: int) -> bool:
    # print('init:', cand)

    @cache
    def dp(val: int) -> bool:
      if val <= 1:
        return val == 1 or val == 0

      idx = bisect_right(cand, val)-1
      # print('check:', val, idx)
      if idx < 0:
        return False

      if val >= 2*cand[idx]:
        return False

      return dp(val-cand[idx])

    return dp(n)
        
  def checkPowersOfThree(self, n: int) -> bool:
    base = 1
    while base < n:
      base *= 3
      
    if base > n:
      base //= 3
      
    @lru_cache(None)
    def check(t: int, x: int) -> bool:
      if x == 1:
        return t == 1
      
      if t == 0 or t == 1 or x == t:
        return True
      
      if t > 3*x or t < 0 or x < 1:
        return False
      
      if check(t - x, x//3):
        return True
        
      return check(t, x//3)
      
    return check(n, base)
  
  