'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 2 * 105
-109 <= nums[i] <= 109
'''


from typing import List
import math


class Solution:
  def find132pattern(self, nums: List[int]) -> bool:
    stack = [nums[-1]]
    popped = -math.inf
    n = len(nums)
    
    for i in range(n-2, -1, -1):
      val = nums[i]
      # print(i, val, stack, popped)
      
      if val < popped:
        return True
      
      if val <= stack[-1]:
        if val != stack[-1]:
          stack.append(val)

        continue
        
      while stack and val > stack[-1]:
        popped = stack.pop()
        
      if not stack or val != stack[-1]:
        stack.append(val)
      
    return False
    