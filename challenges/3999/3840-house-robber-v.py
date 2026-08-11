'''
3840-house-robber-v
'''

from typing import List


class Solution:
  def rob(self, nums: List[int], colors: List[int]) -> int:
    def seg_rob(l: int, r: int) -> int:
      if l < 0 or r < 0:
        return 0

      if l == r:
        return nums[l]

      ln = r-l+1
      dp = [[0, 0] for _ in range(ln+1)]
      
      for i in range(ln):
        prev = dp[i]
        val = nums[l+i]

        # rob house-i, must no rob house-(i-1)
        dp[i+1][1] = val + prev[0]

        # do not rob house-i, can take the best
        # value from prev
        dp[i+1][0] = max(prev)

      # print('iter:', dp)
      return max(dp[-1])

    total = 0
    prev = -1
    start = -1
    n = len(colors)

    for i, c in enumerate(colors):
      if c != prev:
        total += seg_rob(start, i-1)
        # print('add:', (start, i-1), seg_rob(start, i-1))
        prev = c
        start = i

    # count the tail segment
    total += seg_rob(start, n-1)

    return total
