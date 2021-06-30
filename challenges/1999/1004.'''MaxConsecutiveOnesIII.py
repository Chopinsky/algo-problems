'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:

1 <= nums.length <= 10 ** 5
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

from typing import List

class Solution:
  '''
  idea is the sliding window, and we shall make sure that in range [i, j), there can only 
  be at most k zeros inside, then the goal is to find the longest such range.
  '''
  def longestOnes(self, nums: List[int], k: int) -> int:
    n = len(nums)
    l, r = 0, 0
    longest = k 
    
    if k == 0:
      while l < n:
        if nums[l] == 0:
          l += 1
          r = l
          continue
          
        while r < n and nums[r] == 1:
          r += 1
          
        longest = max(longest, r-l)
        # print(longest, l, r)
        l = r+1
        r = l
        
      return longest
    
    c0 = 0
    
    while l < n:
      while r < n:
        if nums[r] == 0:
          if c0 == k:
            break
            
          c0 += 1
          
        r += 1
        
      wl = r-l
      # print("pair:", l, r, c0, wl)
      
      if wl > longest:
        longest = wl
        
      if nums[l] == 0:
        c0 -= 1
        
      l += 1
      if l > r:
        r = l
        
      # won't get more
      if n-l < longest:
        break
        
    # print("done:", longest)
    
    return longest
      