'''
3371-Identify-Largest-Outlier-Array
'''

from typing import List
from collections import Counter


class Solution:
  def getLargestOutlier(self, nums: List[int]) -> int:
    c = Counter(nums)
    if len(nums) == 3:
      if len(c) == 1:
        return nums[0]

      for val in c:
        if c[val] == 1:
          return val

      return -1

    total = sum(nums)
    outlier = -1001

    for v0 in nums:
      rem = total - v0
      if rem%2 == 1:
        continue

      v1 = rem // 2
      # print('iter:', rem, v1)
      if v1 in c and (v0 != v1 or c[v1] >= 2):
        outlier = max(outlier, v0)
          
    return outlier
        