'''
You are given a 0-indexed 2D integer array grid of size m x n which represents a field. Each cell has one of three values:

0 represents grass,
1 represents fire,
2 represents a wall that you and fire cannot pass through.
You are situated in the top-left cell, (0, 0), and you want to travel to the safehouse at the bottom-right cell, (m - 1, n - 1). Every minute, you may move to an adjacent grass cell. After your move, every fire cell will spread to all adjacent cells that are not walls.

Return the maximum number of minutes that you can stay in your initial position before moving while still safely reaching the safehouse. If this is impossible, return -1. If you can always reach the safehouse regardless of the minutes stayed, return 109.

Note that even if the fire spreads to the safehouse immediately after you have reached it, it will be counted as safely reaching the safehouse.

A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

Example 1:


Input: grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
Output: 3
Explanation: The figure above shows the scenario where you stay in the initial position for 3 minutes.
You will still be able to safely reach the safehouse.
Staying for more than 3 minutes will not allow you to safely reach the safehouse.
Example 2:

Input: grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
Output: -1
Explanation: The figure above shows the scenario where you immediately move towards the safehouse.
Fire will spread to any cell you move towards and it is impossible to safely reach the safehouse.
Thus, -1 is returned.
Example 3:

Input: grid = [[0,0,0],[2,2,0],[1,2,0]]
Output: 1000000000
Explanation: The figure above shows the initial grid.
Notice that the fire is contained by walls and you will always be able to safely reach the safehouse.
Thus, 109 is returned.

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 300
4 <= m * n <= 2 * 10^4
grid[i][j] is either 0, 1, or 2.
grid[0][0] == grid[m - 1][n - 1] == 0
'''

import math
from typing import List


class Solution:
  '''
  trick is to guess if we can escape after `t`-delays using binary search -- `t` must be in 
  the range of [0, m*n], and we can't go to the cell where the fire will arrive before the 
  earliest moment that we can reach the cell
  '''
  def maximumMinutes(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    fs, nxt = set(), set()
    grass = 0
    
    for x in range(m):
      for y in range(n):
        if grid[x][y] == 1:
          fs.add((x, y))
        elif grid[x][y] == 0:
          grass += 1
        
    if (0, 0) in fs or (m-1, n-1) in fs:
      return -1
    
    fire = [[math.inf]*n for _ in range(m)]
    t = 0
    for x, y in fs:
      fire[x][y] = t
      
    while fs:
      t += 1
      for x, y in fs:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] == 2:
            continue
            
          if t < fire[x0][y0]:
            nxt.add((x0, y0))
            fire[x0][y0] = t
      
      fs, nxt = nxt, fs
      nxt.clear()
      
    # print(fire)
    
    def can_escape(delay: int) -> bool:
      if delay >= fire[0][0]:
        return False
      
      curr, nxt = [(0, 0)], []
      visited = set(curr)
      t = delay
      
      while curr:
        t += 1
        for x, y in curr:
          for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x0, y0 = x+dx, y+dy
            if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] == 2 or (x0, y0) in visited:
              continue
              
            if x0 == m-1 and y0 == n-1 and fire[x0][y0] >= t:
              return True
            
            # fire already comes here, can't go
            if fire[x0][y0] <= t:
              continue
              
            visited.add((x0, y0))
            nxt.append((x0, y0))
        
        curr, nxt = nxt, curr
        nxt.clear()
        
      return False
    
    l, r = 0, grass+1
    last = l
    
    if not can_escape(0):
      return -1
    
    while l < r:
      mid = (l+r) // 2
      if can_escape(mid):
        # print('can escape:', mid)
        last = mid
        l = mid + 1
      else:
        # print('can NOT escape:', mid)
        r = mid - 1
      
    if l >= grass:
      return 10**9
      
    return max(l, last) if can_escape(l) else last
    