'''
3409-longest-subsequence-with-decreasing-adjacent-difference
'''

from typing import List


class Solution:
  def longestSubsequence(self, nums: List[int]) -> int:
    dp = [[0]*301 for _ in range(301)]
    seen = set()
    long = 0

    for val in nums:
      for v0 in range(300, 0, -1):
        if v0 not in seen:
          continue

        diff = abs(val-v0)
        dp[val][diff] = max(dp[val][diff], dp[v0][diff]+1)

      # accumulate on the best diff
      for diff in range(300, 0, -1):
        dp[val][diff-1] = max(dp[val][diff-1], dp[val][diff])

      long = max(long, dp[val][0])
      seen.add(val)

    return long+1
