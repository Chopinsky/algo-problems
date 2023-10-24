'''
342. Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true

Constraints:

-2^31 <= n <= 2^31 - 1
'''


class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    s = bin(n)[2:]
    if s.count('1') > 1:
      return False
    
    if n < 4:
      return n == 1
    
    return (len(s)-1) % 2 == 0
        
        
  def isPowerOfFour(self, n: int) -> bool:
    if n == 1:
      return True
    
    num = 1
    while num < n:
      num <<= 2
      
    return num == n
      