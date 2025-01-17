'''
1599. Maximum Profit of Operating a Centennial Wheel
'''

from typing import List


class Solution:
  def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
    n = len(customers)
    i = 0
    turns = 0
    rounds = 0
    max_profits = 0
    profits = 0
    waiting = 0

    while i < n or waiting > 0:
      if i < n:
        waiting += customers[i]
        i += 1

      boarding = min(4, waiting)
      waiting -= boarding
      profits += boarding*boardingCost - runningCost
      turns += 1
      
      if profits > max_profits:
        max_profits = profits
        rounds = turns

      # print('iter:', i, boarding, profits)

    return rounds if max_profits > 0 else -1
        