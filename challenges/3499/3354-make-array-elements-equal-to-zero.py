'''
3354-make-array-elements-equal-to-zero
'''

from typing import List


class Solution:
  def countValidSelections(self, nums: List[int]) -> int:
    prefix = [val for val in nums]
    n = len(nums)
    c = 0

    for i in range(1, n):
      prefix[i] += prefix[i-1]

    for i in range(n):
      if nums[i] > 0:
        continue

      l = prefix[i-1] if i > 0 else 0
      r = prefix[-1] - prefix[i]

      if l == r:
        c += 2

      elif abs(l-r) == 1:
        c += 1

    return c