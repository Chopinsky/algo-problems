'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

Example 4:

Input: n = 4
Output: true

Example 5:

Input: n = 5
Output: false

Constraints:

-2 ** 31 <= n <= 2 ** 31 - 1

Follow up: Could you solve it without loops/recursion?
'''

class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
      return False

    return n & (n-1) == 0
        
  def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
      return False
    
    while n > 1:
      if n%2 != 0:
        return False
      
      n >>= 1
      
    return True
        
  def isPowerOfTwo1(self, n: int) -> bool:
    if n <= 0:
      return False

    if n <= 2:
      return True

    while n > 0:
      if n & 1 > 0 and n > 1:
        return False

      n >>= 1

    return True
