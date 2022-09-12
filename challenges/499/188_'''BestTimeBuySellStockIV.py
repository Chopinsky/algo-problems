'''
188. Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
'''

from typing import List


class Solution:
  '''
  the idea is that we can remember the entry point of the k-th trade with the knowledge of the
  max profit from the (k-1)-th trade before i-th day; then the max profit for the i-th day with
  the k-th trade is either don't take the sell-trade @ i-th day (i.e., use the best profit if
  sell @ (i-1)-th day), or we sell @ i-th day with the best entry point so far.
  '''
  def maxProfit(self, k: int, prices: List[int]) -> int:
    n = len(prices)
    if n < 2 or k == 0:
      return 0
    
    curr = [0]*n
    while k > 0:
      nxt = [0]*n
      best_entry = -prices[0]
      
      for i in range(1, n):
        # previous profit with (k-1) trades + entry cost of prices[i]
        best_entry = max(best_entry, curr[i-1]-prices[i])
        
        # update the current best profit with (k) trades that finishes at i-th day
        nxt[i] = max(nxt[i-1], best_entry+prices[i])
      
      k -= 1
      curr = nxt
      
    return curr[-1]
    