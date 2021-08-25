'''
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false

Example 3:

Input: c = 4
Output: true

Example 4:

Input: c = 2
Output: true

Example 5:

Input: c = 1
Output: true

Constraints:

0 <= c <= 2 ** 31 - 1
'''


from math import floor, sqrt, isqrt


class Solution:
  '''
  Fermat's Theorem:

  Any positive number nn is expressible as a sum of two squares 
  if and only if the prime factorization of n, every prime of 
  the form (4k+3) occurs an even number of times.
  '''
  def judgeSquareSum(self, c: int) -> bool:
    for i in range(2, floor(sqrt(c))+1):
      count = 0
      
      if c % i == 0:
        while c % i == 0:
          c //= i
          count += 1
          
        if i % 4 == 3 and count % 2 != 0:
          return 
        
    return c % 4 != 3
    
    
  def judgeSquareSum0(self, c: int) -> bool:
    if c <= 5:
      return c != 3
    
    h = floor(sqrt(c/2))
    # print(c, h)
    
    for n in range(h+1):
      tgt = c - n*n
      if isqrt(tgt) ** 2 == tgt:
        return True
    
    return False
    