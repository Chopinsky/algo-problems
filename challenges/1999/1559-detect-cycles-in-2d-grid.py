'''
1559-detect-cycles-in-2d-grid
'''

from typing import List


class Solution:
  def containsCycle(self, grid: List[List[str]]) -> bool:
    seen = set()
    chain = {}
    m, n = len(grid), len(grid[0])

    def nxt(x0: int, y0: int, s: int):
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x1, y1 = x0+dx, y0+dy
        if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
          continue

        if grid[x1][y1] != grid[x0][y0]:
          continue

        if (x1, y1) in chain and s-chain[x1, y1] > 1:
          # print('found:', chain, (x0, y0), (x1, y1))
          return (x1, y1), True

        if (x1, y1) in seen:
          continue

        return (x1, y1), False

      return None, False

    def check(x: int, y: int) -> bool:
      curr = [(x, y, 0)]
      chain.clear()
      chain[x, y] = 0
      seen.add((x, y))

      while curr:
        x, y, s = curr[-1]
        nxt_move, done = nxt(x, y, s)
        if done:
          return True

        if nxt_move is None:
          curr.pop()
          del chain[x, y]
          continue

        seen.add(nxt_move)
        chain[nxt_move] = s+1
        curr.append((nxt_move[0], nxt_move[1], s+1))

      return False

    for x in range(m):
      for y in range(n):
        if check(x, y):
          return True

    return False
