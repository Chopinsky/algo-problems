'''
4016-maximum-area-of-two-non-overlapping-square-submatrices
'''


class Solution:
  def maxArea(self, mat: list[list[int]]) -> int:
    m = len(mat)
    n = len(mat[0])
    ln = min(m, n)
    pr = [[0]*n for _ in range(m)]
    pc = [[0]*n for _ in range(m)]
    ones = [[0]*n for _ in range(m)]
    debug = True

    for x in range(m):
      for y in range(n):
        py = 0 if y == 0 else pr[x][y-1]
        px = 0 if x == 0 else pc[x-1][y]
        pr[x][y] = mat[x][y] + py
        pc[x][y] = mat[x][y] + px
        prev = 0 if x == 0 or y == 0 else ones[x-1][y-1]
        ones[x][y] = prev + pr[x][y] + pc[x][y] - mat[x][y]

    def calc(oc: int, x0: int, y0: int, x1: int, y1: int) -> int:
      left = 0 if y0 == 0 else ones[x1][y0-1]
      top = 0 if x0 == 0 else ones[x0-1][y1]
      tl = 0 if x0 == 0 or y0 == 0 else ones[x0-1][y0-1]
      base = ones[x1][y1]
      # print('calc:', oc, (x0, y0, x1, y1), base, left, top, base)
      return (base - top - left + tl) == oc

    def check(l: int) -> bool:
      if l < 1:
        return True

      cand = {}
      for x0 in range(m):
        x1 = x0+l-1
        if x1 >= m:
          break

        for y0 in range(n):
          y1 = y0+l-1
          if y1 >= n:
            break

          if not calc(l*l, x0, y0, x1, y1):
            continue

          if x0 not in cand:
            cand[x0] = [y0]
          elif len(cand[x0]) == 1:
            cand[x0].append(y0)
          else:
            cand[x0][1] = y0

      arr = []
      for x, ys in cand.items():
        for y in ys:
          arr.append((x, y))

      lc = len(arr)
      for i in range(lc-1):
        x1, y1 = arr[i]
        for j in range(i+1, lc):
          x2, y2 = arr[j]
          if abs(x2-x1) >= l or abs(y2-y1) >= l:
            # print('found:', l, (x1, y1), (x2, y2))
            return True

      return False

    lo, hi = 0, ln
    last = 0

    while lo <= hi:
      mid = (lo + hi) // 2
      if check(mid):
        last = mid
        lo = mid + 1
      else:
        hi = mid - 1

    return last * last
