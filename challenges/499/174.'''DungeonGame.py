'''
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Example 1:

Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.

Example 2:

Input: dungeon = [[0]]
Output: 1
 

Constraints:

m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000
'''


import math
from typing import List
from heapq import heappop, heappush


class Solution:
  def calculateMinimumHP(self, dun: List[List[int]]) -> int:
    m, n = len(dun), len(dun[0])
    if m == 1 and n == 1:
      return max(1, 1 - dun[0][0])
    
    # min hp requirements for all borders
    hp = [[1 if (i == m or j == n) else math.inf for j in range(n+1)] for i in range(m+1)]
    
    # reverse hero movement
    for i in range(m-1, -1, -1):
      for j in range(n-1, -1, -1):
        if i == m-1:
          # only move to right
          hp[i][j] = hp[i][j+1]
        elif j == n-1:
          # only move to below
          hp[i][j] = hp[i+1][j]
        else:
          # both directions possible, find the 
          # lowest hp requirements to move to
          hp[i][j] = min(hp[i+1][j], hp[i][j+1])
          
        hp[i][j] = max(hp[i][j]-dun[i][j], 1)
        
    return hp[0][0]
  
    
  def calculateMinimumHP0(self, dun: List[List[int]]) -> int:
    m, n = len(dun), len(dun[0])
    if m == 1 and n == 1:
      return max(1, 1 - dun[0][0])
      
    hp = [[-math.inf]*n for _ in range(m)]
    # max-drawdowns, curr, x, y
    q = [(-dun[0][0], -1*min(0, dun[0][0]), 0, 0)]
    dirs = [(0, 1), (1, 0)]
    low = math.inf
    
    while q:
      curr_hp, drawdown, x, y = heappop(q)
      drawdown *= -1
      curr_hp *= -1
      
      # print(x, y, drawdown, curr_hp, hp[x][y])
      # a better solution exists and already visited
      if curr_hp < hp[x][y]:
        continue
        
      hp[x][y] = curr_hp
      
      for dx, dy in dirs:
        x0, y0 = x+dx, y+dy
        if x0 >= m or y0 >= n:
          continue
          
        nxt_hp = curr_hp + dun[x0][y0]
        nxt_dd = drawdown if nxt_hp >= drawdown else nxt_hp
        
        if x0 == m-1 and y0 == n-1:
          # print(1-nxt_dd)
          low = min(low, 1 - nxt_dd)
        
        heappush(q, (-nxt_hp, -nxt_dd, x0, y0))        
    
    # for r in hp:
    #   print(r)
    
    return low
  