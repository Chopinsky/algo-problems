'''
2698. Find the Punishment Number of an Integer

Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

1 <= i <= n
The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.

Example 1:

Input: n = 10
Output: 182
Explanation: There are exactly 3 integers i that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182
Example 2:

Input: n = 37
Output: 1478
Explanation: There are exactly 4 integers i that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478

Constraints:

1 <= n <= 1000
'''

from functools import cache


class Solution:
  @cache
  def calc(self, val: int) -> int:
    if val == 1:
      return True

    base = val*val
    s = str(base)

    @cache
    def dp(s: str, rem: int, is_head: bool) -> bool:
      # print('iter:', val, s, rem)
      if not s:
        return rem == 0

      if rem <= 0:
        return rem == 0 and int(s) == 0

      if int(s) < rem:
        return False

      if int(s) == rem and not is_head:
        return True
      
      base = 0
      n = len(s)
      end = n if not is_head else n-1

      for i in range(end):
        base = 10*base + int(s[i])
        if base > rem:
          return False

        if dp(s[i+1:], rem-base, False):
          return True

      return False

    return base if dp(s, val, True) else 0

  def punishmentNumber(self, n: int) -> int:
    return sum(self.calc(val) for val in range(1, n+1))
        
  def punishmentNumber(self, n: int) -> int:
    known = set([1, 9, 10, 36])
    
    def div(s: str, tgt: int, top: bool) -> bool:
      if s == '':
        return tgt == 0
      
      if tgt == 0:
        return s == '0'*len(s)
      
      if s[0] == '0':
        return div(s[1:], tgt, False)
      
      if int(s) < tgt:
        return False
      
      if not top and int(s) == tgt:
        return True
      
      n = len(s)
      for i in range(n-1):
        curr = int(s[:i+1])
        # if top and tgt == 100:
        #   print(curr, tgt, s[i+1:], div(s[i+1:], tgt-curr, False))
        
        if curr == tgt:
          return s[i+1:] == '0'*(n-i-1)
        
        if curr > tgt:
          break
        
        if div(s[i+1:], tgt-curr, False):
          return True
        
      return False
      
    total = 0
    
    for val in range(1, n+1):
      if val <= 36:
        if val in known:
          total += val*val
          
      else:
        sqr = val*val
        if div(str(sqr), val, True):
          # print('adding:', val)
          total += sqr
    
    return total
        