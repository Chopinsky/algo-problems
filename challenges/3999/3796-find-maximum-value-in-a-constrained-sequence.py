'''
3796-find-maximum-value-in-a-constrained-sequence
'''

import math
from typing import List
from bisect import bisect_left
from heapq import heappop, heappush


class Solution:
  def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
    max_possible = [math.inf] * n
    max_possible[0] = 0
    
    for idx, maxVal in restrictions:
      max_possible[idx] = min(max_possible[idx], maxVal)
    
    for i in range(1, n):
      max_possible[i] = min(max_possible[i], max_possible[i-1] + diff[i-1])
    
    for i in range(n-2, -1, -1):
      max_possible[i] = min(max_possible[i], max_possible[i+1] + diff[i])
    
    return max(max_possible)

  def findMaxVal(self, n: int, r: List[List[int]], diff: List[int]) -> int:
    if not r:
      return sum(diff)

    a = [0]*n
    p = [0]*n
    upper = {0:0}
    cand = [(0, 0)]
    pos = [0] + sorted(v[0] for v in r)

    for i in range(1, n):
      p[i] = diff[i-1] + p[i-1]

    for idx, mval in r:
      upper[idx] = mval
      heappush(cand, (mval, idx))

    def get_diff(i: int, j: int):
      return p[j] - p[i]

    def get_max(i: int, j: int):
      max_val = max(upper[i], upper[j])
      if i == j or i+1 == j:
        return max_val

      for k in range(i+1, j):
        vl = upper[i] + get_diff(i, k)
        vr = upper[j] + get_diff(k, j)
        curr = min(vl, vr)
        max_val = max(max_val, curr)

      return max_val

    # print('init:', pos, upper, cand, p)
    while cand:
      v0, idx = heappop(cand)
      if v0 > upper[idx]:
        continue

      i = bisect_left(pos, idx)
      if i > 0:
        ldx = pos[i-1]
        vl = upper[ldx]
        dl = get_diff(ldx, idx)

        # must reduce max_val at ldx
        if vl-v0 > dl:
          upper[ldx] = v0+dl
          heappush(cand, (upper[ldx], ldx))

      if i < len(pos)-1:
        rdx = pos[i+1]
        vr = upper[rdx]
        dr = get_diff(idx, rdx)

        # must reduce max_val at rdx
        if vr-v0 > dr:
          upper[rdx] = v0+dr
          heappush(cand, (upper[rdx], rdx))

    # print('done1:', upper)
    res = upper[pos[-1]] + get_diff(pos[-1], n-1)

    for k in range(1, len(pos)):
      res = max(
        res,
        get_max(pos[k-1], pos[k])
      )

    return res
        