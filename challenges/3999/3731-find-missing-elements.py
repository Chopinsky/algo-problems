'''
3731-find-missing-elements
'''


class Solution:
  def findMissingElements(self, nums: list[int]) -> list[int]:
    nums = set(nums)
    lo = min(nums)
    hi = max(nums)
    res = []

    for val in range(lo, hi+1):
      if val not in nums:
        res.append(val)

    return res
