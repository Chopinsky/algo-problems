'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 10 ** 4
-10 ** 9 <= nums[i] <= 10 ** 9
-10 ** 9 <= target <= 10 ** 9
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''


from typing import List
from bisect import bisect_left


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    memo = {}
    for i, n in enumerate(nums):
      if (target - n) in memo:
        return [memo[target-n], i]

      memo[n] = i

    return None

  def twoSum0(self, nums: List[int], target: int) -> List[int]:
    nums = [(n, i) for i, n in enumerate(nums)]
    nums.sort()
    
    # print(nums)
    
    for j, (n, i) in enumerate(nums):
      if j > 0 and nums[j-1][0] == n:
        continue
        
      val = target - n
      if val == n:
        if j < len(nums)-1 and nums[j+1][0] == val:
          # print("1", j, target, n, val)
          return [min(i, nums[j+1][1]), max(i, nums[j+1][1])]
        
        continue
      
      pos = bisect_left(nums, (val, ))
      if pos < len(nums) and nums[pos][0] == val:
        # print("2", i, pos, target, n, val)
        return [min(i, nums[pos][1]), max(i, nums[pos][1])]
      
    return None