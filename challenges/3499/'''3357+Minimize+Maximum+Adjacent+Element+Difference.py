'''
3357. Minimize the Maximum Adjacent Element Difference

[1,2,-1,10,8]
[-1,-1,-1]
[-1,10,-1,8]
[21,18,16]
[14,-1,-1,46]
[-1,593,-1,496,612,-1,981,-1,-1,566]
[-1,80,-1,-1,17]
[-1,184,224,-1,-1,66]
'''

from typing import List
from bisect import bisect_left
from itertools import groupby

class Solution:
  def minDifference(self, A: List[int]) -> int:
    groups = [list(grp) for k, grp in groupby(A, key=lambda x: x>0)]
    singles = []  # a? or a??
    doubles = []  # a?b or a??b
    base = 0  # the max diff of two positive elements
    # print(groups)

    for i, grp in enumerate(groups):
      if grp[0] != -1:
        for j in range(1, len(grp)):
          base = max(base, abs(grp[j]-grp[j-1]))
 
        continue

      neis = []
      if i - 1 >= 0:
        neis.append(groups[i-1][-1])

      if i + 1 < len(groups):
        neis.append(groups[i+1][0])

      neis.sort()

      if len(neis) == 1:
        singles.append(*neis)

      if len(neis) == 2:
        doubles.append([*neis, len(grp) > 1])

    if not singles and not doubles:
      return base

    # print(singles, doubles)
    def possible(bound):
      intervals = []
      
      for a in singles:
        intervals.append((a-bound, a+bound))
        
      for a, b, stacked in doubles:
        if stacked:
          intervals.append((a-bound, a+bound))
          intervals.append((b-bound, b+bound))
          
        else:
          lo = b - bound
          hi = a + bound
          if lo > hi: 
            return False
          
          intervals.append((lo, hi))

      # we have a bunch of intervals, and we want to know if we can stab twice
      # to hit all intervals
      lo = min(e for _, e in intervals)
      hi = max(s for s, _ in intervals)

      if lo + bound < hi:
        if not all(
          any(abs(a-p) <= bound and abs(b-p) <= bound for p in [lo, hi]) 
          for a, b, _ in doubles
        ):
          return False

      return all(s <= lo <= e or s <= hi <= e for s, e in intervals)

    return bisect_left(range(10**9), 1, base, max(A), key=possible)
      