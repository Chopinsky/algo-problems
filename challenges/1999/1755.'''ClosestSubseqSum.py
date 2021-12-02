'''
You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

Example 1:

Input: nums = [5,-7,3,5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.

Example 2:

Input: nums = [7,-9,15,-2], goal = -5
Output: 1
Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.

Example 3:

Input: nums = [1,2,3], goal = -7
Output: 7

Constraints:

1 <= nums.length <= 40
-107 <= nums[i] <= 10^7
-109 <= goal <= 10^9
'''


from typing import List
from bisect import bisect_left
from itertools import combinations
import math


class Solution:
  def minAbsDifference(self, nums: List[int], goal: int) -> int:
    def build_sums(src: List[int]) -> List[int]:
      base = set([0])
      for num in src:
        nxt = {num+s for s in base}
        base |= nxt
        
      return list(base)

    l_sum, r_sum = build_sums(nums[::2]), sorted(build_sums(nums[1::2]))
    r_ln = len(r_sum)
    result = math.inf
    
    for num in l_sum:
      target = goal - num
      
      # only if target is in range for a better solution
      if r_sum[0]-target >= result or target-result >= r_sum[-1]:
        continue
              
      # get where we can find the smallest diff abs
      idx = bisect_left(r_sum, target)

      # check neighboring index as well for better abs solution
      for i in [idx-1, idx, idx+1]:
        if i < 0 or i >= r_ln:
          continue

        result = min(result, abs(target - r_sum[i]))
        if result == 0:
          return 0

    return result
  
  
  def minAbsDifference0(self, nums: List[int], goal: int) -> int:
    n = len(nums)
    diff = abs(goal)
    
    if n == 1:
      return min(diff, abs(goal-nums[0]))
    
    def get_sums(arr: List[int]) -> List[int]:
      nonlocal diff
      
      sums = set()
      ln = len(arr)
      
      src = [i for i in range(ln)]
      
      for l in range(1, ln+1):
        for sub in combinations(src, l):
          s0 = 0
          for i in sub:
            s0 += arr[i]
            
          sums.add(s0)

      res = sorted(sums)
      for s0 in res:
        diff = min(diff, abs(goal - s0))
      return res
      
    mid = n // 2
    l, r = get_sums(nums[:mid]), get_sums(nums[mid:])
    # print(l, r)
    
    for s0 in l:
      idx = bisect_left(r, goal-s0)
      if idx < len(r):
        diff = min(diff, abs(goal-(s0+r[idx])))
        
      if idx < len(r)-1:
        diff = min(diff, abs(goal-(s0+r[idx+1])))
        
      if idx > 0:
        diff = min(diff, abs(goal-(s0+r[idx-1])))
      
    return diff
      