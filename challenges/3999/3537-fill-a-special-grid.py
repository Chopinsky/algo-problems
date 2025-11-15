'''
3537-fill-a-special-grid
'''

from typing import List


class Solution:
  def specialGrid(self, n: int) -> List[List[int]]:
    ln = 1<<n
    grid = [[0]*ln for _ in range(ln)]

    def produce(x: int, y: int, size: int, low: int, high: int):
      if low == high or size == 1:
        grid[x][y] = low
        return

      half = size // 2
      delta = (high-low+1) // 4

      # top-right
      produce(x, y+half, half, low, low+delta-1)

      # bottom-right
      produce(x+half, y+half, half, low+delta, low+2*delta-1)

      # bottom-left
      produce(x+half, y, half, low+2*delta, low+3*delta-1)

      # top-left
      produce(x, y, half, low+3*delta, high)

    produce(0, 0, ln, 0, (1<<2*n)-1)

    return grid
        