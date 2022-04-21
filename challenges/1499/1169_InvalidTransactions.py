'''
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
'''

from typing import List
from collections import defaultdict


class Solution:
  def invalidTransactions(self, transactions: List[str]) -> List[str]:
    invalid = set()
    t_lst = []
    
    for i, t in enumerate(transactions):
      data = t.split(',')
      data[1] = int(data[1])
      data[2] = int(data[2])
      t_lst.append((data, i))
      # print(data)
      
    t_lst.sort(key=lambda x: x[0][1])
    # print(t_lst)
    
    for idx, (d, i) in enumerate(t_lst):
      if d[2] > 1000:
        invalid.add(i)
        
      for j in range(idx-1, -1, -1):
        if d[1] - t_lst[j][0][1] > 60:
          break
          
        if d[0] == t_lst[j][0][0] and d[3] != t_lst[j][0][3]:
          invalid.add(i)
          invalid.add(t_lst[j][1])
      
    return [transactions[i] for i in invalid]
  