'''
3942-minimum-operations-to-sort-a-permutation
'''

from typing import List


class Solution:
  def minOperations(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
      return 0 if nums[0] == 0 else -1

    if all(nums[i-1]+1 == nums[i] for i in range(1, n)):
      return 0 if nums[0] == 0 else -1

    idx = nums.index(0)
    debug = False
    if debug:
      print('init:', idx, nums)

    a1 = nums[idx:] + nums[:idx]
    if debug:
      print('test1:', a1)

    if all(a1[i] == i for i in range(n)):
      # left shift n-1
      return min(idx, n-idx+2)

    a2 = nums[(idx+1):] + nums[:(idx+1)]
    if debug:
      print('test2:', a2)

    if all(a2[i] == n-1-i for i in range(n)):
      # left shift idx+1 and reverse
      return min(idx+1, n-1-idx) + 1

    return -1
        