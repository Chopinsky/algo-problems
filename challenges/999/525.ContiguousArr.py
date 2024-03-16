'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
'''

from typing import List

class Solution:
  def findMaxLength(self, nums: List[int]) -> int:
    pos = {0:-1}
    curr = 0
    ln = 0
    
    for i, val in enumerate(nums):
      curr += 1 if val == 1 else -1
      if curr not in pos:
        pos[curr] = i
      else:
        ln = max(ln, i-pos[curr])
        
    return ln
        
  def findMaxLength(self, nums: List[int]) -> int:
    if 0 not in nums or 1 not in nums:
      return 0
      
    pos = {0:-1}
    balance = 0
    long = 0
    
    for i, val in enumerate(nums):
      if val == 1:
        balance += 1
      else:
        balance -= 1
        
      if balance in pos:
        long = max(long, i-pos[balance])
      else:
        pos[balance] = i
        
    return long
  