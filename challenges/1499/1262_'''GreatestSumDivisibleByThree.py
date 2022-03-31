'''
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
'''

from typing import List


class Solution:
  def maxSumDivThree(self, nums: List[int]) -> int:
    dp = [0, 0, 0]
    for val in nums[::-1]:
      mod = val % 3
      if mod == 0:
        d0 = dp[0] + val
        d1 = dp[1] + val if dp[1] > 0 else 0
        d2 = dp[2] + val if dp[2] > 0 else 0
        
      elif mod == 1:
        d1 = max(dp[1], dp[0]+val)
        d2 = max(dp[2], dp[1]+val) if dp[1] > 0 else dp[2]
        d0 = max(dp[0], dp[2]+val) if dp[2] > 0 else dp[0]
      
      else:
        d2 = max(dp[2], dp[0]+val)
        d1 = max(dp[1], dp[2]+val) if dp[2] > 0 else dp[1]
        d0 = max(dp[0], dp[1]+val) if dp[1] > 0 else dp[0]
        
      dp[0] = d0
      dp[1] = d1
      dp[2] = d2
      
    # print(dp)
    return dp[0]
  