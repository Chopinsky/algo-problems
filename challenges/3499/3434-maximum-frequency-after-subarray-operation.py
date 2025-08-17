'''
3434-maximum-frequency-after-subarray-operation
'''

from typing import List
from collections import Counter


class Solution:
  def maxFrequency(self, nums: List[int], k: int) -> int:
    c = Counter(nums)

    def count(val: int):
      res = 0
      curr = 0

      for num in nums:
        if num == k:
          curr -= 1
        
        if num == val:
          curr += 1

        curr = max(curr, 0)
        res = max(res, curr)

      return res

    freq = max(count(val) for val in c)

    return c[k] + freq
