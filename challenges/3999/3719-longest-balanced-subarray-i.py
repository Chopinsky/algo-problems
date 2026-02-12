'''
3719-longest-balanced-subarray-i
'''

from typing import List


class Solution:
  def longestBalanced(self, nums: List[int]) -> int:
    max_ln = 0
    n = len(nums)

    def find_ln(i: int) -> int:
      bal = 0
      ln = 0
      seen = set()

      for j in range(i, n):
        val = nums[j]
        if val not in seen:
          bal += 1 if val%2 == 0 else -1
          seen.add(val)

        if bal == 0:
          ln = max(ln, j-i+1)

        # print('iter:', i, bal, (j, val))

      return ln

    for i in range(n-1):
      max_ln = max(max_ln, find_ln(i))

    return max_ln
