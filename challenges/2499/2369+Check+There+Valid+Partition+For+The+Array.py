'''
2369. Check if There is a Valid Partition For The Array

You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.

Example 1:

Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.
Example 2:

Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.

Constraints:

2 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
'''

from typing import List


class Solution:
  def validPartition(self, nums: List[int]) -> bool:
    n = len(nums)
    if n < 2:
      return False
    
    states = [False]*n
    states[-2] = nums[-1] == nums[-2]
    
    for i in range(n-3, -1, -1):
      if nums[i] == nums[i+1]:
        states[i] |= states[i+2]
        
      if (nums[i] == nums[i+1] and nums[i] == nums[i+2]) or (nums[i]+1 == nums[i+1] and nums[i]+2 == nums[i+2]):
        states[i] |= states[i+3] if i+3 < n else True
       
    # print(states)
    return states[0]
        
        
  def validPartition(self, nums: List[int]) -> bool:
    n = len(nums)
    dp = [False] * n
    
    for i in range(n-2, -1, -1):
      if nums[i] == nums[i+1] and (i == n-2 or dp[i+2]):
        dp[i] = True
        continue
        
      if (i < n-2 and nums[i] == nums[i+1] == nums[i+2]) and (i == n-3 or dp[i+3]):
        dp[i] = True
        continue
        
      if (i < n-2 and nums[i]+2 == nums[i+1]+1 == nums[i+2]) and (i == n-3 or dp[i+3]):
        dp[i] = True
    
    # print(dp)
    return dp[0]
    