'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
'''


from typing import List
from bisect import bisect_left


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    if n == 1:
      return 0 if nums[0] == target else -1
    
    if n == 2:
      if nums[0] == target:
        return 0
      
      if nums[1] == target:
        return 1
      
      return -1

    if target == nums[0]:
      return 0
    
    if target == nums[-1]:
      return n-1

    if nums[0] < nums[-1]:
      idx = bisect_left(nums, target)
      if idx < n and nums[idx] == target:
        return idx
      
      return -1
      
    def find_pvt() -> int:
      if nums[0] > nums[1]:
        return 0
      
      if nums[-1] < nums[-2]:
        return n-2

      l, r = 1, n-2
      pvt = -1

      while l <= r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
          pvt = mid
          break
        
        if nums[mid] > nums[0]:
          pvt = mid
          l = mid + 1
        else:
          r = mid - 1
        
      return pvt
      
    if nums[-1] < target < nums[0]:
      return -1
    
    p = find_pvt()
    offset = 0
    # print('pivot:', p, nums[:p+1], nums[p+1:])
    
    if nums[0] < target <= nums[p]:
      base = nums[:p+1]
    else:
      base = nums[p+1:]
      offset = p+1
      
    idx = bisect_left(base, target)
    # print('search:', base, idx)

    if idx < len(base) and base[idx] == target:
      return offset+idx

    return -1
        
        
  def search(self, nums: List[int], target: int) -> int:
    if nums[0] <= nums[-1]:
      idx = bisect_left(nums, target)
      return idx if (idx < len(nums) and nums[idx] == target) else -1
    
    l, r = 0, len(nums)-1
    
    while l < r:
      m = (l+r) // 2
      if nums[m] == target:
        return m
        
      # print(l, m, r, 'mid:', nums[m])
      
      if nums[l] < nums[r]:
        if nums[m] < target:
          l = m+1
        else:
          r = m-1
          
        continue
        
      if target > nums[m]:
        if nums[m] >= nums[l] or target <= nums[r]:
          l = m+1
        else:
          r = m-1
        
      else:
        if nums[m] < nums[l] or target >= nums[l]:
          r = m-1
        else:
          l = m+1
        
    if l < len(nums) and nums[l] == target:
      return l
    
    return -1
  