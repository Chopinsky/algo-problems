'''
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:

n == nums.length
1 <= n <= 10^4
-10^5 <= nums[i] <= 10^5
'''

from typing import List


class Solution:
  def checkPossibility(self, nums: List[int]) -> bool:
    idx = -1
    n = len(nums)
    
    for i in range(1, n):
      if nums[i] < nums[i-1]:
        if idx >= 0:
          return False
        
        idx = i
    
    # print(stack)
    if idx < 0:
      return True
    
    def check(idx):
      # print('check:', idx)
      if n-1 > idx > 0 and nums[idx-1] > nums[idx+1]:
        return False
      
      return True
    
    return check(idx) or check(idx-1)


  def checkPossibility(self, nums: List[int]) -> bool:
    pos = -1
    for i in range(len(nums)-1):
      n0, n1 = nums[i], nums[i+1]
      if n0 > n1:
        if pos >= 0:
          return False

        pos = i

    # p = pos[0]
    if pos == 0 or pos == len(nums)-1:
      return True

    # print(pos)

    return (nums[pos] <= nums[pos+2]) or (pos > 0 and nums[pos-1] <= nums[pos+1])
