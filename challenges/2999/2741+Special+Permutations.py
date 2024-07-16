'''
2741. Special Permutations

You are given a 0-indexed integer array nums containing n distinct positive integers. A permutation of nums is called special if:

For all indexes 0 <= i < n - 1, either nums[i] % nums[i+1] == 0 or nums[i+1] % nums[i] == 0.
Return the total number of special permutations. As the answer could be large, return it modulo 109 + 7.

Example 1:

Input: nums = [2,3,6]
Output: 2
Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.
Example 2:

Input: nums = [1,4,3]
Output: 2
Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.

Constraints:

2 <= nums.length <= 14
1 <= nums[i] <= 10^9
'''

from functools import lru_cache
from typing import List

class Solution:
  def specialPerm(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
      return 1
    
    mod = 10**9 + 7
    edges = [[] for _ in range(n)]
    nums.sort()
    
    for i in range(1, n):
      v0 = nums[i]
      for j in range(i):
        v1 = nums[j]
        if v0 % v1 == 0:
          edges[i].append(j)
          edges[j].append(i)
      
    # print(nums, edges)
    done = (1<<n)-1
    
    @lru_cache(None)
    def dp(i: int, mask: int):
      # illegal
      if i >= n:
        return 0
      
      # all numbers placed
      if mask == done:
        return 1
      
      if i < 0:
        cand = list(range(n))
      else:
        cand = edges[i]
        
      count = 0
      for j in cand:
        if mask & (1<<j) > 0:
          continue
          
        count = (count + dp(j, mask|(1<<j))) % mod
        
      return count
    
    return dp(-1, 0)
        