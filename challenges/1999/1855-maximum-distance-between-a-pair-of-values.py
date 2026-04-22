'''
1855-maximum-distance-between-a-pair-of-values
'''

from typing import List


class Solution:
  def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
    dist = 0
    i = 0
    n1 = len(nums1)
    n2 = len(nums2)

    for j in range(n2):
      while i < n1 and nums1[i] > nums2[j]:
        i += 1

      if i <= j and i < n1 and nums1[i] <= nums2[j]:
        dist = max(dist, j-i)

    return dist
        