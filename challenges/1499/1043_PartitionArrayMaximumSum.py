'''
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 10^9
1 <= k <= arr.length
'''

from typing import List
from functools import lru_cache


class Solution:
  def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    n = len(arr)
    
    @lru_cache(None)
    def dp(i: int) -> int:
      if i >= n:
        return 0
      
      curr = 0
      res = 0
      
      for j in range(i, n):
        cnt = j-i+1
        if cnt > k:
          break
          
        curr = max(curr, arr[j])
        res = max(res, cnt*curr + dp(j+1))
      
      # print(i, res, curr)
      return res
      
    return dp(0)
        
        
  def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    if k == 1:
      return sum(arr)
    
    n = len(arr)
    
    @lru_cache(None)
    def dp(i: int) -> int:
      if i >= n:
        return 0
      
      max_val = 0
      sums = 0
      
      for j in range(i, min(i+k, n)):
        max_val = max(max_val, arr[j])
        sums = max(sums, max_val*(j-i+1) + dp(j+1))
        
      # print(i, sums, max_val)
      return sums
    
    return dp(0)
        