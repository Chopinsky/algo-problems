'''
3453-separate-squares-i
'''

from typing import List 


class Solution:
  def separateSquares(self, squares: List[List[int]]) -> float:
    total = sum(s[2]**2 for s in squares)
    target = total/2.0
    # squares.sort(key=lambda x: x[1])
    l = min(s[1] for s in squares)
    r = max(s[1]+s[2] for s in squares)
    prec = 0.000001
    # print('init:', target, l, r)

    def check(y0: float) -> int:
      below = 0
      for _, y1, h in squares:
        if y1 >= y0:
          continue

        below += h*(h if y0-y1 >= h else y0-y1)

      if -prec <= below-target < 0:
        return 0

      return 1 if below < target else -1

    while abs(l-r) > prec:
      mid = (l+r) / 2.0
      res = check(mid)
      # print('check:', mid, res)

      if res == 0:
        return mid

      if res > 0:
        l = mid + prec
      else:
        r = mid - prec

    return l
        