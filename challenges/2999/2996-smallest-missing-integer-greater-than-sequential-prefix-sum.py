'''
2996-smallest-missing-integer-greater-than-sequential-prefix-sum
'''


class Solution:
  def missingInteger(self, nums: list[int]) -> int:
    s = nums[0]
    cand = set(nums)

    for i in range(1, len(nums)):
      if nums[i] != nums[i-1]+1:
        break

      s += nums[i]

    while s in cand:
      s += 1

    return s
        