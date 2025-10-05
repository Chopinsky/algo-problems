'''
3473-sum-of-k-subarrays-with-length-at-least-m
'''

from math import inf
from typing import List


class Solution:
  def maxSum(self, nums: List[int], k: int, m: int) -> int:
    n = len(nums)
    prefix = [val for val in nums]
    for i in range(1, n):
      prefix[i] += prefix[i-1]

    dp = [[-inf] * (k+1) for _ in range(n+1)]
    sub = [-inf] * (n+1)

    for i in range(n+1):
      dp[i][0] = 0

    for i in range(n-1, -1, -1):
      sub[i] = max(sub[i+1], prefix[i])

    for kk in range(1, k+1):
      for i in range(n-1, -1, -1):
        if i+m-1 < n:
          dp[i][kk] = max(
            dp[i+1][kk],
            sub[i+m-1] - (prefix[i-1] if i > 0 else 0)
          )
      
      sub = [-inf] * (n+1)
      for i in range(n-1, -1, -1):
        sub[i] = max(sub[i+1], prefix[i]+dp[i+1][kk])

    return max(dp[i][k] for i in range(n))
