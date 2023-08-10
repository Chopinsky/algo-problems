'''
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
 
Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
'''

from typing import List
from bisect import bisect_left


class Solution:
  def search(self, nums: List[int], target: int) -> bool:
    l, r = 0, len(nums)-1
    
    while l <= r:
      mid = (l + r) // 2
      
      if nums[mid] == target or nums[l] == target or nums[r] == target:
        return True
      
      if nums[mid] > nums[r]:
        if nums[l] <= target <= nums[mid]:
          r = mid - 1
        else: 
          l = mid + 1
          
      elif nums[mid] < nums[r]:
        if nums[mid] <= target <= nums[r]:
          l = mid + 1
        else:
          r = mid - 1
          
      else:
        r -= 1
        
    return False
        
        
  def search(self, nums: List[int], target: int) -> bool:
    l = 0
    r = len(nums) - 1

    while l <= r:
      # print(l,r)
      mid = (l + r) // 2

      if nums[mid] == target:
        return True

      while l < mid and nums[l] == nums[mid]:
        l += 1
        
      if nums[l] <= nums[mid]:
        if nums[mid] > target >= nums[l]:
          r = mid - 1
        else:
          l = mid + 1
          
      else:
        if nums[r] >= target > nums[mid]:
          l = mid + 1
        else:
          r = mid - 1

    return False
      
      
  def search0(self, nums: List[int], target: int) -> bool:
    if not nums:
      return False
    
    n = len(nums)
    if nums[0] < nums[-1]:
      i = bisect_left(nums, target)
      return True if i < n and nums[i] == target else False
    
    pivot = 0
    for i in range(1, n):
      if nums[i] < nums[i-1]:
        pivot = i
        break
        
    # print(pivot)
    if pivot <= 0:
      i = bisect_left(nums, target)
      return True if i < n and nums[i] == target else False
    
    arr = nums[pivot:] if target <= nums[-1] else nums[:pivot]
    i = bisect_left(arr, target)
    
    return True if i < len(arr) and arr[i] == target else False
      
      