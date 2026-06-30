'''
1967-number-of-strings-that-appear-as-substrings-in-word
'''

from typing import List


class Solution:
  def numOfStrings(self, patterns: List[str], word: str) -> int:
    return sum(1 if w in word else 0 for w in patterns)
        