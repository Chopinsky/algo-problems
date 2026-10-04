'''
678-valid-parenthesis-string
'''

from functools import cache


class Solution:
  def checkValidString(self, s: str) -> bool:
    n = len(s)

    @cache
    def dp(i: int, bal: int) -> bool:
      if i >= n:
        return bal == 0

      if bal < 0:
        return False

      if s[i] == ')':
        return dp(i+1, bal-1)

      if s[i] == '(':
        return dp(i+1, bal+1)

      return dp(i+1, bal) or dp(i+1, bal+1) or dp(i+1, bal-1)

    return dp(0, 0)
        