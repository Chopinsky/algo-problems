'''
1362. Closest Divisors

Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
Example 2:

Input: num = 123
Output: [5,25]
Example 3:

Input: num = 999
Output: [40,25]

Constraints:

1 <= num <= 10^9
'''

from typing import List
from math import isqrt


class Solution:
  def closestDivisors(self, num: int) -> List[int]:
    def get(val: int):
      if val < 4:
        return [1, val]
      
      for v0 in range(isqrt(val), 1, -1):
        if val % v0 == 0:
          return [v0, val//v0]
          
      return [1, val]
      
    a = get(num+1)
    b = get(num+2)
    # print(num+1, a)
    # print(num+2, b)
    
    return a if abs(a[0]-a[1]) <= abs(b[0]-b[1]) else b
        