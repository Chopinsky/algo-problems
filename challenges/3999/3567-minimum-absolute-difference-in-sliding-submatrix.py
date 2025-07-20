'''
3567-minimum-absolute-difference-in-sliding-submatrix
'''

from typing import List


class Solution:
  def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    if k == 1:
      return [[0]*n for _ in range(m)]

    i = 0
    j = 0
    ans = []

    def find(i: int, j: int) -> int:
      vals = set()
      for x in range(i, i+k):
        for y in range(j, j+k):
          vals.add(grid[x][y])

      cand = sorted(vals)
      # print('find-1:', (i, j), cand)
      if len(cand) == 1:
        return 0

      return min(cand[idx]-cand[idx-1] for idx in range(1, len(vals)))

    while i+k <= m:
      ans.append([])
      j = 0

      while j+k <= n:
        ans[-1].append(find(i, j))
        j += 1

      i += 1
        
    return ans
