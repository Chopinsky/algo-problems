'''
1023-camelcase-matching
'''

from typing import List
from functools import cache


class Solution:
  def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
    @cache
    def is_cap(ch: str) -> bool:
      return 'A' <= ch <= 'Z'

    def check(src: str, pt: str) -> bool:
      i, j = 0, 0

      while i < len(src) and j < len(pt):
        c0 = src[i]
        c1 = pt[j]

        if c0 == c1:
          j += 1
        elif is_cap(c0):
          return False

        i += 1

      return j >= len(pt) and all(not is_cap(ch) for ch in src[i:])

    return [check(w, pattern) for w in queries]
        