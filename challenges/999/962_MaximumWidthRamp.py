'''
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.

Constraints:

2 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 5 * 10^4
'''

from typing import List
from bisect import bisect_left


class Solution:
  def maxWidthRamp(self, nums: List[int]) -> int:
    cand = sorted((val, i) for i, val in enumerate(nums))
    ramp = 0
    low = cand[0][1]
    # print(cand)
    
    for _, i in cand[1:]:
      if i > low:
        ramp = max(ramp, i-low)
        
      low = min(low, i)
      
    return ramp  
        
  def maxWidthRamp(self, nums: List[int]) -> int:
    stack = []
    width = 0
    
    for i in range(len(nums)-1, -1, -1):
      val = nums[i]
      if not stack or val > stack[-1][0]:
        stack.append((val, i))
        continue
        
      j = bisect_left(stack, (val, ))
      if j < len(stack):
        _, k = stack[j]
        width = max(width, k-i)
        
    return width
      
