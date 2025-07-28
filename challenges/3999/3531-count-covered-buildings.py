'''
3531-count-covered-buildings
'''

from collections import defaultdict
from typing import List


class Solution:
  def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
    r = defaultdict(list)
    c = defaultdict(list)

    for x, y in buildings:
      r[x].append(y)
      c[y].append(x)

    for i in list(r):
      vals = set(r[i])
      r[i] = [min(vals), max(vals)]

    for i in list(c):
      vals = set(c[i])
      c[i] = [min(vals), max(vals)]

    count = 0
    # print('init:', r, c)

    for x, y in buildings:
      yl, yh = r[x]
      xl, xh = c[y]
      # print('check:', (xl, x, xh), (yl, y, yh))
      if xl < x < xh and yl < y < yh:
        count += 1

    return count

        