'''
3505-minimum-operations-to-make-elements-within-k-subarrays-equal
'''

from typing import List
from math import inf
from sortedcontainers import SortedList


class Solution:
  def minOperations(self, nums: List[int], x: int, k: int) -> int:
    n = len(nums)
    vals = [None]*n
    low = SortedList()
    high = SortedList()
    sl, sh = 0, 0

    for i, v in enumerate(nums):
      if not high or high[0] <= v:
        high.add(v)
        sh += v
      else:
        low.add(v)
        sl += v

      if i >= x:
        prev = nums[i-x]
        if prev >= high[0]:
          high.remove(prev)
          sh -= prev
        else:
          low.remove(prev)
          sl -= prev

      while len(high) > len(low)+1:
        val = high[0]
        high.remove(val)
        low.add(val)
        sh -= val
        sl += val

      while len(high) < len(low):
        val = low[-1]
        low.remove(val)
        high.add(val)
        sl -= val
        sh += val

      if i >= x-1:
        vals[i-x+1] = sh-sl-high[0]*(len(high) - len(low))

    dp = [[inf]*(k+1) for _ in range(n+1)]
    for i in range(n, -1, -1):
      dp[i][0] = 0
      for j in range(1, k+1):
        if n-i >= j*x:
          dp[i][j] = min(dp[i+1][j], vals[i] + dp[i+x][j-1])

    return dp[0][k]

