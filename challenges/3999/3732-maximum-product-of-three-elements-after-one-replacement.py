'''
3732-maximum-product-of-three-elements-after-one-replacement
'''

from typing import List


class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    n = len(nums)
    cand = sorted(abs(val) for val in nums if val != 0)
    # print('init:', cand)

    # will have to include at least one 0s in the array
    if len(cand) < 2:
      return 0

    return 10**5 * cand[-1] * cand[-2]
        