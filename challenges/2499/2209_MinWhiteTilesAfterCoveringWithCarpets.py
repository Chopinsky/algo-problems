'''
You are given a 0-indexed binary string floor, which represents the colors of tiles on a floor:

floor[i] = '0' denotes that the ith tile of the floor is colored black.
On the other hand, floor[i] = '1' denotes that the ith tile of the floor is colored white.
You are also given numCarpets and carpetLen. You have numCarpets black carpets, each of length carpetLen tiles. Cover the tiles with the given carpets such that the number of white tiles still visible is minimum. Carpets may overlap one another.

Return the minimum number of white tiles still visible.

Example 1:


Input: floor = "10110101", numCarpets = 2, carpetLen = 2
Output: 2
Explanation: 
The figure above shows one way of covering the tiles with the carpets such that only 2 white tiles are visible.
No other way of covering the tiles with the carpets can leave less than 2 white tiles visible.
Example 2:


Input: floor = "11111", numCarpets = 2, carpetLen = 3
Output: 0
Explanation: 
The figure above shows one way of covering the tiles with the carpets such that no white tiles are visible.
Note that the carpets are able to overlap one another.
 

Constraints:

1 <= carpetLen <= floor.length <= 1000
floor[i] is either '0' or '1'.
1 <= numCarpets <= 1000
'''

import math
from functools import lru_cache


class Solution:
  def minimumWhiteTiles(self, floor: str, num: int, ln: int) -> int:
    n = len(floor)
    count = 0
    
    for val in floor:
      count += int(val)

    if ln == 1:
      return max(0, count - num)

    if num * ln >= n:
      return 0

    if count == n:
      return len(floor) - num * ln
    
    if num * ln >= n:
      return 0
    
    suffix = [int(val) for val in floor]
    for i in range(n-2, -1, -1):
      suffix[i] += suffix[i+1]
    
    # bottom up
    dp = [[suffix[i]] * (num+1) for i in range(n)]
    
    for i in range(n-1, -1, -1):
      for j in range(1, num+1):
        if i == n-1:
          dp[i][j] = 1 if floor[i] == '1' and j == 0 else 0
          continue
        
        if j >= suffix[i] or j*ln >= n-i:
          dp[i][j] = 0
          continue
        
        k = min(n-1, i+ln)
        dp[i][j] = min(dp[k][j-1], (1 if floor[i] == '1' else 0) + dp[i+1][j])
      
    # print('after', dp)
    return dp[0][num]
      
        
  def minimumWhiteTiles0(self, floor: str, num: int, ln: int) -> int:
    n = len(floor)
    count = 0
    
    for val in floor:
      count += int(val)

    if ln == 1:
      return max(0, count - num)

    if num * ln >= n:
      return 0

    if count == n:
      return len(floor) - num * ln
    
    if num * ln >= n:
      return 0
    
    suffix = [int(val) for val in floor]
    for i in range(n-2, -1, -1):
      suffix[i] += suffix[i+1]
    
    # print(suffix)
    
    @lru_cache(None)
    def dp(i: int, rem: int) -> int:
      if i >= n:
        return math.inf if rem < 0 else 0
      
      # no more carpet left, return the remainder white
      # floors from i forward
      if rem == 0:
        return suffix[i]

      # we can use all remain carpets to cover all white floors
      if rem >= suffix[i] or rem*ln >= n-i:
        return 0
      
      return min(
        # if use carpet here
        dp(i+ln, rem-1),  
        # if don't use carpet here
        (1 if floor[i] == '1' else 0) + dp(i+1, rem))
      
    return dp(0, num)
  