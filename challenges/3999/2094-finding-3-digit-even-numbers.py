'''
2094-finding-3-digit-even-numbers
'''

from typing import List
from collections import Counter


class Solution:
  def findEvenNumbers(self, digits: List[int]) -> List[int]:
    base = Counter(digits)
    vals = set(d for d in base if d%2 == 0)

    def is_valid(val: int) -> bool:
      dc = Counter(int(d) for d in str(val))
      # print('check:', val, dc)

      for d, c in dc.items():
        if d not in base or c > base[d]:
          return False

      return True

    round = 0
    nxt = set()
    # print('init:', vals, base)

    while vals and round < 2:
      round += 1
      mult = pow(10, round)

      for d in base:
        for val in vals:
          nxt_val = mult*d + val
          if not is_valid(nxt_val):
            continue

          nxt.add(nxt_val)

      # print('iter:', round, nxt)
      vals, nxt = nxt, vals
      nxt.clear()

    return sorted(val for val in vals if val >= 100)
        