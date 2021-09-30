'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:

Input: m = 7, n = 3
Output: 28

Example 4:

Input: m = 3, n = 3
Output: 6

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
'''


class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    dp = [1 for _ in range(n)]
    nxt = []
    
    for i in range(1, m):
      for j in range(n):
        nxt.append((nxt[-1] if j > 0 else 0) + dp[j])
        
      dp, nxt = nxt, dp
      nxt.clear()
      
    return dp[-1]
    