'''
3533-Concatenated-Divisibility
'''

from typing import List


class Solution:
  def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    p10 = [pow(10, len(str(x)), k) for x in nums]
    dp = [{} for _ in range(1<<n)]
    dp[0][0] = []

    for mask in range(1<<n):
      for rem, seq in list(dp[mask].items()):
        for i in range(n):
          # seen
          if mask & (1<<i) > 0:
            continue

          nxt_mask = mask | (1<<i)
          nxt_rem = (rem*p10[i] + nums[i]) % k
          cand = seq + [nums[i]]

          if nxt_rem not in dp[nxt_mask] or cand < dp[nxt_mask][nxt_rem]:
            dp[nxt_mask][nxt_rem] = cand

    return dp[(1<<n)-1].get(0, [])
          