'''
3654-minimum-sum-after-divisible-sum-deletions
'''

from typing import List
from math import inf


class Solution:
  def minArraySum(self, nums: List[int], k: int) -> int:
    if k == 1:
      return 0

    dp = [0] + [inf]*k
    curr = 0

    for val in nums:
      curr += val
      dp[curr%k] = min(dp[curr%k], curr)
      curr = dp[curr%k]

    return curr
        