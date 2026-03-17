'''
3873-maximum-points-activated-with-one-addition
'''


class Solution:
  def maxActivated(self, points: list[list[int]]) -> int:
    n = len(points)
    p = list(range(n))
    size = [1]*n

    def find(x: int) -> int:
      while p[x] != x:
        x = p[x]

      return x

    def union(x: int, y: int):
      gx, gy = find(x), find(y)
      if gx == gy:
        return

      if size[gx] < size[gy]:
        gx, gy = gy, gx

      p[gy] = gx
      size[gx] += size[gy]

    rows = {}
    cols = {}

    for i, (x, y) in enumerate(points):
      if x in rows:
        union(i, rows[x])
      else:
        rows[x] = i

      if y in cols:
        union(i, cols[y])
      else:
        cols[y] = i

    g = [size[i] for i in range(n) if p[i] == i]
    g.sort()
    # print('done:', g)

    return 1+g[-1] if len(g) == 1 else 1+g[-1]+g[-2]
