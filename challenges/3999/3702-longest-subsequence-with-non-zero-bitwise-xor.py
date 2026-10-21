'''
3702-longest-subsequence-with-non-zero-bitwise-xor
'''


class Solution:
  def longestSubsequence(self, nums: list[int]) -> int:
    if all(val == 0 for val in nums):
      return 0

    base = 0
    for val in nums:
      base ^= val
      # print('iter:', val, base)

    n = len(nums)
    return n if base != 0 else n-1
        