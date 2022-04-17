'''
implement binary search on a sorted array
'''

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    if not nums or target < nums[0] or target > nums[-1]:
      return -1
    
    l, r = 0, len(nums)
    while l < r:
      m = (l + r) // 2
      if nums[m] == target:
        l = m
        break
        
      if nums[m] < target:
        l = m + 1
      else:
        r = m - 1
        
    return l if nums[l] == target else -1
  
      