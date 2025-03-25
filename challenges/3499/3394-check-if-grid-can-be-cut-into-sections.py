'''
3394-check-if-grid-can-be-cut-into-sections
'''

from typing import List


class Solution:
  def checkValidCuts(self, n: int, rect: List[List[int]]) -> bool:
    x_segs = []
    y_segs = []

    for x0, y0, x1, y1 in rect:
      x_segs.append((x1, -1))
      x_segs.append((x0, 1))
      y_segs.append((y1, -1))
      y_segs.append((y0, 1))

    x_segs.sort()
    y_segs.sort()
    xc = 0
    yc = 0
    xlines = 0
    ylines = 0
    # print('init:', x_segs, y_segs)

    for i, (_, tp) in enumerate(x_segs):
      xc += tp
      # print('x-check:', tp, xc)

      if xc == 0 and i != len(x_segs)-1:
        xlines += 1

      if xlines >= 2:
        return True

    for i, (_, tp) in enumerate(y_segs):
      yc += tp
      # print('y-check:', tp, yc)

      if yc == 0 and i != len(y_segs)-1:
        ylines += 1

      if ylines >= 2:
        return True

    return False
        