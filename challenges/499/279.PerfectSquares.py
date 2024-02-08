'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is 
the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect 
squares while 3 and 11 are not.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:

1 <= n <= 10^4
'''

from math import isqrt
from collections import deque

class Solution:
  def numSquares(self, n: int) -> int:
    nums = []
    cnt = [float('inf')] * (n+1)
    val = 1
    
    while val*val <= n:
      nums.append(val*val)
      cnt[val*val] = 1
      val += 1
      
    for v0 in range(1, n+1):
      for v1 in nums:
        if v0+v1 > n:
          break
          
        cnt[v0+v1] = min(cnt[v0+v1], 1+cnt[v0])
    
    # print(nums, cnt)
    
    return cnt[-1]
        
        
  def numSquares(self, n: int) -> int:
    base = set()
    val = 1
    root = isqrt(n)
    if root*root == n:
      return 1
      
    while val*val <= n:
      if val*val == n:
        return 1
      
      base.add(val*val)
      if n - val*val in base:
        return 2
      
      val += 1
      
    # print(base)
    
    #Legendre's three-square theorem O(log(n)) presumably
    while n > 0 and n%4 == 0:
      n //= 4
        
    if n % 8 != 7:
      return 3
    
    #Lagrange's four-square theorem
    return 4
    

  def numSquares(self, n: int) -> int:
    def is_square(n: int) -> bool:
      s = isqrt(n)
      return s*s == n
    
    if is_square(n):
      return 1
    
    hashmap = set()
    ceiling = isqrt(n)
    
    for i in range(ceiling+1):
      hashmap.add(i*i)
      if (n - i*i) in hashmap:
        return 2

   #Legendre's three-square theorem O(log(n)) presumably
    while n > 0 and n%4 == 0:
      n //= 4
        
    if n % 8 != 7:
      return 3
    
    #Lagrange's four-square theorem
    return 4
      
    
  def numSquares0(self, n: int) -> int:
    if n == 1:
      return 1
    
    base = [i*i for i in range(1, isqrt(n)+1)]
    stack = deque([(val, 1) for val in base[::-1]])
    count = {}
    
    while stack:
      # print(stack)
      curr, cnt = stack.popleft()
      if (curr in count) and (count[curr] <= cnt):
        continue
      
      if curr == n:
        return cnt
      
      count[curr] = cnt
      
      for val in base[::-1]:
        nxt = curr + val
        if nxt > n:
          continue
          
        stack.append((nxt, cnt+1))
    
    return 0
  
