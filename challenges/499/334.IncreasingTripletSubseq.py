'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:

1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
'''

from typing import List
import math


class Solution:
  def increasingTriplet(self, nums: List[int]) -> bool:
    stack = []
    n = len(nums)
    small = math.inf
    big = -math.inf
    
    for val in nums:
      stack.append(val > small)
      small = min(small, val)
      
    for i in range(n-1, 0, -1):
      val = nums[i]
      if val < big and small[i]:
        return True

      big = max(big, val)
      
    return False
    

  def increasingTriplet(self, nums: List[int]) -> bool:
    p0 = None
    p1 = None
    
    for n in nums:
      if p1 != None and n > p1:
        return True
      
      if p0 == None or n <= p0:
        p0 = n
        continue
        
      # n > p[0]
      if p1 == None or n <= p1:
        p1 = n
        
    return False
        
