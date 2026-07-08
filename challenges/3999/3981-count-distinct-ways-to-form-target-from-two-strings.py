'''
3981-count-distinct-ways-to-form-target-from-two-strings
'''

from functools import cache


class Solution:
  def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
    mod = 10**9+7

    @cache
    def dfs(i: int, j: int, k: int) -> int:
      if k == len(target):
        return 1 if i and j else 0

      ans = 0
      for x in range(i, len(word1)):
        if word1[x] == target[k]:
          ans = (ans + dfs(x+1, j, k+1)) % mod

      for x in range(j, len(word2)):
        if word2[x] == target[k]:
          ans = (ans + dfs(i, x+1, k+1)) % mod

      return ans

    return dfs(0, 0, 0)
        