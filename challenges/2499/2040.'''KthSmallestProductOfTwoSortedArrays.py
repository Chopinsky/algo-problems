'''
Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.
 

Example 1:

Input: nums1 = [2,5], nums2 = [3,4], k = 2
Output: 8
Explanation: The 2 smallest products are:
- nums1[0] * nums2[0] = 2 * 3 = 6
- nums1[0] * nums2[1] = 2 * 4 = 8
The 2nd smallest product is 8.
Example 2:

Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
Output: 0
Explanation: The 6 smallest products are:
- nums1[0] * nums2[1] = (-4) * 4 = -16
- nums1[0] * nums2[0] = (-4) * 2 = -8
- nums1[1] * nums2[1] = (-2) * 4 = -8
- nums1[1] * nums2[0] = (-2) * 2 = -4
- nums1[2] * nums2[0] = 0 * 2 = 0
- nums1[2] * nums2[1] = 0 * 4 = 0
The 6th smallest product is 0.
Example 3:

Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
Output: -6
Explanation: The 3 smallest products are:
- nums1[0] * nums2[4] = (-2) * 5 = -10
- nums1[0] * nums2[3] = (-2) * 4 = -8
- nums1[4] * nums2[0] = 2 * (-3) = -6
The 3rd smallest product is -6.
 

Constraints:

1 <= nums1.length, nums2.length <= 5 * 10^4
-105 <= nums1[i], nums2[j] <= 10^5
1 <= k <= nums1.length * nums2.length
nums1 and nums2 are sorted.
'''


from typing import List
from bisect import bisect_right, bisect_left


class Solution:
  def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
    ndx1 = bisect_right(nums1, 0)
    ndx2 = bisect_right(nums2, 0)
    n1 = nums1[:ndx1]
    n2 = nums2[:ndx2]

    pdx1 = bisect_left(nums1, 1)
    pdx2 = bisect_left(nums2, 1)
    p1 = nums1[pdx1:]
    p2 = nums2[pdx2:]

    # n1, p1, n2, p2 = [], [], [], []
    z1 = len(nums1)-len(n1)-len(p1)
    z2 = len(nums2)-len(n2)-len(p2)
    
    '''
    for val in nums1:
      if val == 0:
        z1 += 1
      elif val < 0:
        n1.append(val)
      else:
        p1.append(val)
        
    for val in nums2:
      if val == 0:
        z2 += 1
      elif val < 0:
        n2.append(val)
      else:
        p2.append(val)
    '''

    a, b, c, d = nums1[0]*nums2[0], nums1[-1]*nums2[-1], nums1[-1]*nums2[0], nums1[0]*nums2[-1]
    l = min(a, b, c, d)
    r = max(a, b, c, d)
    
    # number of products smaller than 0
    c1 = len(p1) * len(n2) + len(n1) * len(p2)
    
    # number of products that yield 0
    c2 = z1 * len(nums2) + z2 * len(nums1) - z1 * z2
    
    '''
    print(len(n1), len(p1), len(nums1), z1)
    print(len(n2), len(p2), len(nums2), z2)
    print(l, r, c1, c2)
    '''
    
    # count number of products that are equal to or smaller than val
    def count(val: int) -> int:
      if val == 0:
        return c1 + c2
      
      if val > 0:
        base = c1 + c2
        print('base', c1, c2, base)
        
        # count((v1 from p1) * (v2 from p2) <= val)
        if p1 and p2:
          for v1 in p1:
            t = val // v1
            if t < p2[0]:
              break
              
            idx = bisect_right(p2, t) - 1
            if idx < 0:
              break
              
            # print('p1-p2', v1, p2[idx], v1*p2[idx], idx, idx+1)
            base += idx + 1
            
        # count((v1 from n1) * (v2 from n2) <= val)
        if n1 and n2:
          for v1 in n1[::-1]:
            t = -(val // -v1)
            if t > n2[-1]:
              break
              
            idx = bisect_left(n2, t)
            if idx >= len(n2):
              break
              
            # print('n1-n2', v1, n2[idx], v1*n2[idx], idx, len(n2)-idx)
            base += len(n2) - idx
        
      else:
        base = 0  
        
        if p1 and n2:
          for v1 in p1[::-1]:
            t = val // v1
            if t < n2[0]:
              break
              
            idx = bisect_right(n2, t) - 1
            if idx < 0:
              break
              
            base += idx + 1
          
        if n1 and p2:
          for v2 in p2[::-1]:
            t = val // v2
            if t < n1[0]:
              break
              
            idx = bisect_right(n1, t) - 1
            if idx < 0:
              break
              
            base += idx + 1
      
      return base
    
    last_val = r
    
    while l < r:
      m = (l + r) // 2
      # print('bs:', l, m, r, count(m))
      
      if count(m) >= k:
        last_val = min(last_val, m)
        r = m-1
      else:
        l = m+1
    
    # print(count(120512), count(120513))
    # return 0
  
    # print('out:', l, last_val, count(l))
    return l if count(l) >= k else last_val
    