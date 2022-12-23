'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:

Input: prices = [1]
Output: 0

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''


from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    done = 0
    stage = -math.inf
    entry = -prices[0]
    
    for val in prices[1:]:
      # if sell here, we finish 1 round trip, 
      # update the profit to be staged
      last_stage = stage
      stage = val + entry
      
      # new entry is to buy here, compared with 
      # previous max profit
      entry = max(entry, done-val)
      
      # last staged value becomes available 
      # for new entries
      done = max(done, last_stage)
    
    # print(done, stage)
    return max(done, stage)
    
    
  def maxProfit(self, prices: List[int]) -> int:
    own = 0
    out = 0
    cd = 0
    
    for i, p in enumerate(prices):
      if i == 0:
        own -= p
        continue
        
      nxt_own = max(own, cd-p)
      nxt_out = max(out, own+p)

      cd = out
      own, out = nxt_own, nxt_out

    return max(own, out)
  