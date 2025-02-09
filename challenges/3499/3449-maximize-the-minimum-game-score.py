'''
3449-maximize-the-minimum-game-score
'''

from math import ceil
from typing import List


class Solution:
  def maxScore(self, points: List[int], m: int) -> int:
    n = len(points)
    if n == 2:
      r = m//2
      extra = m%2
      s0 = (r+extra)*points[0]
      s1 = r*points[1]
      return min(s0, s1)

    def check(floor: int) -> bool:
      score = points[0]
      curr = m-1

      for i in range(n):
        nextScore = 0
        if score < floor:
          r = ceil((floor - score) / points[i])
          if curr - (2*r) < 0:
            return False
            
          curr -= 2*r
          if i+1 < n:
            nextScore += points[i+1] * r
            
        if i+1 < n:
          if curr <= 0 and nextScore < floor:
            return False

          curr -= 1
          nextScore += points[i+1]

        score = nextScore

      return True

    l, r = 0, m*max(points)
    last = 0

    while l <= r:
      mid = (l+r)//2
      if check(mid):
        last = mid
        l = mid+1
      else:
        r = mid-1
    
    return last
        