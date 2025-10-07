'''
3380-maximum-area-rectangle-with-point-constraints-i
'''

from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right


class Solution:
  def maxRectangleArea(self, points: List[List[int]]) -> int:
    xs = defaultdict(list)
    points.sort()

    for x, y in points:
      xs[x].append(y)

    area = -1
    cand = sorted(xs)
    n = len(cand)
    # print('init:', cand, xs)

    for i in range(n):
      x0 = cand[i]
      l0 = len(xs[x0])
      if l0 < 2:
        continue

      for j in range(l0-1):
        y0, y1 = xs[x0][j], xs[x0][j+1]

        for j in range(i+1, n):
          x1 = cand[j]
          ycand = xs[x1]
          low_idx = bisect_left(ycand, y0)
          high_idx = bisect_right(ycand, y1)-1

          # no intersections
          if low_idx > high_idx or low_idx >= len(ycand) or high_idx < 0:
            continue

          if low_idx+1 == high_idx and ycand[low_idx] == y0 and ycand[high_idx] == y1:
            area = max(area, (x1-x0)*(y1-y0))

          break

    return area
