'''
3806-maximum-bitwise-and-after-increment-operations
'''

from typing import List


class Solution:
  def maximumAND(self, nums: List[int], k: int, m: int) -> int:
    ans = 0
    n = len(nums)

    for bit in range(30, -1, -1):
      target = ans | (1<<bit)
      costs = []

      for val in nums:
        missing = target & ~val
        if missing == 0:
          costs.append(0)
          continue

        high_bit = missing.bit_length() - 1
        nxt_bit = high_bit

        while ((val>>nxt_bit) & 1) == 1:
          nxt_bit += 1

        mask = (1<<nxt_bit) - 1
        cost = ((val&~mask) | (1<<nxt_bit) | (target&mask)) - val
        costs.append(cost)

      costs.sort()
      total_cost = sum(costs[:m])
      if total_cost <= k:
        ans = target

    return ans
        