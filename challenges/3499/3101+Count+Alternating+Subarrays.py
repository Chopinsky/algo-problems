'''
3101. Count Alternating Subarrays

You are given a binary array nums.

We call a subarray alternating if no two adjacent elements in the subarray have the same value.

Return the number of alternating subarrays in nums.
'''

from typing import List

class Solution:
  def countAlternatingSubarrays(self, nums: List[int]) -> int:
    n = len(nums)
    i, j = 0, 0
    count = 0
    prev = -1
    
    while i < n:
      if j <= i:
        j = i
        prev = 1-nums[i]
      
      while j < n and 1-prev == nums[j]:
        prev = nums[j]
        j += 1
      
      count += j-i
      # print('iter:', (i, j))
      i += 1
      
    return count
        