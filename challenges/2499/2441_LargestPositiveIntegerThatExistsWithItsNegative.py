'''
2441. Largest Positive Integer That Exists With Its Negative

Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.
Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0
'''

from typing import List

class Solution:
  def findMaxK(self, nums: List[int]) -> int:
    negatives = set(val for val in nums if val < 0)
    positives = sorted(val for val in nums if val > 0)
    
    while positives:
      val = positives.pop()
      if -val in negatives:
        return val 
    
    return -1
  
  def findMaxK(self, nums: List[int]) -> int:
    base = set(nums)
    
    for val in sorted(nums, reverse=True):
      if val <= 0:
        break
      
      if -val in base:
        return val
        
    return -1
        