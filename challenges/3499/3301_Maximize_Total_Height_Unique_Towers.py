'''
3301. Maximize the Total Height of Unique Towers
'''

from typing import List


class Solution:
  def maximumTotalSum(self, height: List[int]) -> int:
    height.sort()
    prev = 2*height[-1]
    total = 0

    for i in range(len(height)-1, -1, -1):
      curr = min(prev-1, height[i])
      # print('iter:', (i, height[i], curr))

      if curr <= 0:
        return -1

      total += curr
      prev = curr

    return total
