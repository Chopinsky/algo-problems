'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Constraints:

2 <= n <= 58
'''

class Solution:
  '''
  another tricky math problem. the largest prod from (a, b) is when a and b are the closest
  number pair that adds to n. Essentially if n%2 == 1, a = n//2 and b = n//2+1, else a = b = n//2.
  keep dividing and we will find that all break-up numbers are 3s and the remainder of n%3 and 
  a 4 if that's what's left. 
  '''
  def integerBreak(self, n: int) -> int:
    if n <= 3:
      return n-1
    
    prod = 1
    while n > 4:
      prod *= 3
      n -= 3

    return prod*n
    