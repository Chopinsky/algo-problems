'''
3000-maximum-area-of-longest-diagonal-rectangle
'''

from math import sqrt
from typing import List


class Solution:
  def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
    diag = 0
    area = 0

    for x, y in dimensions:
      d0 = sqrt(x*x + y*y)
      if d0 > diag:
        area = x*y
        diag = d0

      elif d0 == diag:
        area = max(area, x*y)


    return area
        