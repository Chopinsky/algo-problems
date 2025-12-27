'''
3381-maximum-subarray-sum-with-length-divisible-by-k
'''

from typing import List


class Solution:
  def maxSubarraySum(self, nums: List[int], k: int) -> int:
    rem = [None] * k
    prefix = 0
    res = sum(nums[:k])

    for i, val in enumerate(nums):
      prefix += val

      if i < k:
        rem[i] = prefix
      else:
        r = i % k
        res = max(res, prefix-rem[r])
        rem[r] = min(rem[r], prefix)

      if (i+1)%k == 0:
        res = max(res, prefix)

    return res

