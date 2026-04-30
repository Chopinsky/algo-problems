'''
3742-maximum-path-score-in-a-grid
'''

from typing import List


class Solution:
  def maxPathScore(self, grid: List[List[int]], k: int) -> int:
    if k == 0 and grid[0][0] > 0:
      return -1

    m = len(grid)
    n = len(grid[0])
    prev = [[-1]*(k+1) for _ in range(n)]
    prev[0][k] = 0
    curr = []

    def get_left(j: int, k0: int) -> int:
      if j == 0 or not curr:
        return -1
      
      if grid[i][j] == 0:
        # free to enter
        return curr[-1][k0]

      # can't enter without paying
      return -1 if k0 == k else curr[-1][k0+1]

    def get_up(j: int, k0: int) -> int:
      if grid[i][j] == 0:
        # free to enter
        return prev[j][k0]

      # must pay 1 to enter
      return -1 if k0 == k else prev[j][k0+1]

    for i in range(m):
      for j in range(n):
        score = [-1]*(k+1)
        for k0 in range(k+1):
          left = get_left(j, k0)
          up = get_up(j, k0)
          best = max(left, up)
          if best < 0:
            continue

          score[k0] = grid[i][j] + best
        
        curr.append(score)

      # print('iter:', i, curr)
      curr, prev = prev, curr
      curr.clear()
    
    return max(prev[-1])
        