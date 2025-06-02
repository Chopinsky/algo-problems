'''
2901-longest-unequal-adjacent-groups-subsequence-ii
'''

from functools import cache
from typing import List


class Solution:
  def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
    n = len(words)

    def is_valid(i: int, j: int) -> bool:
      if i < 0:
        return True

      if groups[i] == groups[j]:
        return False

      if len(words[i]) != len(words[j]):
        return False

      cnt = 0
      for k in range(len(words[i])):
        if words[i][k] != words[j][k]:
          cnt += 1

        if cnt > 1:
          return False

      return cnt == 1

    @cache
    def dp(i: int, prev: int):
      if i >= n:
        return tuple()

      if not is_valid(prev, i):
        return dp(i+1, prev)

      l1 = dp(i+1, prev)
      l2 = tuple([words[i]] + list(dp(i+1, i)))

      return l1 if len(l1) > len(l2) else l2
    
    return dp(0, -1)
