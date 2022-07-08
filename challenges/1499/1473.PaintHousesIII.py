'''
There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.

Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.

Example 3:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
Output: 5

Example 4:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.
 

Constraints:

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4
'''

from typing import List
from functools import lru_cache
import math


class Solution:
  def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    last_color = -1
    cnt = [0] * m
    
    for i in range(m-1, -1, -1):
      if houses[i] != 0 and houses[i] != last_color:
        cnt[i] = (0 if i == m-1 else cnt[i+1]) + 1
        last_color = houses[i]
      else:
        cnt[i] = 0 if i == m-1 else cnt[i+1]
        
    # print(cnt)
    
    @lru_cache(None)
    def score(i: int, prev: int, t: int) -> int:
      if i >= m:
        return 0 if t == 0 else math.inf
        
      if t < 0:
        return math.inf
        
      if cnt[i] > t+1:
        return math.inf
      
      if houses[i] > 0:
        return score(i+1, houses[i], t - (0 if houses[i] == prev else 1))
      
      c = math.inf
      for j in range(1, n+1):
        nxt_cost = score(i+1, j, t - (0 if j == prev else 1))
        c = min(c, cost[i][j-1] + nxt_cost)
        
      return c
      
    s = score(0, -1, target)
    return -1 if s == math.inf else s


  def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    @lru_cache(None)
    def dp(i: int, curr: int, t: int) -> int:
      if t < 0:
        return -1
      
      if i >= len(houses):
        return 0 if t == 0 else -1
        
      # already painted, skip this one
      if houses[i] > 0:
        # if the same color as last, keep tallying;
        # otherwise, we're starting a new neighbourhood, remove 1 from the target
        return dp(i+1, houses[i], t if houses[i] == curr else t-1)
        
      # not painted, choose wisely
      best = -1
      
      for idx, money in enumerate(cost[i]):
        color = idx+1
        extra = dp(i+1, color, t if color == curr else t-1)
        
        if extra < 0:
          continue
          
        if best < 0 or money+extra < best:
          # print(money, extra)
          best = money + extra
      
      # print(i, curr, t, best)
      return best
    
    return dp(0, -1, target)
  
