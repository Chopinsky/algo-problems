'''
3552-grid-teleportation-traversal
'''

from typing import List
from collections import defaultdict


class Solution:
  def minMoves(self, mat: List[str]) -> int:
    m, n = len(mat), len(mat[0])
    if m == 1 and n == 1:
      return 0

    step = 0
    best = {}
    seen = set()
    pos = defaultdict(list)
    curr, nxt = [], []

    for x in range(m):
      for y in range(n):
        if 'A' <= mat[x][y] <= 'Z':
          pos[mat[x][y]].append((x, y))

    if len(pos[mat[0][0]]) > 0:
      curr = pos[mat[0][0]].copy()
      seen.add(mat[0][0])
    else:
      curr.append((0, 0))

    for x, y in curr:
      if x == m-1 and y == n-1:
        return step
        
      best[x, y] = step

    # print('init:', pos, curr)
    while curr:
      step += 1
      # print('iter:', step, curr)

      for x0, y0 in curr:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x1, y1 = x0+dx, y0+dy
          if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
            continue

          if mat[x1][y1] == '#':
            continue

          if (x1, y1) in best and step >= best[x1, y1]:
            continue

          if 'A' <= mat[x1][y1] <= 'Z':
            if mat[x1][y1] in seen:
              continue

            seen.add(mat[x1][y1])
            for x2, y2 in pos[mat[x1][y1]]:
              if x2 == m-1 and y2 == n-1:
                return step

              nxt.append((x2, y2))
              best[x2, y2] = step
          
          else:
            if x1 == m-1 and y1 == n-1:
              return step

            nxt.append((x1, y1))
            best[x1, y1] = step

      curr, nxt = nxt, curr
      nxt.clear()

    return -1
        