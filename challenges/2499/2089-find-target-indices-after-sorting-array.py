'''
2089-find-target-indices-after-sorting-array
'''

from bisect import bisect_left


class Solution:
  def targetIndices(self, nums: list[int], target: int) -> list[int]:
    nums.sort()
    i = bisect_left(nums, target)
    res = []

    while i < len(nums) and nums[i] == target:
      res.append(i)
      i += 1

    return res

        