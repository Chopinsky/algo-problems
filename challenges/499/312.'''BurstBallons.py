'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 500
0 <= nums[i] <= 100
'''


from typing import List
from functools import lru_cache


class Solution:
  def maxCoins0(self, nums: List[int]) -> int:
    if len(nums) > 1 and len(set(nums)) == 1:
      return (len(nums)-2) * pow(nums[0], 3) + pow(nums[0], 2) + pow(nums[0], 1)

    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for left in range(n-2, -1, -1):
      for right in range(left, n-1):
        for i in range(left, right+1):
          dp[left][right] = max(
            dp[left][right],
            nums[left-1]*nums[i]*nums[right+1] + dp[left][i-1] + dp[i+1][right]
          )

    return dp[1][n-2]
      
      
  def maxCoins(self, nums: List[int]) -> int:
    nums = [1] + nums + [1]
    # print(len(nums))
    
    @lru_cache(None)
    def burst(i: int, j: int) -> int:
      if i+1 >= j or i >= len(nums) or j < 0:
        return 0
      
      if i+1 == j-1:
        return nums[i]*nums[i+1]*nums[i+2]
      
      # optimization for a special case
      s = set(nums[i+1:j])
      if len(s) == 1:
        base = nums[i+1]
        return (j-i-3) * (base ** 3) + max(nums[i], nums[j]) * (base ** 2) + nums[i] * nums[j] * base
      
      most_coins = 0
      
      # i+1 and j are the boundary ballons that won't burst 
      # from this round, and k will be the last ballon to burst
      # in this section
      for k in range(i+1, j):
        coins = burst(i, k) + nums[i]*nums[k]*nums[j] + burst(k, j)
        most_coins = max(most_coins, coins)
        
      return most_coins
      
    return burst(0, len(nums)-1)
    