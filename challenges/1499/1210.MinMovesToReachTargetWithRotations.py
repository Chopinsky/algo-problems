'''
In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1). The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).

In one move the snake can:

Move one cell to the right if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
Move down one cell if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).

Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty. In that case the snake moves from (r, c) and (r+1, c) to (r, c) and (r, c+1).

Return the minimum number of moves to reach the target.

If there is no way to reach the target, return -1.

Example 1:

Input: grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
Output: 11
Explanation:
One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].
Example 2:

Input: grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
Output: 9

Constraints:

2 <= n <= 100
0 <= grid[i][j] <= 1
It is guaranteed that the snake starts at empty cells.
'''


from typing import List
from heapq import heappop, heappush


class Solution:
  '''
  alt solution is to use BFS instead of heap (n^2log(n^2) -> n^2), because the snake are moving towards
  bottom right in either moves, there's no going back
  '''
  def minimumMoves(self, grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[n-1][n-1] == 1 or grid[n-1][n-2] == 1:
      return -1
    
    stack = [(0, 0, 1, 0)]
    visited = set()
    
    while stack:
      steps, x, y, alig = heappop(stack)
      # print(steps, x, y, alig)
      
      if x == n-1 and y == n-1 and alig == 0:
        return steps
      
      # move to the right
      if y < n-1 and grid[x][y+1] == 0:
        if (alig == 0) or (alig == 1 and x-1 >= 0 and grid[x-1][y+1] == 0) and (x, y+1, alig) not in visited:
          visited.add((x, y+1, alig))
          heappush(stack, (steps+1, x, y+1, alig))
      
      # move down 
      if x < n-1 and grid[x+1][y] == 0:
        if (alig == 1) or (alig == 0 and y-1 >= 0 and grid[x+1][y-1] == 0) and (x+1, y, alig) not in visited:
          visited.add((x+1, y, alig))
          heappush(stack, (steps+1, x+1, y, alig))

      # clockwise rotate:
      if x < n-1 and (alig == 0 and grid[x+1][y] == 0 and grid[x+1][y-1] == 0) and (x+1, y-1, 1) not in visited:
        visited.add((x+1, y-1, 1))
        heappush(stack, (steps+1, x+1, y-1, 1))
        
      # counter-clockwise rotate:
      if y < n-1 and alig == 1 and grid[x][y+1] == 0 and grid[x-1][y+1] == 0 and (x-1, y+1, 0) not in visited:
        visited.add((x-1, y+1, 0))
        heappush(stack, (steps+1, x-1, y+1, 0))
        
    return -1
  