'''
3643-flip-square-submatrix-vertically
'''

from typing import List


class Solution:
  def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
    right = y+k
    x0 = x
    x1 = x+k-1

    while x1 > x0:
      for yy in range(y, right):
        # print('swap:', (x0, x1), yy)
        grid[x0][yy], grid[x1][yy] = grid[x1][yy], grid[x0][yy]

      x0 += 1
      x1 -= 1

    return grid
        