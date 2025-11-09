'''
3743-maximize-cyclic-partition-score
'''

from typing import List
from itertools import accumulate
from math import inf


class Solution:
  def maximumScore(self, nums: List[int], k: int) -> int:
    n = len(nums)
    
    def solve(a: List) -> int:
      dp = list(accumulate(a, max))
      for i, lo in enumerate(accumulate(a, min)):
        dp[i] -= lo

      # base case: 1 partition
      ans = dp[n-1]

      for _ in range(k-1):
        # best score for 1 more partition
        ndp = [-inf] * n
        x = y = -inf

        for j in range(1, n):
          x = max(x, dp[j-1] - a[j])
          y = max(y, dp[j-1] + a[j])
          ndp[j] = max(ndp[j-1], x+a[j], y-a[j])

        dp = ndp
        ans = max(ans, dp[n-1])

      return ans

    j = nums.index(min(nums))
    a = [nums[(j+i)%n] for i in range(n)]
    b = [nums[(j+1+i)%n] for i in range(n)][::-1]

    return max(solve(a), solve(b))

