'''
3468-find-the-number-of-copy-arrays
'''

from typing import List


class Solution:
  def countArrays(self, a: List[int], bounds: List[List[int]]) -> int:
    n = len(a)
    if n == 1:
      return bounds[0][1]-bounds[0][0]+1

    def check(diff: int) -> bool:
      for i in range(n):
        v1 = a[i]+diff
        if v1 < bounds[i][0] or v1 > bounds[i][1]:
          return False

      return True

    diff_low = bounds[0][0] - a[0]
    diff_high = bounds[0][1] - a[0]

    for i in range(n):
      diff_low = max(diff_low, bounds[i][0]-a[i])
      diff_high = min(diff_high, bounds[i][1]-a[i])
    
    # print('done:', diff_low, diff_high, a[0]+diff_low)
    if not check(diff_low) or not check(diff_high):
      return 0

    return diff_high-diff_low+1
