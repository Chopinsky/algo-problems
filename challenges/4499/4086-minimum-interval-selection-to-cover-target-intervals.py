'''
4086-minimum-interval-selection-to-cover-target-intervals
'''

from typing import List
from bisect import bisect_left, bisect_right


class Solution:
  def minSelection(self, a: List[List[int]], b: List[List[int]]) -> int:
    a.sort(key=lambda x: (x[0], -x[1]))
    b.sort()
    t = []
    head = []
    tail = []
    itv = {}

    for s, e in b:
      if t and s <= t[-1][1]:
        t[-1][1] = max(t[-1][1], e)
        continue

      t.append([s, e])
      # tail.append(e)
      # itv[e] = (s, len(t)-1)

    for s, e in t:
      head.append(s)
      tail.append(e)
      itv[e] = s

    # print('init:', t, a)
    # print('t:', tail)
    i = 0
    cand = []
    curr = t[i].copy()

    def can_pop(s: int) -> bool:
      if not cand:
        return False

      if len(cand) == 1:
        return s <= t[0][0]

      if s <= cand[-2][1]:
        return True

      i = bisect_right(tail, cand[-2][1])-1
      j = bisect_left(head, s)

      # prev-prev and curr can cover the remaining intervals
      if i+1 == j:
        return True

      ps = cand[-1][0]
      i = bisect_left(tail, ps)
      if i >= len(tail):
        return False

      te = tail[i]
      ts = itv[te]
      # print('check:', s, ps, (ts, te))

      # prev-prev and curr can cover the remaining intervals
      return ps < ts and s <= ts

    for s, e in a:
      if i >= len(t):
        break

      # already covered
      if cand and e <= cand[-1][1]:
        continue

      # not contributing
      if e < curr[0]:
        continue

      # not be able to cover
      if s > curr[0]:
        return -1
        
      while can_pop(s):
        p = cand.pop()
        # print('pop:', (s, e), p)

      cand.append([s, e])
      curr[0] = max(curr[0], e)
      
      # full coverage achieved
      if e >= curr[1]:
        while i < len(t) and e >= t[i][1]:
          i += 1

        if i < len(t):
          curr = t[i].copy()
          curr[0] = max(curr[0], e)

    # print('done:', cand, i)
    return len(cand) if i >= len(t) and cand else -1
