'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
'''


from typing import List
from functools import lru_cache


class Solution:
  def combine(self, n: int, k: int) -> List[List[int]]:
    if n == k:
      return [[i+1 for i in range(k)]]
    
    @lru_cache(None)
    def dp(i: int, rem: int) -> List[int]:
      if rem == 1:
        return [[i]]
      
      if n+1-i == rem:
        return [[val for val in range(i, n+1)]]
      
      ans = []
      for j in range(i+1, n+1):
        if n+2-j < rem:
          break
        
        # print(i, j)
        for arr in dp(j, rem-1):
          if i > 0:
            ans.append([i] + arr)
          else:
            ans.append(arr)
      
      return ans
      
    return dp(0, k+1)
    