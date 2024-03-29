'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:

Input: nums = [1], target = 0
Output: 0

Constraints:

1 <= nums.length <= 10 ** 4
-10 ** 4 <= nums[i] <= 10 ** 4
nums contains distinct values sorted in ascending order.
-10 ** 4 <= target <= 10 ** 4
'''

from typing import List
from bisect import bisect_left

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    n = len(nums)
    l, r = 0, len(nums)
    idx = r
    
    while l <= r:
      mid = (l + r) // 2
      # print(l, r)
      
      if mid >= n or nums[mid] == target:
        idx = mid
        break
        
      if nums[mid] < target:
        l = mid + 1
      else:
        idx = mid
        r = mid - 1
    
    return idx
    
    
  def searchInsert(self, nums: List[int], target: int) -> int:
    if target <= nums[0]:
      return 0

    if target > nums[-1]:
      return len(nums)

    return bisect_left(nums, target)
