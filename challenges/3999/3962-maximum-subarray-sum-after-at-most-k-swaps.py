'''
3962-maximum-subarray-sum-after-at-most-k-swaps
'''

from sortedcontainers import SortedList
from bisect import bisect_left


class Solution:
  def maxSum(self, nums: list[int], k: int) -> int:
    ans = sum(nums)
    if all(val >= 0 for val in nums):
      return ans

    n = len(nums)
    s = sorted(nums)
    cand = SortedList()
    others = SortedList()

    for l in range(n):
      cand.clear()
      others.clear()

      # swap out k largest elements to the rest of the
      # array
      for i in range(max(0, n-k)):
        others.add(s[i])

      # move all k largest elements to the cand
      for i in range(max(0, n-k), n):
        cand.add(s[i])

      curr = 0
      for r in range(l, n):
        if others:
          # find and pop this value if it's in the others
          idx = bisect_left(others, nums[r])

          if idx < len(others) and others[idx] == nums[r]:
            # pop and move the value in range
            val = nums[r]
            others.pop(idx)
          else:
            # value already added, check if a swap can get
            # larger subarray sum
            val = others.pop()

          # remove a large value @ index-i from others and add 
          # it to the candidates list
          cand.add(val)

        # swap in the largest value so far -- it's either a swap
        # or using existing values from the original values in the
        # nums[i:r+1] subarray
        large = cand.pop()
        curr += large

        # compare ans with sum(nums[l:r+1]) after swaps
        ans = max(ans, curr)

    return ans
        