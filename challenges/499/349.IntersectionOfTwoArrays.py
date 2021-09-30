'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''


from typing import List


class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    s1, s2 = set(nums1), set(nums2)
    ln1, ln2 = len(s1), len(s2)
    
    if ln1 > ln2:
      s1, s2 = s2, s1
      
    res = []
    
    for num in s1:
      if num in s2:
        res.append(num)
      
    return res
    