'''
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:

Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

Example 3:

Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 10 ** 4
1 <= startTime[i] < endTime[i] <= 10 ** 9
1 <= profit[i] <= 10 ** 4
'''

from typing import List
from bisect import bisect_right


class Solution:
  def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    src = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)], key=lambda x: (x[1], x[0]))
    
    t = [0]
    p = [0]
    
    for s, e, p0 in src:
      idx = bisect_right(t, s)-1
      p1 = p0 + (p[idx] if idx >= 0 else 0)
      p2 = max(p[-1], p1)
      
      # print('state', t, p)
      # print((s, e, p0), idx, p1, p2)
      
      if e == t[-1]:
        p[-1] = p2
      else:
        p.append(p2)
        t.append(e)
    
    return p[-1]
    

  def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    best_profit = 0
    ln = len(startTime), len(endTime)
    dp = [0] * ln
    
    events = [(endTime[i], i, 1) for i in range(ln)] + [(startTime[i], i, 0) for i in range(ln)]
    events.sort(key=lambda x: x[0])
    
    for _, i, typ in events:
      # print(time, i, typ)
      if typ == 0:
        dp[i] = best_profit + profit[i]
      else:
        best_profit = max(best_profit, dp[i])
    
    return best_profit
  