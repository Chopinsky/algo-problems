'''
3430. Maximum and Minimum Sums of at Most Size K Subarrays
'''

from typing import List
from functools import lru_cache


class Solution:
  def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    nextBig = [n] * n
    prevBig = [-1] * n
    nextSmall = [n] * n
    prevSmall = [-1] * n
    bStack = []
    sStack = []

    #monotonic stack 4 times
    for i in range(n):
      val = nums[i]

      while bStack and bStack[-1][-1] < val:
        j, _ = bStack.pop()
        nextBig[j] = i

      while sStack and sStack[-1][-1] > val:
        j, _ = sStack.pop()
        nextSmall[j] = i

      bStack.append((i, val))
      sStack.append((i, val))

    bStack.clear()
    sStack.clear()

    for i in range(n-1, -1, -1):
      val = nums[i]
      
      while bStack and bStack[-1][-1] <= val:
        j, _ = bStack.pop()
        prevBig[j] = i

      while sStack and sStack[-1][-1] >= val:
        j, _ = sStack.pop()
        prevSmall[j] = i
        
      bStack.append((i, val))
      sStack.append((i, val))

    @lru_cache(None)
    def count_subarr(before: int, after: int):
      firstBeforeLimit = before - (k - after)
      excluded = 0.

      # for each idx before firstBeforeLimit, each will have 
      # 1, 2, 3, ..., firstBeforeLimit counts of choices that
      # needs to be excluded
      if firstBeforeLimit > 1:
        excluded = firstBeforeLimit * (firstBeforeLimit - 1) // 2 
        
      return before*after - excluded
    
    ans = 0
    for idx, val in enumerate(nums):
      after = min(nextBig[idx]-idx, k)
      before = min(idx-prevBig[idx], k)
      ans += val * count_subarr(before, after)
      
      after = min(nextSmall[idx]-idx, k)
      before = min(idx-prevSmall[idx], k)
      ans += val * count_subarr(before, after)
    
    return ans
