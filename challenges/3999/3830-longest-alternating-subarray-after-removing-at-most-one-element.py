'''
3830-longest-alternating-subarray-after-removing-at-most-one-element
'''

from typing import List


class Solution:
  def longestAlternating(self, nums: List[int]) -> int:
    n = len(nums)

    def is_alternating(v0: int, v1: int, v2: int) -> bool:
      return (v0 < v1 and v1 > v2) or (v0 > v1 and v1 < v2)

    l = [1]*n
    for i in range(1, n):
      if nums[i] != nums[i-1]:
        if i > 1 and is_alternating(nums[i-1], nums[i], nums[i-2]):
          # continue the previous alternating subarray
          l[i] = l[i-1] + 1
        else:
          # start a new alternating subarray
          l[i] = 2

    r = [1]*n
    for i in range(n-2, -1, -1):
      if nums[i+1] != nums[i]:
        if i < n-2 and is_alternating(nums[i+1], nums[i], nums[i+2]):
          # continue the previous alternating subarray
          r[i] = r[i+1] + 1
        else:
          # start a new alternating subarray
          r[i] = 2

    res = max(l)
    for i in range(1, n-1):
      # connecting the neighbor dots
      if nums[i-1] != nums[i+1]:
        l_ln = l[i-1] if i > 1 and is_alternating(nums[i-2], nums[i-1], nums[i+1]) else 1
        r_ln = r[i+1] if i < n-2 and is_alternating(nums[i-1], nums[i+1], nums[i+2]) else 1
        res = max(res, l_ln+r_ln)

    return res
