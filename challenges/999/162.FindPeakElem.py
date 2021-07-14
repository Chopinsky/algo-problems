'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:

1 <= nums.length <= 1000
-2 ** 31 <= nums[i] <= 2 ** 31 - 1
nums[i] != nums[i + 1] for all valid i.
'''


import math
from typing import List


class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    ln = len(nums)
    if ln == 1 or nums[0] > nums[1]:
      return 0
      
    if nums[-1] > nums[-2]:
      return ln-1
    
    nums = [-math.inf] + nums + [-math.inf]
    l, r = 1, ln+1
    
    while l < r:
      mid = (l+r) // 2
      # print(mid, l, r)
      
      if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
        return mid-1
      
      if nums[mid-1] < nums[mid] < nums[mid+1]:
        l = mid+1
      else:
        r = mid-1
        
    # print("done:", l-1)
    return l-1
      