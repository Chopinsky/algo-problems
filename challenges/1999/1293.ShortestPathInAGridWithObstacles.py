'''
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] == 0 or 1
grid[0][0] == grid[m - 1][n - 1] == 0
'''


from typing import List
from heapq import heappop, heappush


class Solution:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    h, w = len(grid), len(grid[0])
    if h == 1 and w == 1:
      return 0
    
    stack = [(0, -k, 0, 0)]
    dirs = [-1, 0, 1, 0, -1]
    steps = [[-1]*w for _ in range(h)]
    steps[0][0] = k
    
    while stack:
      step, k, x, y = heappop(stack)
      k = -k
      
      for i in range(4):
        x0, y0 = x+dirs[i], y+dirs[i+1]
        if x0 < 0 or x0 >= h or y0 < 0 or y0 >= w:
          continue
          
        k0 = k if grid[x0][y0] == 0 else k-1
        if k0 < 0 or (steps[x0][y0] >= 0 and k0 <= steps[x0][y0]):
          continue
          
        if x0 == h-1 and y0 == w-1:
          return step+1
          
        heappush(stack, (step+1, -k0, x0, y0))
        steps[x0][y0] = k0
        
      # print("after", x, y, k, stack)
        
    return -1
    