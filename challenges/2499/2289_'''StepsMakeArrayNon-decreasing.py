'''
2289. Steps to Make Array Non-decreasing

You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.

Return the number of steps performed until nums becomes a non-decreasing array.

Example 1:

Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3
Explanation: The following are the steps performed:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]
[5,7,11,11] is a non-decreasing array. Therefore, we return 3.
Example 2:

Input: nums = [4,5,7,7,13]
Output: 0
Explanation: nums is already a non-decreasing array. Therefore, we return 0.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
'''

from typing import List


class Solution:
  '''
  the idea is to identify the rounds to eliminate all the smaller numbers to 
  the right of this number: we iterate from right to left, then use the mono-decreasing
  stack to identify all numbers that can be consumed to the right -- and the right number
  could have already consumed more numbers already, so we take the max count between
  the 2 -- the current rounds to consume all previous numbers, and the rounds for the right
  number to consume smaller numbers from it.
  '''
  def totalSteps(self, nums: List[int]) -> int:
    n = len(nums)
    stack = []
    count = [0] * len(nums)
    
    for i in range(n-1, -1, -1):
      while stack and nums[i] > nums[stack[-1]]:
        j = stack.pop()
        count[i] = max(1+count[i], count[j])
      
      stack.append(i)
        
    return max(count)
    