'''
3563-lexicographically-smallest-string-after-adjacent-removals

test if we can remove s[i:j+1] and recursively check all intervals
'''

from functools import cache


class Solution:
  def lexicographicallySmallestString(self, s: str) -> str:
    n = len(s) 
    a = [ord(ch)-ord('a') for ch in s]
    print('init:', n, a)

    @cache
    def empty(i: int, j: int) -> bool:
      # check if we can remove s[i:j+1]
      if i > j:
        return True

      # can remove
      if abs(a[i] - a[j]) in [1, 25] and empty(i+1, j-1):
        return True

      return any(empty(i, k) and empty(k+1, j) for k in range(i+1, j, 2))

    @cache
    def dp(i: int) -> str:
      if i == n:
        return ""

      ans = s[i] + dp(i+1)
      for j in range(i+1, n, 2):
        # if we can remove s[i:j+1]
        if empty(i, j):
          ans = min(ans, dp(j+1))

      return ans

    return dp(0)
