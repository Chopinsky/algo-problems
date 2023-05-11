'''
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

Example 1:

Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

Example 2:

Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3

Example 3:

Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2

Constraints:

1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000
'''


from typing import List
from collections import defaultdict
from bisect import bisect_left
from functools import lru_cache


class Solution:
  def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
    n1, n2 = len(nums1), len(nums2)
    
    @lru_cache(None)
    def dp(i: int, j: int) -> int:
      if i >= n1 or j >= n2:
        return 0
      
      base = max(dp(i+1, j), dp(i, j+1))
      if nums1[i] != nums2[j]:
        return base
      
      return max(base, 1+dp(i+1, j+1))
      
    return dp(0, 0)
        

  def maxUncrossedLines(self, n1: List[int], n2: List[int]) -> int:
    if len(n1) > len(n2):
      n1, n2 = n2, n1

    indices = defaultdict(list)
    for i, n in enumerate(n1):
      indices[n].append(i)
      
    # arr has reversed indices, because we need to find
    # the longest increasing seq, we need to rule out
    # duplicate lines (i.e. number in n1 to multiple 
    # numbers in n2) from the seq
    arr = []
    for n in n2:
      arr.extend(reversed(indices[n]))
    
    # print(arr)
    
    # goal is to find the longest increasing seq
    res  = []
    for i in arr:
      if len(res) == 0 or i > res[-1]:
        res.append(i)
        continue
      
      idx = bisect_left(res, i)
      res[idx] = i

    return len(res)
      
    
  def maxUncrossedLines0(self, nums1: List[int], nums2: List[int]) -> int:
    dp = [[0] * len(nums2) for _ in range(len(nums1))]
    ln = len(nums2)
      
    for i, n in enumerate(nums1):
      for j in range(ln):
        if i == 0:
          dp[i][j] = max(
            dp[i][j-1] if j > 0 else 0, 
            1 if nums1[i] == nums2[j] else 0
          )
          
        else:
          if j == 0:
            dp[i][j] = max(
              dp[i-1][j],
              1 if nums1[i] == nums2[j] else 0
            )
            
          else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            if nums1[i] == nums2[j]:
              dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
        
        
    # for r in dp:
    #   print(r)
    
    return dp[-1][-1]
  
