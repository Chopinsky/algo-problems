'''
3584-maximum-product-of-first-and-last-elements-of-a-subsequence
'''

from typing import List
from heapq import heappop


class Solution:
  def maximumProduct(self, nums: List[int], m: int) -> int:
      res = nums[0] * nums[-1]
      large, small = nums[0], nums[0]
      n = len(nums)
      
      for i in range(m-1, n):
        val = nums[i]
        large = max(large, nums[i-m+1])
        small = min(small, nums[i-m+1])
        res = max(res, val * (large if val > 0 else small))
      
      return res

  def maximumProduct(self, nums: List[int], m: int) -> int:
    maxp = nums[0]*nums[-1]
    small = sorted((val, i) for i, val in enumerate(nums))
    large = sorted((-val, i) for i, val in enumerate(nums))
    n = len(nums)

    for i in range(n):
      while small and small[0][1]-i+1 < m:
        heappop(small)

      while large and large[0][1]-i+1 < m:
        heappop(large)

      if not small or not large:
        break

      val = nums[i]
      maxp = max(maxp, val*small[0][0], -val*large[0][0])

    return maxp
