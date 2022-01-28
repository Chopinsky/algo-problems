'''
Given an integer n, return the largest palindromic integer 
that can be represented as the product of two n-digits integers. 
Since the answer can be very large, return it modulo 1337.

Example 1:

Input: n = 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
Example 2:

Input: n = 1
Output: 9

Constraints:

1 <= n <= 8
'''


from heapq import heappush, heappop


class Solution:
  def largestPalindrome(self, n: int) -> int:
    # Math
    # https://medium.com/@d_dchris/largest-palindrome-product-problem-brilliant-approach-using-mathematics-python3-leetcode-479-b3f2dd91b1aa
    if n == 1: 
      return 9

    for z in range(2, 2 * (9 * 10**n) - 1):
      left = 10**n - z
      right = int(str(left)[::-1])
      root_1, root_2 = 0, 0
    
      # no root
      if z**2 - 4*right < 0:
        continue

      # at least one root
      else:
        root_1 = 1/2 * (z + (z**2-4*right)**0.5)
        root_2 = 1/2 * (z - (z**2-4*right)**0.5)
      
        if root_1.is_integer() or root_2.is_integer():
          return ((10**n) * left + right) %1337


  def largestPalindrome0(self, n: int) -> int:
    mod = 1337
    max_val = pow(10, n) - 1
    min_val = max_val - pow(10, (n+1) >> 1)
    
    def is_pal(val: int) -> bool:
      vs = str(val)
      l, r = 0, len(vs)-1
      
      while l < r:
        if vs[l] != vs[r]:
          return False
        
        l += 1
        r -= 1
        
      return True
    
    pq = []
    for i in range(max_val, min_val, -1):
      r = i % 10
      
      if r == 3 or r == 7:
        heappush(pq, (-i*i, i, i))
      elif r == 1:
        heappush(pq, (-i*(i-2), i, i-2))
      elif r == 9:
        heappush(pq, (-i*(i-8), i, i-8))
        
    while pq:
      prod, a, b = heappop(pq)
      prod = -prod
      
      if is_pal(prod):
        return prod % mod
      
      if b > min_val:
        b -= 10
        heappush(pq, (-a*b, a, b))
    
    return 0
      