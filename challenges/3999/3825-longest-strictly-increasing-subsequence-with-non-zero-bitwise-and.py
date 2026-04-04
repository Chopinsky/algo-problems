'''
3825-longest-strictly-increasing-subsequence-with-non-zero-bitwise-and
'''

from bisect import bisect_left


class Solution:
  def longestSubsequence(self, nums: list[int]) -> int:
    bits = [[] for _ in range(32)]

    for val in nums:
      for shift in range(32):
        if val & (1<<shift):
          bits[shift].append(val)

    ln = 0
    # print('init:', bits)

    def get_subseq_len(arr: list[int]) -> int:
      if not arr:
        return 0

      stack = []

      for val in arr:
        if not stack or val > stack[-1]:
          stack.append(val)
          continue

        idx = bisect_left(stack, val)
        stack[idx] = val

      return len(stack)

    return max(get_subseq_len(arr) for arr in bits)
        