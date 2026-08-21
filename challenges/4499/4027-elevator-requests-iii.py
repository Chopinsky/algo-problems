'''
4027-elevator-requests-iii
'''

from functools import cache


class Solution:
  def elevatorRequests(self, _n: int, start: int, req: list[list[int]]) -> int:
    n = len(req)

    @cache
    def dp(i: int, mask: int) -> int:
      t0, f0 = req[i]
      if mask == (1<<n) - 1:
        return max(abs(start-f0), t0)

      res = float("inf")
      for j in range(n):
        if mask & (1<<j): 
          continue

        _, f1 = req[j]
        tt = dp(j, mask|(1<<j))
        res = min(res, max(tt + abs(f1-f0), t0))

      return res

    return min(dp(i, 1<<i) for i in range(n))
