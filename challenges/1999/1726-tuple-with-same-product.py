'''
1726-tuple-with-same-product
'''

from typing import List
from collections import defaultdict


class Solution:
  def tupleSameProduct(self, nums: List[int]) -> int:
    pairs = defaultdict(int)
    n = len(nums)
    count = 0

    for i in range(n):
      v0 = nums[i]
      for j in range(i+1, n):
        res = v0*nums[j]
        # print('check:', res, pairs[res])

        if res in pairs:
          count += pairs[res]

        pairs[res] += 1

    return count*8
        