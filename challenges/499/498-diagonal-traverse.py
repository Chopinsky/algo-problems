'''
498-diagonal-traverse
'''

from typing import List


class Solution:
  def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    m = len(mat)
    n = len(mat[0])
    if m == 1:
      return mat[0]

    if n == 1:
      return [row[0] for row in mat]

    res = []
    x, y = 0, 0
    dx, dy = -1, 1

    while len(res) < m*n:
      # print('append:', (x, y))
      res.append(mat[x][y])

      x += dx
      y += dy

      # out of the grid, turning point
      if x < 0 or x >= m or y < 0 or y >= n:
        if dx > 0:
          if x >= m:
            x = m-1
            y += 2

          else:
            y = 0

        else:
          if y >= n:
            x += 2
            y = n-1

          else:
            x = 0

        dx *= -1
        dy *= -1

    return res

        