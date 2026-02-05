'''
3665-twisted-mirror-path-count
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  def uniquePaths(self, grid: List[List[int]]) -> int:
    n = len(grid[0])
    curr_row = [0] * n
    curr_row[0] = 1

    for row in grid:
      prev_row, curr_row, prev_cell = curr_row, [0]*n, 0
      
      for idx, p in enumerate(prev_row):
        if row[idx] == 0:
          curr_row[idx] = prev_cell + p # above+left
          prev_cell = prev_cell + p     # above+left
        else:
          curr_row[idx] = prev_cell # from left
          prev_cell = p             # from above

    return curr_row[-1] % 1_000_000_007

  def uniquePaths(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    mod = 10**9 + 7

    score = {(0, 0): 1}
    cand = [(0, 0, 0)]
    dirs = [(0, 1), (1, 0)]
    seen = set([(0, 0)])

    def travel(x0: int, y0: int, d: int):
      if x0 >= m or y0 >= n:
        return (-1, -1)

      x1 = x0 + dirs[d][0]
      y1 = y0 + dirs[d][1]

      if x1 >= m or y1 >= n:
        return (-1, -1)

      if grid[x1][y1] == 0:
        return x1, y1

      return travel(x1, y1, (d+1)%2)

    while cand:
      _, x0, y0 = heappop(cand)
      s0 = score[x0, y0]
      # print('iter:', (x0, y0), s0)

      # to the right
      x1, y1 = travel(x0, y0, 0)
      # print('t1:', (x1, y1))
      if x1 >= 0 and y1 >= 0:
        score[x1, y1] = (s0 + score.get((x1, y1), 0)) % mod
        if (x1, y1) not in seen:
          heappush(cand, (x1+y1, x1, y1))
          seen.add((x1, y1))

      # to the down
      x2, y2 = travel(x0, y0, 1)
      # print('t2:', (x2, y2))
      if x2 >= 0 and y2 >= 0:
        score[x2, y2] = (s0 + score.get((x2, y2), 0)) % mod
        if (x2, y2) not in seen:
          heappush(cand, (x2+y2, x2, y2))
          seen.add((x2, y2))

    return score.get((m-1, n-1), 0)
        