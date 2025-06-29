'''
2327-number-of-people-aware-of-a-secret
'''

from functools import cache


class Solution:
  def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    mod = 10**9+7

    @cache
    def dp(i: int) -> int:
      if i >= n:
        return 1 if i == n else 0

      cnt = 0
      for d in range(delay, forget):
        cnt += dp(min(n+1, i+d))

      if i+forget > n:
        cnt += 1

      return cnt % mod

    return dp(1)
