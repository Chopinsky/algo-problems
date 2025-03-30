'''
3500-minimum-cost-to-divide-array-into-subarrays
'''

from typing import List


class Solution:
  def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
    n = len(nums)
    pn = nums.copy()
    pc = cost.copy()
    for i in range(1, n):
      pn[i] += pn[i-1]
      pc[i] += pc[i-1]

    dp = [[None]*n for _ in range(n)]

    def find(s: int, e: int, k: int) -> int:
      if dp[s][e] is not None:
        return dp[s][e]

      left = k + (pn[e] if s == 0 else pn[e]-pn[s-1])
      right = pc[n-1] if s == 0 else pc[n-1]-pc[s-1]
      res = left * right

      if e == n-1:
        dp[s][e] = res
        return res

      res += find(e+1, e+1, k)
      res = min(res, find(s, e+1, k))
      dp[s][e] = res

      return res

    return find(0, 0, k)
    