'''
A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: n = 1, a = 2, b = 3
Output: 2
Example 2:

Input: n = 4, a = 2, b = 3
Output: 6
Example 3:

Input: n = 5, a = 2, b = 4
Output: 10
Example 4:

Input: n = 3, a = 6, b = 4
Output: 8
 

Constraints:

1 <= n <= 10^9
2 <= a, b <= 4 * 10^4
'''


from math import gcd


class Solution:
  def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
    mod = 1_000_000_007
    if a > b:
      a, b = b, a
      
    if a == b or a == 1 or a * n <= b:
      return (a * n) % mod
    
    l, r = b, a*n
    lcm = a * b // gcd(a, b)
    # print('init', a, b, lcm)
    
    while l < r:
      m = (l + r) // 2
      count = m//a + m//b - m//lcm
      # print(l, r, m, count)
      
      if (count == n) and (m%a == 0 or m%b == 0):
        return m % mod
      
      if count < n:
        l = m + 1
      else:
        r = m - 1
    
    return l % mod
  