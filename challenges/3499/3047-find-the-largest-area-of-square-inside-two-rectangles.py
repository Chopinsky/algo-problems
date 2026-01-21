'''
3047-find-the-largest-area-of-square-inside-two-rectangles
'''

from typing import List


class Solution:
  def largestSquareArea(self, bl: List[List[int]], tr: List[List[int]]) -> int:
    n = len(bl)
    rect = [bl[i]+tr[i] for i in range(n)]
    area = 0
    # print('init:', rect)

    def ol(a: List, b: List) -> int:
      x0, y0, x1, y1 = a
      x2, y2, x3, y3 = b

      # no overlaps
      if y3 <= y0 or x3 <= x0 or x1 <= x2 or y1 <= y2:
        return 0

      bx = max(x0, x2)
      by = max(y0, y2)
      tx = min(x1, x3)
      ty = min(y1, y3)

      l0 = tx-bx
      l1 = ty-by
      if l0 <= 0 or l1 <= 0:
        return 0

      ln = min(l0, l1)

      return ln*ln

    for i in range(n-1):
      for j in range(i+1, n):
        area = max(area, ol(rect[i], rect[j]))

    return area
        