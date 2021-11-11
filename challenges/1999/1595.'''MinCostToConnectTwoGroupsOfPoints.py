'''
You are given two groups of points where the first group has size1 
points, the second group has size2 points, and size1 >= size2.

The cost of the connection between any two points are given in an 
size1 x size2 matrix where cost[i][j] is the cost of connecting point 
i of the first group and point j of the second group. The groups are 
connected if each point in both groups is connected to one or more 
points in the opposite group. In other words, each point in the first 
group must be connected to at least one point in the second group, and 
each point in the second group must be connected to at least one point 
in the first group.

Return the minimum cost it takes to connect the two groups.

Example 1:

Input: cost = [[15, 96], [36, 2]]
Output: 17
Explanation: The optimal way of connecting the groups is:
1--A
2--B
This results in a total cost of 17.

Example 2:

Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
Output: 4
Explanation: The optimal way of connecting the groups is:
1--A
2--B
2--C
3--A
This results in a total cost of 4.
Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.

Example 3:

Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
Output: 10
 

Constraints:

size1 == cost.length
size2 == cost[i].length
1 <= size1, size2 <= 12
size1 >= size2
0 <= cost[i][j] <= 100
'''


from typing import List
from functools import lru_cache
from itertools import combinations
import math


class Solution:
  def connectTwoGroups(self, cost: List[List[int]]) -> int:
    m, n = len(cost), len(cost[0])
    min_cost = [min(cost[i][j] for i in range(m)) for j in range(n)]
    
    @lru_cache(None)
    def dfs(i: int, mask: int) -> int:
      if i >= m:
        score = 0
        
        # we've run out of the left nodes, add min cost to connect 
        # nodes on the right to the left nodes
        for j in range(n):
          if mask & (1<<j) == 0:
            score += min_cost[j]
        
      else:
        score = math.inf
        
        # try to connect node i to the right side
        for j in range(n):
          score = min(score, cost[i][j] + dfs(i+1, mask | (1<<j)))
      
      return score
    
    return dfs(0, 0)
  
    
  def connectTwoGroups1(self, cost: List[List[int]]) -> int:
    m, n = len(cost), len(cost[0])
    dp, nxt = [math.inf] * (1<<n), [math.inf] * (1<<n)
    # gmap = defaultdict(list)
    top = (1<<n) - 1
    
    for group in range(1, 1<<n):
      score = 0
      for j in range(n):
        if group & 1<<j > 0:
          score += cost[0][j]
          # gmap[group].append(j)
          
      dp[group] = score
    
    # print('init', dp)
    
    for i in range(1, m):
      c = cost[i]
      least = math.inf
      
      for j in range(n):
        if 1<<j & top > 0:
          least = min(least, c[j])
          
      nxt[top] = dp[top] + least
      
      for g2 in range(1, top-1):
        least = math.inf
        grp = []
        
        for j in range(n):
          if 1<<j & g2 > 0:
            least = min(least, c[j])
            grp.append(j)
      
        # to form the [1, i] -> g2 mapping, the minimum cost is updated
        # if i is not connecting to any new nodes
        nxt[g2] = min(nxt[g2], dp[g2] + least)
        g1 = top^g2
        score = 0
        
        for j in range(n):
          if 1 << j & g1 > 0:
            score += c[j]
            
        nxt[top] = min(nxt[top], dp[g2] + score)
        
        for l in range(1, max(2, len(grp)-1)):
          for sub in combinations(grp, l):            
            score, g1 = 0, 0
            for j in sub:
              score += c[j]  
              g1 |=  1 << j
              
            nxt[g2] = min(nxt[g2], dp[g2^g1]+score)
        
      # print('round', i, nxt)
      dp, nxt = nxt, dp
      nxt = [math.inf] * (1<<n)
      
    # print(dp)
    return dp[-1]
  