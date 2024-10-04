'''
2934. Minimum Operations to Maximize Last Elements in Arrays
'''

from typing import List

class Solution:
  def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    
    def count(m1, m2):
      ops = 0
      
      for i in range(n-1):
        v1 = nums1[i]
        v2 = nums2[i]

        if v1 > m1 and v1 > m2:
          return -1

        if v2 > m1 and v2 > m2:
          return -1

        if v1 > m1:
          if v2 > m1:
            return -1

          ops += 1
          # print('0:', (m1, m2), (v1, v2))
          
          continue

        if v2 > m2:
          if v1 > m2:
            return -1
          
          ops += 1
          # print('1:', (m1, m2), (v1, v2))
          
          continue

      return ops
        
    c0 = count(nums1[-1], nums2[-1])
    c1 = count(nums2[-1], nums1[-1])
    # print('done:', c0, c1)
    
    if c0 >= 0 and c1 >= 0:
      return min(c0, 1+c1)
    
    if c1 >= 0:
      return 1+c1
    
    return c0
  