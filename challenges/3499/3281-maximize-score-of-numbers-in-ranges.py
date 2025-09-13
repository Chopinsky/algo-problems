'''
3281-maximize-score-of-numbers-in-ranges
'''

from typing import List


class Solution:
  def maxPossibleScore(self, start: List[int], d: int) -> int:
    start.sort()
    n = len(start)
    l, r = min(start[i+1]-start[i] for i in range(n-1)), start[-1]-start[0]+d
    last = l
    # print('init:', last)

    def is_possible(delta: int) -> bool:
      prev = start[0]
      for i in range(1, n):
        val = start[i]
        if val+d-prev < delta:
          return False

        prev = max(prev+delta, val)

      return True

    while l <= r:
      mid = (l+r) // 2
      if is_possible(mid):
        last = mid
        l = mid+1
      else:
        r = mid-1

    return last
