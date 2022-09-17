'''
2412. Minimum Money Required Before Transactions

You are given a 0-indexed 2D integer array transactions, where transactions[i] = [costi, cashbacki].

The array describes transactions, where each transaction must be completed exactly once in some order. At any given moment, you have a certain amount of money. In order to complete transaction i, money >= costi must hold true. After performing a transaction, money becomes money - costi + cashbacki.

Return the minimum amount of money required before any transaction so that all of the transactions can be completed regardless of the order of the transactions.

Example 1:

Input: transactions = [[2,1],[5,0],[4,2]]
Output: 10
Explanation:
Starting with money = 10, the transactions can be performed in any order.
It can be shown that starting with money < 10 will fail to complete all transactions in some order.
Example 2:

Input: transactions = [[3,0],[0,3]]
Output: 3
Explanation:
- If transactions are in the order [[3,0],[0,3]], the minimum money required to complete the transactions is 3.
- If transactions are in the order [[0,3],[3,0]], the minimum money required to complete the transactions is 0.
Thus, starting with money = 3, the transactions can be performed in any order.
 

Constraints:

1 <= transactions.length <= 10^5
transactions[i].length == 2
0 <= costi, cashbacki <= 10^9
'''

from typing import List


class Solution:
  '''
  the trick is to consider if transaction-i is the last one to finish, then
  we must have the money that can finish all previous transactions, plus the
  cost to finish this very last one; we pre-calculate the total deficit from
  the cost > disc ones (since that will require larger input money), and update
  the final amount required to finish the transaction-i if it's the last one
  to be done;
  '''
  def minimumMoney(self, t: List[List[int]]) -> int:
    deficit = 0
    min_req = 0

    for cost, disc in t:
      if cost > disc:
        deficit += cost-disc

      min_req += cost

    for cost, disc in t:
      curr_deficit = deficit if cost <= disc else deficit-(cost-disc)
      min_req = max(min_req, cost + curr_deficit)

    return min_req


  '''
  the trick is to sort the transactions accordingly -- for the cost > cashbacks
  batch, the order that puts small discount first and large discount last will require
  the highest amount of initial cash; for the cost <= cashbacks batch, the order that puts
  large discount first and small discount last will require the highest amount of initial 
  cash; we need to finish the cost > cashbacks batch first, then the remainder shall be 
  used to finish the cost <= cashbacks batch, and add the diff on top of the first batch
  as the final result
  '''
  def minimumMoney0(self, t: List[List[int]]) -> int:
    cand = []
    cashbacks = []
    cb_min, cand_min = 0, 0
    
    for cost, disc in t:
      if cost > disc:
        cand.append([cost, disc])
      else:
        cashbacks.append([cost, disc])
    
    cashbacks.sort(key=lambda x: x[1])
    cand.sort(key=lambda x: -x[1])
    # print(cand)
    # print(cashbacks)
    
    for c, d in cashbacks:
      if cb_min - d < 0:
        cb_min = max(cb_min, c)
      else:
        cb_min += c-d
    
    for c, d in cand:
      if cand_min+d < c:
        cand_min += c
      else:
        cand_min += c - d
        
    end_amnt = cand_min - sum(c-d for c, d, in cand)
    # print(end_amnt, cb_min, cand_min)
    
    # must compansate for the deficit that's required to finish the cashback
    # transactions
    return cand_min + max(0, cb_min-end_amnt)
    