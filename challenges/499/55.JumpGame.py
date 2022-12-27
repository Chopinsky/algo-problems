'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''


from typing import List


class Solution:
  def canJump(self, nums: List[int]) -> bool:
    forward = 0
    n = len(nums)
    
    for i in range(n):
      if i > forward:
        return False
      
      forward = max(forward, i+nums[i])
      if forward >= n-1:
        break
      
    return True

    
  def canJump(self, nums: List[int]) -> bool:
    idx = 0
    for i, n in enumerate(nums):
      if i > idx:
        break
        
      idx = max(idx, i+n)
      if idx >= len(nums)-1:
        return True
      
    return False
    