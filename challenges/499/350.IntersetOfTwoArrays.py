'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''


from typing import List
from collections import Counter


class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) < len(nums2):
      s = sorted(nums1)
      l = sorted(nums2)
    else:
      s = sorted(nums2)
      l = sorted(nums1)
      
    i, j = 0, 0
    ans = []
    
    while i < len(s) and j < len(l):
      if s[i] == l[j]:
        ans.append(s[i])
        i += 1
        j += 1
      elif s[i] < l[j]:
        i += 1
      else:
        j += 1
        
    return ans
      
    
  def intersect0(self, nums1: List[int], nums2: List[int]) -> List[int]:
    a0 = Counter(nums1) 
    a1 = Counter(nums2)
    ans = []
    
    for n, c in a0.items():
      # print(n, c)
      if n in a1:
        c = min(c, a1[n])
        if c > 0:
          ans.extend([n]*c)
      
    return list(ans)