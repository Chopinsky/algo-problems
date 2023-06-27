'''
2462. Total Cost to Hire K Workers

You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.

Example 1:

Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.
Example 2:

Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
- In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
The total hiring cost is 4.

Constraints:

1 <= costs.length <= 10^5
1 <= costs[i] <= 10^5
1 <= k, candidates <= costs.length
'''

from heapq import heappush, heappop
from typing import List


class Solution:
  def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    n = len(costs)
    if k >= n:
      return sum(costs)
    
    left, right = [], []
    l, r = 0, n-1
    
    while l <= r and len(left) < candidates:
      heappush(left, costs[l])
      l += 1
      
    while l <= r and len(right) < candidates:
      heappush(right, costs[r])
      r -= 1
      
    total = 0
    # print(l, r, left, right)
    
    while k > 0:
      # print(k, left, right)
      k -= 1
      
      if left and not right:
        # print('from left', left[0])
        total += heappop(left)
      elif right and not left:
        # print('from right', right[0])
        total += heappop(right)
      elif left[0] <= right[0]:
        # print('from left', left[0])
        total += heappop(left)
      else:
        # print('from right', right[0])
        total += heappop(right)
      
      if l <= r and len(left) < candidates:
        heappush(left, costs[l])
        l += 1
        
      if l <= r and len(right) < candidates:
        heappush(right, costs[r])
        r -= 1
      
    return total
      
      
  def totalCost(self, costs: List[int], k: int, m: int) -> int:
    total = 0
    stack = []
    n = len(costs)
    l, r = 0, n-1
    
    while l <= r and len(stack) < 2*m:
      heappush(stack, (costs[l], l, 0))
      if l != r:
        heappush(stack, (costs[r], r, 1))
        
      l += 1
      r -= 1
    
    # print(stack)
    while stack and k > 0:
      c, _, from_left = heappop(stack)
      total += c
      k -= 1
      
      if l <= r:
        if from_left == 0:
          heappush(stack, (costs[l], l, 0))
          l += 1
          
        else:
          heappush(stack, (costs[r], r, 1))
          r -= 1
    
    return total
    