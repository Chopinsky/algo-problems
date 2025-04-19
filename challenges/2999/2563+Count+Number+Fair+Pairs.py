'''
2563. Count the Number of Fair Pairs

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

Constraints:

1 <= nums.length <= 10^5
nums.length == n
-10^9 <= nums[i] <= 10^9
-10^9 <= lower <= upper <= 10^9
'''

from typing import List
from bisect import bisect_right, bisect_left


class Solution:
  def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    nums.sort()
    cnt = 0
    # print('init:', nums)

    for i, val in enumerate(nums):
      ldx = bisect_left(nums, lower-val)
      rdx = bisect_right(nums, upper-val)-1
      # print('found:', (i, val), (ldx, rdx))

      if rdx < ldx or ldx >= len(nums) or rdx < 0:
        continue

      c = rdx-ldx+1
      if ldx <= i <= rdx:
        c -= 1

      cnt += c

    return cnt//2
        
  def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    nums.sort()
    n = len(nums)
    total = 0
    
    for val in nums:
      lv, rv = lower-val, upper-val
      ldx = bisect_left(nums, lv)
      rdx = bisect_right(nums, rv)-1
      
      if 0 <= ldx <= rdx < n:
        total += rdx-ldx+1
        if lv <= val <= rv:
          total -= 1
        
    # print(total)
    return total // 2
    