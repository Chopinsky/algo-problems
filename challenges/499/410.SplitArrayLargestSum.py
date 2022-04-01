'''
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9

Example 3:

Input: nums = [1,4,4], m = 3
Output: 4

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.length)
'''


from typing import List
from bisect import bisect_right
from functools import lru_cache
import math


class Solution:
  def splitArray(self, nums: List[int], m: int) -> int:
    n = len(nums)
    if m == n:
      return max(nums)
    
    presum = [nums[i] for i in range(n)]
    for i in range(1, n):
      presum[i] += presum[i-1]

    l = max(nums)
    r = presum[-1]
    last = r
    
    def check(arr_sum: int) -> bool:
      count = 0
      curr = 0
      i = 0

      while i <= n:
        if i == n:
          if curr > arr_sum:
            return False

          count += 1
          break

        if nums[i] > arr_sum:
          return False

        if curr+nums[i] > arr_sum:
          count += 1
          curr = nums[i]
        else:
          curr += nums[i]

        i += 1

      return count <= m

    # check if we can find less than `m` subarrays whose
    # sum is equal to or less than `sub_sum`, taking 
    def check0(sub_sum: int) -> bool:
      count = 1
      idx = bisect_right(presum, sub_sum) - 1
      
      # the first element is larger than `sub_sum`
      if idx < 0:
        return False
      
      # create the next subarray with greedy -- just find
      # the next subarray whose sum is the same or below `sub_sum`
      while idx < n-1:
        tgt = presum[idx] + sub_sum
        jdx = bisect_right(presum, tgt) - 1
        
        # next subarray won't fit in with even 1 element
        if jdx <= idx:
          return False
        
        # add the max-sized subarray with sum that equals or 
        # is smaller
        count += 1
        idx = jdx
        
        # need to create more subarrays than desired, skip
        if count > m:
          return False
      
      # if we can create less than `m` subarrays, this is a valid 
      # case
      return count <= m
    
    while l < r:
      mid = (l + r) // 2
      
      if check(mid):
        last = mid
        r = mid - 1
      else:
        l = mid + 1
        
    return l if (l < last and check(l)) else last
    
    
  def splitArray(self, nums: List[int], m: int) -> int:
    prefix = [val for val in nums]
    n = len(nums)
    
    for i in range(1, n):
      prefix[i] += prefix[i-1]
      
    @lru_cache(None)
    def dp(i: int, rem: int) -> int:
      if n-i == rem:
        return max(nums[i:])
      
      if rem == 1:
        return prefix[-1] - (prefix[i-1] if i > 0 else 0)
      
      right = n - rem
      curr = prefix[right] - (prefix[i-1] if i > 0 else 0)
      max_val = math.inf
      
      for j in range(right, i-1, -1):
        nxt_val = dp(j+1, rem-1)
        max_val = min(max_val, max(curr, nxt_val))
        if curr < nxt_val:
          break
          
        curr -= nums[j]
        
      return max_val
    
    return dp(0, m)
