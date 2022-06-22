'''
You are given two integers m and n that represent the height and width of a rectangular piece of wood. You are also given a 2D integer array prices, where prices[i] = [hi, wi, pricei] indicates you can sell a rectangular piece of wood of height hi and width wi for pricei dollars.

To cut a piece of wood, you must make a vertical or horizontal cut across the entire height or width of the piece to split it into two smaller pieces. After cutting a piece of wood into some number of smaller pieces, you can sell pieces according to prices. You may sell multiple pieces of the same shape, and you do not have to sell all the shapes. The grain of the wood makes a difference, so you cannot rotate a piece to swap its height and width.

Return the maximum money you can earn after cutting an m x n piece of wood.

Note that you can cut the piece of wood as many times as you want.

 

Example 1:


Input: m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]
Output: 19
Explanation: The diagram above shows a possible scenario. It consists of:
- 2 pieces of wood shaped 2 x 2, selling for a price of 2 * 7 = 14.
- 1 piece of wood shaped 2 x 1, selling for a price of 1 * 3 = 3.
- 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2.
This obtains a total of 14 + 3 + 2 = 19 money earned.
It can be shown that 19 is the maximum amount of money that can be earned.
Example 2:


Input: m = 4, n = 6, prices = [[3,2,10],[1,4,2],[4,1,3]]
Output: 32
Explanation: The diagram above shows a possible scenario. It consists of:
- 3 pieces of wood shaped 3 x 2, selling for a price of 3 * 10 = 30.
- 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2.
This obtains a total of 30 + 2 = 32 money earned.
It can be shown that 32 is the maximum amount of money that can be earned.
Notice that we cannot rotate the 1 x 4 piece of wood to obtain a 4 x 1 piece of wood.
 

Constraints:

1 <= m, n <= 200
1 <= prices.length <= 2 * 10^4
prices[i].length == 3
1 <= hi <= m
1 <= wi <= n
1 <= pricei <= 10^6
All the shapes of wood (hi, wi) are pairwise distinct.
'''

from typing import List
from functools import lru_cache


class Solution:
  '''
  the trick is to try all possible piece sizes -- if we can sell the piece as a whole,
  this price is a starting point; otherwise, we set the start point to 0. then we try
  to make a horizontal cut or a vertical cut for all possible cuts, and divide the problem
  and then try to solve it. 
  '''
  def sellingWood0(self, m: int, n: int, prices: List[List[int]]) -> int:
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for w, h, p in prices:
      dp[w][h] = p
      
    for w in range(1, m+1):
      for h in range(1, n+1):
        # try all possible vertical cuts
        for w0 in range(1, w//2+1):
          dp[w][h] = max(dp[w][h], dp[w0][h] + dp[w-w0][h])
          
        # try all possible horizontal cuts
        for h0 in range(1, h//2+1):
          dp[w][h] = max(dp[w][h], dp[w][h0] + dp[w][h-h0])
      
    return dp[m][n]
  
  
  def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
    p = {}
    for h, w, p0 in prices:
      p[h, w] = p0
    
    @lru_cache(None)
    def dp(m: int, n: int) -> int:
      if m == 0 or n == 0:
        return 0
      
      # if we sell the piece as a whole
      s = p[m, n] if (m, n) in p else 0
      
      # horizontal cuts
      for h0 in range(1, m//2+1):
        s = max(s, dp(h0, n) + dp(m-h0, n))
        
      # vertical cuts
      for w0 in range(1, n//2+1):
        s = max(s, dp(m, w0) + dp(m, n-w0))
        
      return s
      
    return dp(m, n)
