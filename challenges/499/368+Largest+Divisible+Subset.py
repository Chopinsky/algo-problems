'''
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
'''


from typing import List


class Solution:
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    nums.sort()
    dp = [[1, -1] for _ in range(len(nums))]
    top = [1, 0]
    
    for i, val in enumerate(nums):
      if i == 0:
        continue
        
      for j in range(i):
        if (val % nums[j] == 0) and (dp[i][0] < dp[j][0]+1):
          dp[i][0] = dp[j][0] + 1
          dp[i][1] = j
          
      if dp[i][0] > top[0]:
        top[0] = dp[i][0]
        top[1] = i

    idx = top[1]
    ans = []
    # print(dp)
    
    while idx >= 0:
      ans.append(nums[idx])
      idx = dp[idx][1]
      # print(idx)
      
    return ans
  