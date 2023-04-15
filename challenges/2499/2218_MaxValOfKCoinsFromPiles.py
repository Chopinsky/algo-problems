'''
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

Example 1:

Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.
Example 2:

Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
Output: 706
Explanation:
The maximum total can be obtained if we choose all coins from the last pile.
 

Constraints:

n == piles.length
1 <= n <= 1000
1 <= piles[i][j] <= 10^5
1 <= k <= sum(piles[i].length) <= 2000
'''

from typing import List
from functools import lru_cache


class Solution:
  def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
    n = len(piles)
    rem = [len(piles[i]) for i in range(n)]
    for i in range(n-2, -1, -1):
      rem[i] += rem[i+1]
    
    # print('remain:', rem)
    
    @lru_cache(None)
    def dp(i, m):
      if i >= n or m <= 0:
        return 0
      
      if m >= rem[i]:
        return sum(sum(piles[j]) for j in range(i, n))
      
      score = 0
      bound = min(len(piles[i]), m)
      curr = 0
      
      for j in range(bound+1):
        score = max(score, curr + dp(i+1, m-j))
        if j < len(piles[i]):
          curr += piles[i][j]
        
      return score
      
    return dp(0, k)
      
      
  def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
    n = len(piles)
    count = [[len(piles[i]), sum(piles[i])] for i in range(n)]
    
    for i in range(n-2, -1, -1):
      count[i][0] += count[i+1][0]
      count[i][1] += count[i+1][1]
      
    # print(count)
    if k >= count[0][0]:
      return count[0][1]
    
    @lru_cache(None)
    def dp(i: int, rem: int) -> int:
      if i >= n:
        return 0
      
      # we can take all coints from the remainder piles
      if rem >= count[i][0]:
        return count[i][1]
      
      curr = 0
      score = dp(i+1, rem)
      
      for j in range(min(len(piles[i]), rem)):
        curr += piles[i][j]
        score = max(score, curr + dp(i+1, rem-j-1))
        
      return score
      
    return dp(0, k)
  