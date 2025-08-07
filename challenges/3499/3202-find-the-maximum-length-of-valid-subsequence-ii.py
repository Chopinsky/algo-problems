'''
3202-find-the-maximum-length-of-valid-subsequence-ii
'''

from typing import List
from collections import defaultdict


class Solution:
  def maximumLength(self, nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [defaultdict(int) for _ in range(n)]
    ln = 0

    for i in range(1, n):
      v0 = nums[i]
      for j in range(i):
        base = (v0 + nums[j]) % k
        if base in dp[j]:
          curr = 1 + dp[j][base]
        else:
          curr = 2

        dp[i][base] = max(dp[i][base], curr)
        ln = max(ln, dp[i][base])
    
    return ln
        