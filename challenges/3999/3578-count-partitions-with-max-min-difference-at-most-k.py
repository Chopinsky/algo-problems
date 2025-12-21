'''
3578-count-partitions-with-max-min-difference-at-most-k
'''


from typing import List
from collections import deque


class Solution:
  def countPartitions(self, nums: List[int], k: int) -> int:
    mod = 10**9 + 7
    n = len(nums)
    dp = [1] + [0]*n
    acc = 1
    minq = deque()
    maxq = deque()
    i = 0

    for j in range(n):
      # maintain maxq
      while maxq and nums[j] > nums[maxq[-1]]:
        maxq.pop()
      maxq.append(j)

      # maintain minq
      while minq and nums[j] < nums[minq[-1]]:
        minq.pop()
      minq.append(j)

      # print('iter:', maxq, minq)
      while minq and maxq and nums[maxq[0]] - nums[minq[0]] > k:
        # shift the left pole of the window by 1
        acc = (acc - dp[i]) % mod
        i += 1

        while minq and minq[0] < i:
          minq.popleft()

        while maxq and maxq[0] < i:
          maxq.popleft()

      dp[j+1] = acc
      acc = (acc+dp[j+1]) % mod

    return dp[n]


        