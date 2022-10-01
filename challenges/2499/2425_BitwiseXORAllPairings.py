'''
2425. Bitwise XOR of All Pairings
'''

from typing import List


class Solution:
  def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
    base1 = nums1[0] 
    for val in nums1[1:]:
      base1 ^= val
    
    if len(nums2) % 2 == 0:
      base1 = 0
      
    base2 = nums2[0]
    for val in nums2[1:]:
      base2 ^= val
      
    if len(nums1) % 2 == 0:
      base2 = 0
    
    # print(nums1, base1, nums2, base2)
    return base1^base2
    
