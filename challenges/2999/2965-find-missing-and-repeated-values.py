'''
2965-find-missing-and-repeated-values
'''

from typing import List


class Solution:
  def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    ans = []
    n = len(grid)
    cand = set(i+1 for i in range(n*n))

    for row in grid:
      for val in row:
        if val in cand:
          cand.discard(val)
        else:
          ans.append(val)

    ans += list(cand)

    return ans
        