'''
3729-count-distinct-subarrays-divisible-by-k-in-sorted-array
'''

from typing import List
from collections import Counter


class Solution:
  def numGoodSubarrays(self, nums: List[int], k: int) -> int:
    c = Counter([0])
    pre = 0
    res = 0

    for val in nums:
      pre = (pre+val) % k
      res += c[pre]
      c[pre] += 1

    for val, ln in Counter(nums).items():
      # print('iter:', val, ln)
      for subln in range(1, ln):
        if (subln*val) % k == 0:
          # remove duplicate counts
          res -= (ln - subln)

    return res
        