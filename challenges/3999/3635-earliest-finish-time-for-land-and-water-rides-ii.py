'''
3635-earliest-finish-time-for-land-and-water-rides-ii
'''

import math
from typing import List


class Solution:
  def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:
    m = len(ls)
    n = len(ws)
    t = math.inf
    l = sorted(zip(ls, ld), key=lambda x: (x[0]+x[1], x[0], x[1]))
    w = sorted(zip(ws, wd), key=lambda x: (x[0]+x[1], x[0], x[1]))
    idx = 0
    short = math.inf
    
    sl = [sum(vals) for vals in l]
    for i in range(m-2, -1, -1):
      sl[i] = min(sl[i], sl[i+1])

    sw = [sum(vals) for vals in w]
    for i in range(n-2, -1, -1):
      sw[i] = min(sw[i], sw[i+1])
    
    # print('init:', l, sl, w, sw)

    # take land ride first
    for s, d in l:
      while idx < n and w[idx][0] <= s+d:
        short = min(short, w[idx][1])
        idx += 1

      if short < math.inf:
        # taking opened ride
        t = min(t, s+d+short)

      if idx < n:
        # taking next open ride
        t = min(t, sw[idx])

      # print('land:', t, (s, d), short, idx)

    idx = 0
    short = math.inf

    # take water ride first
    for s, d in w:
      while idx < m and l[idx][0] <= s+d:
        short = min(short, l[idx][1])
        idx += 1
      
      if short < math.inf:
        t = min(t, s+d+short)

      if idx < m:
        t = min(t, sl[idx])

      # print('water:', t, (s, d), short, idx)

    return t
