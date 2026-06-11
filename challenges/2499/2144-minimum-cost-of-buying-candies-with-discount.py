'''
2144-minimum-cost-of-buying-candies-with-discount
'''

from typing import List


class Solution:
  def minimumCost(self, cost: List[int]) -> int:
    c = 0
    cost.sort()

    while cost:
      c += cost.pop()
      if cost:
        c += cost.pop()

      if cost:
        cost.pop()

    return c
