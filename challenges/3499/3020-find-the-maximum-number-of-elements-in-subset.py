'''
3020-find-the-maximum-number-of-elements-in-subset
'''

from typing import List
from collections import Counter
from math import isqrt


class Solution:
  def maximumLength(self, nums: List[int]) -> int:
    c = Counter(nums)
    bound = isqrt(max(c))+1
    ln = 1
    seen = set()

    def get_len(v: int) -> int:
      if v == 1:
        seen.add(v)
        return c[v] if c[v]%2 == 1 else c[v]-1

      cnt = 0
      while v in c and c[v] > 1:
        cnt += 2
        seen.add(v)
        v *= v

      if v in c and c[v] == 1:
        cnt += 1
        seen.add(v)
      else:
        cnt -= 1

      return cnt

    for val in sorted(c):
      if val > bound:
        break

      if val in seen:
        continue

      ln = max(ln, get_len(val))

    return ln

        