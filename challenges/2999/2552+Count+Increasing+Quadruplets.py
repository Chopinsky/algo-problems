'''
2552. Count Increasing Quadruplets

Given a 0-indexed integer array nums of size n containing all numbers from 1 to n, return the number of increasing quadruplets.

A quadruplet (i, j, k, l) is increasing if:

0 <= i < j < k < l < n, and
nums[i] < nums[k] < nums[j] < nums[l].

Example 1:

Input: nums = [1,3,2,4,5]
Output: 2
Explanation: 
- When i = 0, j = 1, k = 2, and l = 3, nums[i] < nums[k] < nums[j] < nums[l].
- When i = 0, j = 1, k = 2, and l = 4, nums[i] < nums[k] < nums[j] < nums[l]. 
There are no other quadruplets, so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Explanation: There exists only one quadruplet with i = 0, j = 1, k = 2, l = 3, but since nums[j] < nums[k], we return 0.

Constraints:

4 <= nums.length <= 4000
1 <= nums[i] <= nums.length
All the integers of nums are unique. nums is a permutation.
'''

from typing import List
from bisect import bisect_left, insort


class Solution:
  def countQuadruplets(self, nums: List[int]) -> int:
    n = len(nums)
    left_vals = [nums[0]]
    cnt = 0
    
    def count_pairs(i: int) -> int:
      base = nums[i]
      if base <= 2 or base == n:
        return 0
      
      r, rc = n-1, 0
      total = 0
      # print('count:', base, left_vals)
      
      while r > i:
        if nums[r] < base:
          lc = bisect_left(left_vals, nums[r])
          if lc > 0:
            total += lc * rc
        
        else:
          rc += 1
          
        # print('move right:', nums[r], rc)
        r -= 1
      
      return total
    
    for i in range(1, n-1):
      cnt += count_pairs(i)
      insort(left_vals, nums[i])
      
    return cnt
    