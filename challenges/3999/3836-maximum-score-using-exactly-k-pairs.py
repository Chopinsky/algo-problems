'''
3836-maximum-score-using-exactly-k-pairs
'''

import math
from functools import cache
from typing import List


class Solution:
  def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
    n1 = len(nums1)
    n2 = len(nums2)

    @cache
    def dp(i: int, j: int, r: int) -> int:
      if r == 0:
        return 0

      if i >= n1 or j >= n2 or n1-i < r or n2-j < r:
        return -math.inf

      return max(
        nums1[i]*nums2[j] + dp(i+1, j+1, r-1),
        dp(i+1, j, r),
        dp(i, j+1, r),
      ) 

    return dp(0, 0, k)
      