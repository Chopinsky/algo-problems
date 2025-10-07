'''
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  def swimInWater(self, grid: List[List[int]]) -> int:
    time = {(0, 0): grid[0][0]}
    m = len(grid)
    n = len(grid)
    h = [(grid[0][0], 0, 0)]

    while h:
      t0, x0, y0 = heappop(h)
      if x0 == m-1 and y0 == n-1:
        return t0

      if (x0, y0) in time and t0 > time[x0, y0]:
        continue

      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x1 = x0 + dx
        y1 = y0 + dy
        if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
          continue

        t1 = max(t0, grid[x1][y1])
        if (x1, y1) in time and t1 >= time[x1, y1]:
          continue

        time[x1, y1] = t1
        heappush(h, (t1, x1, y1))

    return -1
        
  def swimInWater(self, grid: List[List[int]]) -> int:
    cand = [[grid[0][0], 0, 0]]
    dirs = [-1, 0, 1, 0, -1]
    
    h, w = len(grid), len(grid[0])
    t = [[-1 if (i != 0 or j != 0) else grid[0][0] for i in range(w)] for j in range(h)]
    # print(t)
    
    while len(cand) > 0:
      [time, x, y] = heappop(cand)
      # print(time, x, y, cand)
      
      for i in range(4):
        x0, y0 = x+dirs[i], y+dirs[i+1]
        if x0 < 0 or x0 >= h or y0 < 0 or y0 >= w:
          continue
          
        best_time = max(time, grid[x0][y0])
        if t[x0][y0] >= 0 and best_time >= t[x0][y0]:
          continue
          
        if x0 == h-1 and y0 == w-1:
          return best_time
          
        heappush(cand, [max(time, grid[x0][y0]), x0, y0])
        t[x0][y0] = best_time
        
    return -1
          