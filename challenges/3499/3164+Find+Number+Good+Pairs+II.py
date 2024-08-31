'''
3164. Find the Number of Good Pairs II

You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.

Example 1:

Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1

Output: 5

Explanation:

The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
Example 2:

Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3

Output: 2

Explanation:

The 2 good pairs are (3, 0) and (3, 1).

Constraints:

1 <= n, m <= 10^5
1 <= nums1[i], nums2[j] <= 10^6
1 <= k <= 10^3
'''

from typing import List
from collections import Counter

class Solution:
  def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
    pairs = 0
    c0 = Counter(nums1)
    c1 = Counter(nums2)
    top = max(c0)
    
    for val, cnt in c1.items():
      val *= k
      base = val
      
      while val <= top:
        if val in c0:
          pairs += c0[val]*cnt
          
        val += base
    
    return pairs
        