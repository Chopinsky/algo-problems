'''
You are given two 0-indexed integer arrays nums1 and nums2, each of size n, and an integer diff. Find the number of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
Return the number of pairs that satisfy the conditions.

Example 1:

Input: nums1 = [3,2,5], nums2 = [2,2,1], diff = 1
Output: 3
Explanation:
There are 3 pairs that satisfy the conditions:
1. i = 0, j = 1: 3 - 2 <= 2 - 2 + 1. Since i < j and 1 <= 1, this pair satisfies the conditions.
2. i = 0, j = 2: 3 - 5 <= 2 - 1 + 1. Since i < j and -2 <= 2, this pair satisfies the conditions.
3. i = 1, j = 2: 2 - 5 <= 2 - 1 + 1. Since i < j and -3 <= 2, this pair satisfies the conditions.
Therefore, we return 3.
Example 2:

Input: nums1 = [3,-1], nums2 = [-2,2], diff = -1
Output: 0
Explanation:
Since there does not exist any pair that satisfies the conditions, we return 0.
 

Constraints:

n == nums1.length == nums2.length
2 <= n <= 105
-104 <= nums1[i], nums2[i] <= 104
-104 <= diff <= 104
'''

from typing import List


class Solution:
  def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
    n = len(nums1)
    delta = [nums1[i]-nums2[i] for i in range(n)]
    base, top = min(delta), max(delta)
    fenwick = [0] * (top-base+2)
    
    def update(val: int):
      val += 1
      while val < len(fenwick):
        fenwick[val] += 1
        val += (val & -val)
        
    def query(val: int):
      count = 0
      val += 1
      
      while val > 0:
        count += fenwick[val]
        val -= (val & -val)
        
      return count
    
    total = 0
    upper = top-base
    # print(len(fenwick), base, top)
    
    for d in delta:
      d -= base
      total += query(min(upper, d+diff))
      update(d)
      
    return total
      
    
