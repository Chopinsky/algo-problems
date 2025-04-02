'''
3462-maximum-sum-with-at-most-k-elements
'''

from heapq import heappop
from typing import List


class Solution:
  def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
    n = len(grid)
    m = len(grid[0])
    stack = sorted([(-grid[i][j], i) for j in range(m) for i in range(n)])
    total = 0
    # print('init:', stack)

    while stack and k > 0:
      val, r = heappop(stack)
      if limits[r] == 0:
        continue

      total -= val
      limits[r] -= 1
      k -= 1

    return total
