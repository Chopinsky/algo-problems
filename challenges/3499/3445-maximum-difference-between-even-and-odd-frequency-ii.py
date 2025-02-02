'''
3445-maximum-difference-between-even-and-odd-frequency-ii
'''

from collections import deque


class Solution:
  def maxDifference(self, s: str, k: int) -> int:
    cand = sorted(set(s))
    diff = -float('inf')
    n = len(cand)
    debug = False
    # print('init:', cand)

    def count(v0: str, v1: str) -> int:
      ac, bc = 0, 0
      eo = None
      oe = None
      oo = None
      ee = None
      q = deque()
      diff = -float('inf')
      if debug:
        print('count:', v0, v1)

      for i, ch in enumerate(s):
        if ch == v0:
          ac += 1

        if ch == v1:
          bc += 1

        while q and i-q[0][0] >= k and q[0][1] < ac and q[0][2] < bc:
          _, a0, b0 = q.popleft()
          if debug:
            print('pop:', (a0, b0))

          if a0%2 == 0 and b0%2 == 0:
            d0 = a0-b0
            if ee is None:
              ee = [d0, d0]
            else:
              ee[0] = min(ee[0], d0)
              ee[1] = max(ee[1], d0)
          
          if a0%2 == 1 and b0%2 == 1:
            d1 = a0-b0
            if oo is None:
              oo = [d1, d1]
            else:
              oo[0] = min(oo[0], d1)
              oo[1] = max(oo[1], d1)

          if a0%2 == 1 and b0%2 == 0:
            d2 = a0-b0
            if oe is None:
              oe = [d2, d2]
            else:
              oe[0] = min(oe[0], d2)
              oe[1] = max(oe[1], d2)

          if a0%2 == 0 and b0%2 == 1:
            d3 = a0-b0
            if eo is None:
              eo = [d3, d3]
            else:
              eo[0] = min(eo[0], d3)
              eo[1] = max(eo[1], d3)

        q.append((i, ac, bc))
        if i+1 >= k and ac > 0 and bc > 0 and ac%2 != bc%2:
          base = ac-bc if ac%2 == 1 else bc-ac
        else:
          base = -float('inf')

        diff = max(diff, base)
        d0 = ac-bc
        if debug:
          print('iter:', (i, ac, bc), base, oe, eo, oo, ee)

        if ac%2 == 1 and bc%2 == 1:
          if oe is not None:
            diff = max(diff, oe[1]-d0)

          if eo is not None:
            diff = max(diff, d0-eo[0])

        if ac%2 == 0 and bc%2 == 0:
          if oe is not None:
            diff = max(diff, d0-oe[0])

          if eo is not None:
            diff = max(diff, eo[1]-d0)

        if ac%2 == 1 and bc%2 == 0:
          if ee is not None:
            diff = max(diff, d0-ee[0])

          if oo is not None:
            diff = max(diff, oo[1]-d0)

        if ac%2 == 0 and bc%2 == 1:
          if ee is not None:
            diff = max(diff, ee[1]-d0)

          if oo is not None:
            diff = max(diff, d0-oo[0])

      return diff

    for i in range(n-1):
      for j in range(i+1, n):
        diff = max(diff, count(cand[i], cand[j]))  

    return diff
