'''
2900-longest-unequal-adjacent-groups-subsequence-i
'''

from typing import List


class Solution:
  def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
    curr = -1
    ans = []
    n = len(words)

    for i in range(n):
      w = words[i]
      d = groups[i]

      if d != curr:
        curr = d
        ans.append(w)

    return ans
    