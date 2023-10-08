'''
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.

Example 2:

Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.

Example 3:

Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.

Constraints:

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000
'''


from typing import List
from functools import lru_cache


class Solution:
  def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    n1 = len(nums1)
    n2 = len(nums2)
    
    @lru_cache(None)
    def dp(i: int, j: int) -> int:
      if i == n1-1:
        return max(nums1[i]*nums2[k] for k in range(j, n2))
      
      if j == n2-1:
        return max(nums2[j]*nums1[k] for k in range(i, n1))
      
      v0 = nums1[i]*nums2[j]
      v1 = dp(i+1, j+1)
      v3 = dp(i, j+1)
      v4 = dp(i+1, j)
      
      return max(v0, v0+v1, v3, v4)
    
    return dp(0, 0)
        
        
  def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    l1, l2 = len(nums1), len(nums2)
    if l1 == 1 and l2 == 1:
      return nums1[0] * nums2[0]
    
    p1 = [nums1[0] * nums2[i] for i in range(l2)]
    p2 = [nums2[0] * nums1[i] for i in range(l1)]
    
    for i in range(1, l2):
      p1[i] = max(p1[i-1], p1[i])
      
    for i in range(1, l1):
      p2[i] = max(p2[i-1], p2[i])
    
    
    @lru_cache(None)
    def dp(i: int, j: int) -> int:
      if i == 0:
        return p1[j]
        
      if j == 0:
        return p2[i]
      
      nxt = dp(i-1, j-1) if (i >= 1 and j >= 1) else 0
      base = nums1[i] * nums2[j] + max(nxt, 0)
      # print('base', i, j, base)
      
      if i > 0:
        base = max(base, dp(i-1, j))
        
      if j > 0:
        base = max(base, dp(i, j-1))
      
      # print('final', i, j, base)
      return base
    
    return dp(l1-1, l2-1)
  