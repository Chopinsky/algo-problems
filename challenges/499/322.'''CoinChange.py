'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Example 4:

Input: coins = [1], amount = 1
Output: 1

Example 5:

Input: coins = [1], amount = 2
Output: 2

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
'''


from typing import List
from collections import deque


class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    q = deque([0])
    count = {0: 0}
    
    while q:
      curr_amnt = q.popleft()
      if curr_amnt == amount:
        return count[amount]
      
      for c in coins:
        nxt_amnt = curr_amnt + c
        curr_cnt = count[curr_amnt]
        
        # overshoot or better solution exists
        if nxt_amnt > amount or (nxt_amnt in count and count[nxt_amnt] <= 1+curr_cnt):
          continue
        
        q.append(nxt_amnt)
        count[nxt_amnt] = 1 + curr_cnt
      
    return -1
    
    
  def coinChange0(self, coins: List[int], amount: int) -> int:
    if amount == 0:
      return 0
    
    if len(coins) == 1:
      return amount//coins[0] if (amount%coins[0] == 0) else -1
    
    dp = [-1] * (amount+1)
    dp[0] = 0
    
    for amnt in range(1, amount+1):
      for c in coins:
        if c > amnt or dp[amnt-c] < 0:
          continue
          
        dp[amnt] = min(dp[amnt], dp[amnt-c]+1) if dp[amnt] >= 0 else dp[amnt-c]+1
      
    return dp[amount]
  