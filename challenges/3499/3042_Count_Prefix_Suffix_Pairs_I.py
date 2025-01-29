'''
3042. Count Prefix and Suffix Pairs I
'''

from typing import List


class Solution:
  def countPrefixSuffixPairs(self, words: List[str]) -> int:
    def is_prefix_suffix(a: str, b: str) -> bool:
      if len(b) < len(a):
        return False

      return b.startswith(a) and b.endswith(a)

    count = 0
    n = len(words)
    for i in range(n-1):
      for j in range(i+1, n):
        if is_prefix_suffix(words[i], words[j]):
          count += 1

    return count
        