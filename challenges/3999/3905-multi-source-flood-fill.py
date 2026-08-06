'''
3905-multi-source-flood-fill
'''


class Solution:
  def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
    g = [[0]*m for _ in range(n)]
    curr, nxt = set(), set()
    seen = set()

    for x, y, c in sources:
      # if 0 <= x < m and 0 <= y < n:
      g[x][y] = c
      curr.add((x, y))
      seen.add((x, y))

    while curr:
      for x0, y0 in curr:
        c0 = g[x0][y0]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x1, y1 = x0+dx, y0+dy
          if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
            continue

          if (x1, y1) in seen:
            continue

          g[x1][y1] = max(g[x1][y1], c0)
          nxt.add((x1, y1))

      curr, nxt = nxt, curr
      nxt.clear()
      seen |= curr

    return g
