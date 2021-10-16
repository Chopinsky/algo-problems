'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:

Input: prices = [1]
Output: 0

Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^5
'''


import math
from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
      return 0
    
    # 1st transactions
    prev_profit = max(0, prices[1]-prices[0])
    prev_low = min(prices[0], prices[1])
    
    # 2nd transactions
    s_profit = 0
    s_low = -math.inf
    
    for i in range(2, n):
      p = prices[i]
      
      # update 2nd transaction profit and lows
      p1 = p + s_low if s_low >= 0 else -math.inf
      s_low = max(s_low, prev_profit-p)
      # print(i, '2nd', p1, s_low, s_profit)
      
      if p1 > s_profit:
        s_profit = max(s_profit, p1)
      
      # update 1st transaction profit and lows
      p0 = p - prev_low
      prev_low = min(prev_low, p)
      # print(i, '1st', p0, prev_low, prev_profit)
      
      if p0 > prev_profit:
        prev_profit = p0
      
    return max(0, prev_profit, s_profit)
  