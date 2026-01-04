'''
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0
 

Constraints:

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5
'''

from typing import List
from math import isqrt
from functools import cache


class Solution:
  def sumFourDivisors(self, nums: List[int]) -> int:
    @cache
    def cnt(val: int) -> bool:
      c = 0
      s = 0

      for v0 in range(1, isqrt(val)+1):
        if v0*v0 > val:
          break

        if val%v0 == 0:
          c += 1
          s += v0

          if val//v0 != v0:
            s += val//v0
            c += 1

        if c > 4:
          break

      return s if c == 4 else 0
        
    total = 0

    for val in nums:
      total += cnt(val)

    return total

  def sumFourDivisors(self, nums: List[int]) -> int:
    def sive(n: int) -> List[int]:
      s = [i for i in range(n+1)]
      for i in range(2, n+1):
        if s[i] < i:
          continue
          
        for j in range(i*i, n+1, i):
          if s[j] > i:
            s[j] = i
            
      return s
    
    s = sive(max(nums))
    sums = 0
    # print(s)
    
    for val in nums:
      if val < 6 or s[val] == val:
        continue
        
      d0 = s[val]
      d1 = val // d0
      
      # the next 2 divisors are the only ones
      if (s[d1] == d1 or (s[d1] == d0 and d1 == d0*d0)) and d0 != d1:
        # print('found:', val, d0, d1, s[d1])
        sums += 1 + val + d0 + d1
    
    return sums
  