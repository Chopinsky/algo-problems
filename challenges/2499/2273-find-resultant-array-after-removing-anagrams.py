'''
2273-find-resultant-array-after-removing-anagrams
'''

from collections import Counter
from typing import List, Dict


class Solution:
  def removeAnagrams(self, words: List[str]) -> List[str]:
    res = []
    n = len(words)
    pw = None
    prev = None

    def check(w: str, d: Dict) -> bool:
      if not prev or not pw:
        return False

      if len(w) != len(pw):
        return False

      if len(prev) != len(d):
        return False

      for ch in prev:
        if prev[ch] != d[ch]:
          return False

      return True

    for i in range(n):
      word = words[i]
      curr = Counter(word)
      if not check(word, curr):
        res.append(word)
        pw = word
        prev = curr

    return res
        