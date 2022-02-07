'''
Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by an integer and add all these numbers. The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.

Return True if the array is good otherwise return False.

Example 1:

Input: nums = [12,5,7,23]
Output: true
Explanation: Pick numbers 5 and 7.
5*3 + 7*(-2) = 1

Example 2:

Input: nums = [29,6,10]
Output: true
Explanation: Pick numbers 29, 6 and 10.
29*1 + 6*(-3) + 10*(-1) = 1

Example 3:

Input: nums = [3,6]
Output: false

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
'''


from typing import List
from math import gcd


class Solution:
  '''
  use Bézout's lemma, we know that it is possible to find integer factors (x, y), such that
  a * x + b * y == gcd(a, b), so we just generate all possible gcd(a, b), where a is the 
  gcd results of nums[:i], and b == nums[i], if we can obtain gcd(a, b) == 1, then we find
  the combo (i.e. all numbers that are staked to generate a, and nums[i]); another trick to 
  avoid TLE is only store the gcd results, because smaller number (i.e. the gcd of 2 numbers)
  is always better than the original number, as we're racing to 1.
  '''
  def isGoodArray(self, nums: List[int]) -> bool:
    if 1 in nums:
      return True
    
    # nums = sorted(set(nums), reverse=True)
    vals, nxt = set([nums[0]]), set()
    
    for v0 in nums[1:]:
      # if only use v0
      nxt.add(v0)
      # print(v0, vals)
      
      for v1 in vals:
        g = gcd(v0, v1)
        if g == 1:
          # print(v0, v1)
          return True
        
        nxt.add(g)
        
      vals, nxt = nxt, vals
      nxt.clear()
      
    return False
  