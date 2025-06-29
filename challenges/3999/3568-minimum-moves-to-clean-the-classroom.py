'''
3568-minimum-moves-to-clean-the-classroom
'''

from typing import List


class Solution:
  def minMoves(self, grid: List[str], energy: int) -> int:
    m, n = len(grid), len(grid[0])
    best = {}
    pos = {}
    count = 0
    start = None

    for x in range(m):
      for y in range(n):
        if grid[x][y] == 'L':
          pos[x, y] = 1 << count
          count += 1

        if grid[x][y] == 'S':
          start = (x, y)

    if count == 0 or start is None:
      return 0

    goal = (1 << count) - 1
    step = 0
    curr, nxt = [(start[0], start[1], energy, 0)], []
    best[start[0], start[1], 0] = energy
    # print('init:', pos, count, goal)

    while curr:
      step += 1
      # print('iter:', step, curr)

      for x, y, e, mask in curr:
        if e == 0:
          continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x0 = x+dx
          y0 = y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
            continue

          if grid[x0][y0] == 'X':
            continue

          ne = e-1
          if grid[x0][y0] == 'R':
            ne = energy

          if grid[x0][y0] == 'L':
            nxt_mask = mask | pos[x0, y0]
          else:
            nxt_mask = mask

          # print('move:', x0, y0, ne, nxt_mask, best)
          if nxt_mask == goal:
            return step

          if (x0, y0, nxt_mask) not in best or ne > best[x0, y0, nxt_mask]:
            best[x0, y0, nxt_mask] = ne
            nxt.append((x0, y0, ne, nxt_mask))

      curr, nxt = nxt, curr
      nxt.clear()

    return -1
        