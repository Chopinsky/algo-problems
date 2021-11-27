from typing import List
from functools import lru_cache


class Solution:
  def stoneGameV(self, stones: List[int]) -> int:
    n = len(stones)
    if n < 2:
      return 0

    presum = [val for val in stones]
    for i in range(1, n):
      presum[i] += presum[i-1]

    @lru_cache(None)
    def dp(i: int, j: int) -> int:
      if i == j:
        return 0

      if i == j-1:
        return min(stones[i:j+1])

      score = 0

      for k in range(i, j):
        sl = presum[k] - (presum[i-1] if i > 0 else 0)
        sr = presum[j] - presum[k]

        if sl > sr:
          score = max(score, sr + dp(k, j))
        elif sr > sl:
          score = max(score, sl + dp(i, k))
        else:
          score = max(score, sl + dp(k, j), sr + dp(i, k))

      return score

    return dp(0, n-1)


  def stoneGameV0(self, stones: List[int]) -> int:
    n = len(stones)
    if n < 2:
      return 0
    
    presum = [val for val in stones]
    for i in range(1, n):
      presum[i] += presum[i-1]
    
    dp = [[0 for _ in range(n)] for _ in range(n)]
    top = [[stones[i] if i == j else 0 for j in range(n)] for i in range(n)]
    
    for j in range(1, n):
      mid = j
      total = stones[j]
      right = 0
      
      # now considering range [i, j]
      for i in range(j-1, -1, -1):
        total += stones[i]
        
        # shifting to get the optimal left/right dividing point 
        # since left bound `i` is moving from `j-1` to 0 in this 
        # process
        while (right + stones[mid]) * 2 <= total:
          right += stones[mid]
          mid -= 1
          
        if right * 2 == total:
          dp[i][j] = top[i][mid]
          
        else:
          dp[i][j] = 0 if mid == i else top[i][mid-1]
          
        dp[i][j] = max(dp[i][j], 0 if mid == j else top[j][mid+1])
        top[i][j] = max(top[i][j-1], dp[i][j] + total)
        top[j][i] = max(top[j][i+1], dp[i][j] + total)
    
    return dp[0][n-1]
