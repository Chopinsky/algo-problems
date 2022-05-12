'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

Constraints:

2 <= k <= 9
1 <= n <= 60
'''

from typing import List
from functools import lru_cache


class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    if k*(k+1)//2 > n:
      return []
    
    @lru_cache(None)
    def comb(t: int, val: int, lvl: int):
      if t <= 0 or val > t or val > 9 or lvl > k:
        return []
      
      if lvl == k:
        return [[t]] if t <= 9 else []
            
      res = []
      for x in range(val, t+1):
        for arr in comb(t-x, x+1, lvl+1):
          # print('append:', arr, x, lvl)
          if arr and arr[-1] == x:
            continue
            
          res.append([x] + arr)
          
      # print(res)
      return res
    
    return comb(n, 1, 1)
