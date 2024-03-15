'''
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Constraints:

1 <= nums.length <= 3 * 10^4
nums[i] is either 0 or 1.
0 <= goal <= nums.length
'''

from typing import List


class Solution:
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    prefix = [-1]
    curr = 0
    count = 0
    
    for i in range(len(nums)):
      curr += nums[i]
      if nums[i] == 1:
        prefix.append(i)
        
      if curr < goal:
        continue
      
      v0 = curr - goal
      s = prefix[v0]
      e = prefix[v0+1] if len(prefix) > v0+1 else i
      count += e-s
      # print((i, curr), v0, prefix, e, s)
      
    return count
      
      
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    n = len(nums)
    count = 0
    
    if goal == 0:
      last = -1
      for i in range(n):
        if nums[i] == 1:
          last = i
        else:
          count += i - last
          
      return count
      
    prefix = [-1]
    curr = 0
    
    for i in range(n):
      if nums[i] == 1:
        prefix.append(i)
        curr += 1
        
      if curr - goal >= 0:
        count += prefix[curr-goal+1] - prefix[curr-goal]
    
    return count
  