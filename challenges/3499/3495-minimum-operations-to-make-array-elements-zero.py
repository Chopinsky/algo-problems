'''
3495-minimum-operations-to-make-array-elements-zero
'''

from typing import List


class Solution:
  def minOperations(self, queries: List[List[int]]) -> int:
    def calc_steps(l: int, r: int):
      cnt, low, k = 0, 1, 1
      while low <= r:
        high = (low<<2) - 1
        left, right = max(l, low), min(r, high)
        if left <= right:
          cnt += (right-left+1) * k

        low <<= 2
        k += 1

      return cnt

    ans = 0
    for l, r in queries:
      ops = calc_steps(l, r)
      ans += (ops + 1) // 2

    return ans
        