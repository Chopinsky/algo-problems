'''
3291-minimum-number-of-valid-strings-to-form-target-i
'''

from typing import List
from functools import cache
import math


class Solution:
  def minValidStrings(self, words: List[str], target: str) -> int:
    root = {}
    ln = []

    def add(w: str):
      curr = root
      for ch in w:
        if ch not in curr:
          curr[ch] = {}

        curr = curr[ch]

    def count(w: int) -> int:
      curr = root
      ln = 0
      for ch in w:
        if ch not in curr:
          break

        curr = curr[ch]
        ln += 1

      return ln

    @cache
    def dp(i: int) -> int:
      if i >= len(target):
        return 0

      if ln[i] == 0:
        return -1

      curr = math.inf
      for l in range(ln[i]):
        j = i+l+1
        nxt = dp(j)
        if nxt < 0:
          continue

        curr = min(curr, 1+nxt)

      return -1 if curr == math.inf else curr

    for w in words:
      add(w)

    for i in range(len(target)):
      ln.append(count(target[i:]))
    
    # print('init:', root, ln)

    return dp(0)
