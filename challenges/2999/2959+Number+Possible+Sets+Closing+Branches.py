'''
2959. Number of Possible Sets of Closing Branches

There is a company with n branches across the country, some of which are connected by roads. Initially, all branches are reachable from each other by traveling some roads.

The company has realized that they are spending an excessive amount of time traveling between their branches. As a result, they have decided to close down some of these branches (possibly none). However, they want to ensure that the remaining branches have a distance of at most maxDistance from each other.

The distance between two branches is the minimum total traveled length needed to reach one branch from another.

You are given integers n, maxDistance, and a 0-indexed 2D array roads, where roads[i] = [ui, vi, wi] represents the undirected road between branches ui and vi with length wi.

Return the number of possible sets of closing branches, so that any branch has a distance of at most maxDistance from any other.

Note that, after closing a branch, the company will no longer have access to any roads connected to it.

Note that, multiple roads are allowed.

Example 1:

Input: n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]
Output: 5
Explanation: The possible sets of closing branches are:
- The set [2], after closing, active branches are [0,1] and they are reachable to each other within distance 2.
- The set [0,1], after closing, the active branch is [2].
- The set [1,2], after closing, the active branch is [0].
- The set [0,2], after closing, the active branch is [1].
- The set [0,1,2], after closing, there are no active branches.
It can be proven, that there are only 5 possible sets of closing branches.
Example 2:

Input: n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
Output: 7
Explanation: The possible sets of closing branches are:
- The set [], after closing, active branches are [0,1,2] and they are reachable to each other within distance 4.
- The set [0], after closing, active branches are [1,2] and they are reachable to each other within distance 2.
- The set [1], after closing, active branches are [0,2] and they are reachable to each other within distance 2.
- The set [0,1], after closing, the active branch is [2].
- The set [1,2], after closing, the active branch is [0].
- The set [0,2], after closing, the active branch is [1].
- The set [0,1,2], after closing, there are no active branches.
It can be proven, that there are only 7 possible sets of closing branches.
Example 3:

Input: n = 1, maxDistance = 10, roads = []
Output: 2
Explanation: The possible sets of closing branches are:
- The set [], after closing, the active branch is [0].
- The set [0], after closing, there are no active branches.
It can be proven, that there are only 2 possible sets of closing branches.

Constraints:

1 <= n <= 10
1 <= maxDistance <= 10^5
0 <= roads.length <= 1000
roads[i].length == 3
0 <= ui, vi <= n - 1
ui != vi
1 <= wi <= 1000
All branches are reachable from each other by traveling some roads.
'''

import math
from typing import List


class Solution:
  def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
    if n == 1:
      return 2
    
    if n == 2:
      dist = min(w for _, _, w in roads)
      return 3 + (1 if dist <= maxDistance else 0)
        
    mask = (1 << n) - 1
    count = 1
    d0 = [[math.inf]*n for _ in range(n)]
    
    for u, v, w in roads:
      d0[u][v] = min(d0[u][v], w)
      d0[v][u] = min(d0[v][u], w)
    
    def get_cell(mask: int, i: int, j: int):
      if (1<<i) & mask == 0:
        return math.inf
      
      if (1<<j) & mask == 0:
        return math.inf
      
      if d0[i][j] > maxDistance:
        return math.inf
      
      return d0[i][j]

    # use Floyd-Warshall algorithm to find the min-distance between any
    # vertex-pair; time complexity is O(n^3), space complexity is O(n^2)
    def test(v_mask: int) -> bool:
      v_cnt = (bin(v_mask)[2:]).count('1')
      if v_cnt == 1:
        return True

      # d1 only has edges with remaining vertices
      d1 = [[get_cell(v_mask, i, j) for j in range(n)] for i in range(n)]
      
      # k is the intermediate node
      for k in range(n):
        if (1<<k) & v_mask == 0:
          continue
          
        # i is the start node
        for i in range(n):
          if (1<<i) & v_mask == 0:
            continue
            
          for j in range(n):
            if (1<<j) & v_mask == 0:
              continue
            
            d1[i][j] = min(d1[i][j], d1[i][k]+d1[k][j])
      
      # print('loop:', bin(v_mask)[2:], d1)
      for i in range(n):
        if (1<<i) & v_mask == 0:
          continue

        for j in range(i+1, n):
          if (1<<j) & v_mask == 0:
            continue
            
          if d1[i][j] > maxDistance:
            return False
          
      return True
    
    # print('init:', d0)
    while mask > 0:
      if test(mask):
        count += 1
      
      mask -= 1
      
    return count
      