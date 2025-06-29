'''
2099-find-subsequence-of-length-k-with-the-largest-sum
'''

from typing import List
from heapq import heappop


class Solution:
  def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    h = sorted((nums[i], i) for i in range(n))
    while len(h) > k:
      heappop(h)

    seq = sorted(h, key=lambda x: x[1])

    return [v[0] for v in seq]
        