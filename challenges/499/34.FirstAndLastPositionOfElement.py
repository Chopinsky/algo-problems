'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
'''

from typing import List
from bisect import bisect_left, bisect_right


class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    if not nums:
      return [-1, -1]
    
    idx = bisect_left(nums, target)
    if idx >= len(nums) or nums[idx] != target:
      return [-1, -1]
    
    jdx = bisect_right(nums, target) - 1
    
    return [idx, jdx]
    

  def searchRange(self, nums: List[int], target: int) -> List[int]:
    ln = len(nums)
    if ln == 0 or target < nums[0] or target > nums[-1]:
      return [-1, -1]

    l, r = bisect_left(nums, target), bisect_right(nums, target)
    if nums[l] != target:
      return [-1, -1]

    return [l, r-1]
