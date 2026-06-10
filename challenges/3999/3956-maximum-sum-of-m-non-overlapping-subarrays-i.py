'''
3956-maximum-sum-of-m-non-overlapping-subarrays-i
'''

from typing import List
from math import inf
from collections import deque


class Solution:
  def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
    n = len(nums)
    pref = [0]*(n+1)
    for i in range(n):
      pref[i+1] = pref[i] + nums[i]

    dp_prev = [0] * (n+1)
    ans = -inf

    for _ in range(1, m+1):
      dp = [-inf] * (n+1)
      dq: deque[tuple[int, int]] = deque()

      for i in range(1, n+1):
        # add elements to the deque that are in the range
        j = i - l
        if j >= 0 and dp_prev[j] != -inf:
          val = dp_prev[j] - pref[j]

          # remove elements that are smaller than the current
          # best value
          while dq and dq[-1][1] <= val:
            dq.pop()

          dq.append((j, val))

        # remove elements out of the range
        j = i - r
        while dq and dq[0][0] < j:
          dq.popleft()

        # update the current best value in the subarray candidates
        dp[i] = dp[i-1]
        if dq:
          dp[i] = max(dp[i], pref[i] + dq[0][1])
      
      ans = max(ans, dp[i])
      dp_prev=dp

    return ans

  def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
    n = len(nums)

    pre = [0]*(n+1)
    for i in range(n):
      pre[i+1] = pre[i] + nums[i]
    
    dp = [[-inf]*(n+1) for _ in range(m+1)]
    for i in range(n+1):
      dp[0][i] = 0

    ans = -inf

    for k in range(1, m+1):
      dp[k][n] = 0
      dq = deque()

      for i in range(n-1, -1, -1):
        if i+l <= n:
          curr = pre[i+l] + dp[k-1][i+l]
          while dq:
            base = dq[-1]
            val = pre[base] + dp[k-1][base]
            if val >= curr:
              break

            dq.pop()

          dq.append(i+l)

        while dq and dq[0] > i+r:
          dq.popleft()

        dp[k][i] = dp[k][i+1]
        if dq:
          j = dq[0]
          dp[k][i] = max(
            dp[k][i],
            dp[k-1][j] + pre[j] - pre[i],
          )
    
      ans = max(ans, dp[k][0])

    # print('done:', ans)
    if ans == 0:
      base = -inf
      for i in range(n):
        for ln in range(l, r+1):
          if i+ln > n:
            break

          base = max(base, pre[i+ln]-pre[i])

      return base

    return ans
        