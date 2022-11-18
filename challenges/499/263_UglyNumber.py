'''
263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:

-2^31 <= n <= 2^31 - 1
'''


class Solution:
  def isUgly(self, n: int) -> bool:
    if n <= 0:
      return False
    
    while n > 1:
      if n % 2 == 0:
        n //= 2
        continue
        
      if n % 3 == 0:
        n //= 3
        continue
        
      if n % 5 == 0:
        n //= 5
        continue
        
      return False
      
    return True
  