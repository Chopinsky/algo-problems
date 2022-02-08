'''
You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay

Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
Example 3:

Input: steps = 4, arrLen = 2
Output: 8

Constraints:

1 <= steps <= 500
1 <= arrLen <= 10^6
'''


from functools import lru_cache


class Solution:
  def numWays(self, steps: int, arrLen: int) -> int:
    # has to stay
    if steps == 1:
      return 1
    
    mod = 10**9 + 7
    
    @lru_cache(None)
    def dp(idx: int, rem: int) -> int:
      if rem == 0:
        return 1 if idx == 0 else 0
      
      # out of the bounds or not going to make it
      if idx > rem or idx < 0 or idx >= arrLen:
        return 0
      
      # must moves all the way back to the start
      if idx == rem:
        return 1
      
      return (dp(idx-1, rem-1) + dp(idx, rem-1) + dp(idx+1, rem-1)) % mod
    
    return dp(0, steps)
      