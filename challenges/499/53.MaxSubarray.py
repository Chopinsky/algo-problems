'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

1 <= nums.length <= 3 * 10^4
-105 <= nums[i] <= 105
'''


from typing import List


class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    prefix = [n for n in nums]
    n = len(nums)
    low = nums[0]
    ans = nums[0]
    
    for i in range(1, n):
      prefix[i] += prefix[i-1]
      ans = max(ans, prefix[i] - min(0, low))
      low = min(low, prefix[i])
          
    return ans