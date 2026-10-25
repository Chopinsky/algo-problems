'''
3718-smallest-missing-multiple-of-k
'''


class Solution:
  def missingMultiple(self, nums: list[int], k: int) -> int:
    nums.sort()
    curr = k

    for val in nums:
      if val == curr:
        curr += k

    return curr
        