'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10]
Output: 1

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
'''

from typing import List

class Solution:
  '''
  idea is to accumulate possible ways with addition of each coin to the
  collection
  '''
  def change(self, amount: int, coins: List[int]) -> int:
    dp = [0 if i > 0 else 1 for i in range(amount+1)]
    
    for c in coins:
      for amnt in range(amount-c+1):
        # accumulate existing ways
        if dp[amnt]:
          dp[amnt+c] += dp[amnt]
    
    return dp[amount]


  def change0(self, amount: int, coins: List[int]) -> int:
    if amount == 0:
      return 1

    n = len(coins)
    dp = [[0] * (amount+1) for _ in range(n)]
    presums = [0] * (amount+1)

    for i in range(n):
      coin = coins[i]

      for j in range(max(1, j), amount+1):
        if j == coin:
          dp[i][j] += 1

        if j > coin and dp[i][j-coin] > 0:
          dp[i][j] += dp[i][j-coin]

        if i > 0 and j > coin:
          dp[i][j] += presums[j-coin]

      for j in range(1, amount+1):
        presums[j] += dp[i][j]

    # print(dp)

    counts = 0
    for i in range(n):
      counts += dp[i][amount]

    return counts
