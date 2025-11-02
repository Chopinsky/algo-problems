'''
3588-find-maximum-area-of-a-triangle
'''

from typing import List
from collections import defaultdict


class Solution:
  def maxArea(self, coords: List[List[int]]) -> int:
    rows = defaultdict(list)
    cols = defaultdict(list)

    for x, y in coords:
      if y not in rows:
        rows[y] = [x, x]
      else:
        rows[y][0] = min(rows[y][0], x)
        rows[y][1] = max(rows[y][1], x)
      
      if x not in cols:
        cols[x] = [y, y]
      else:
        cols[x][0] = min(cols[x][0], y)
        cols[x][1] = max(cols[x][1], y)

    min_y, max_y = min(rows), max(rows)
    min_x, max_x = min(cols), max(cols)
    area = -1

    for y in rows:
      base = rows[y][1] - rows[y][0]
      height = max(max_y-y, y-min_y)
      a0 = base*height
      # print('rows:', y, base, height, a0)

      if a0 > 0:
        area = max(area, a0)

    for x in cols:
      base = cols[x][1] - cols[x][0]
      height = max(max_x-x, x-min_x)
      a0 = base*height
      # print('cols:', y, base, height, a0)

      if a0 > 0:
        area = max(area, a0)

    return area
