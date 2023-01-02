'''
2521. Distinct Prime Factors of Product of Array

Given an array of positive integers nums, return the number of distinct prime factors in the product of the elements of nums.

Note that:

A number greater than 1 is called prime if it is divisible by only 1 and itself.
An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.
 

Example 1:

Input: nums = [2,4,3,7,10,6]
Output: 4
Explanation:
The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7.
There are 4 distinct prime factors so we return 4.
Example 2:

Input: nums = [2,4,8,16]
Output: 1
Explanation:
The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 210.
There is 1 distinct prime factor so we return 1.

Constraints:

1 <= nums.length <= 10^4
2 <= nums[i] <= 1000
'''

from typing import List


class Solution:
  def distinctPrimeFactors(self, nums: List[int]) -> int:
    top = max(nums)
    s = [i for i in range(top+1)]
    
    for v0 in range(2, top+1):
      if s[v0] < v0:
        continue

      for v1 in range(v0*v0, top+1, v0):
        if s[v1] > v0:
          s[v1] = v0
    
    def get_factors(val: int):
      p = set()
      
      while s[val] > 1:
        p.add(s[val])
        val //= s[val]
        
      # print(p)
      return p
    
    primes = set()
    for val in nums:
      # print('check:', val)
      primes |= get_factors(val)
    
    return len(primes)
          