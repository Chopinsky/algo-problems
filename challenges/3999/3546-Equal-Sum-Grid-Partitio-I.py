'''
3546-Equal-Sum-Grid-Partitio-I
'''

from typing import List


class Solution:
  def canPartitionGrid(self, grid: List[List[int]]) -> bool:
    m = len(grid)
    n = len(grid[0])
    rows = [sum(row) for row in grid]
    cols = [sum(grid[i][j] for i in range(m)) for j in range(n)]
    total = sum(rows)

    # undividable
    if total%2 == 1:
      return False

    curr = 0
    for i in range(m-1):
      curr += rows[i]
      if curr*2 == total:
        return True

    curr = 0
    for j in range(n-1):
      curr += cols[j]
      if curr*2 == total:
        return True

    return False
        