'''
A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following rules:

The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
The character '.' represents the floor which means a free cell to walk.
The character '#' represents the wall which means an obstacle (impossible to walk there).
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

 

Example 1:


Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.
Example 2:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1
Example 3:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation:  push the box down, left, left, up and up.
Example 4:

Input: grid = [["#","#","#","#","#","#","#"],
               ["#","S","#",".","B","T","#"],
               ["#","#","#","#","#","#","#"]]
Output: -1

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid contains only characters '.', '#', 'S', 'T', or 'B'.
There is only one character 'S', 'B', and 'T' in the grid.
'''


from typing import List
from functools import lru_cache
from collections import deque


class Solution:
  def minPushBox(self, grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    box = None
    player = None
    target = None
    
    # find interesting points
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 'S':
          player = (i, j)
          
        if grid[i][j] == 'B':
          box = (i, j)
          
        if grid[i][j] == 'T':
          target = (i, j)
          
    if box == target:
      return 0
    
    # check if the player can go from (x0, y0) to (x1, y1) with box at (bx, by)
    @lru_cache(None)
    def has_access(x0: int, y0: int, x1: int, y1: int, bx: int, by: int) -> bool:
      if x0 == x1 and y0 == y1:
        return True
      
      stack = [(x0, y0)]
      visited = set(stack)
      
      while stack:
        x, y = stack.pop()
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
          xx, yy = x+dx, y+dy
          if xx < 0 or xx >= m or yy < 0 or yy >= n:
            continue
            
          if grid[xx][yy] == '#' or (xx == bx and yy == by) or (xx, yy) in visited:
            continue
            
          if xx == x1 and yy == y1:
            return True
          
          stack.append((xx, yy))
          visited.add((xx, yy))
        
      return False
    
    # find potential moves when the box is at (bx, by)
    def find_moves(bx: int, by: int) -> List[List[int]]:
      ans = []
      for dx, dy in [(-1, 0), (0, -1)]:
        x0, y0 = bx+dx, by+dy
        x1, y1 = bx-dx, by-dy
        
        if 0 <= x0 < m and 0 <= y0 < n and 0 <= x1 < m and 0 <= y1 < n and grid[x0][y0] != '#' and grid[x1][y1] != '#':
          ans.append((x0, y0, x1, y1))
          ans.append((x1, y1, x0, y0))
        
      return ans
    
    stack = deque([])
    visited = set()

    # build initial positions
    for x0, y0, x1, y1 in find_moves(box[0], box[1]):
      if has_access(player[0], player[1], x0, y0, box[0], box[1]):
        stack.append((1, box[0], box[1], x1, y1))
        visited.add((x0, y0, box[0], box[1]))
        visited.add((box[0], box[1], x1, y1))
        
    # bfs all possible moves
    while stack:
      moves, px, py, bx, by = stack.popleft()
      # print(moves, 'box:', bx, by, 'player:', px, py)
      
      if bx == target[0] and by == target[1]:
        return moves
      
      for x0, y0, x1, y1 in find_moves(bx, by):
        if (bx, by, x1, y1) in visited:
          continue
        
        # print('nxt move:', 'b:', x1, y1, 'p:', bx, by)
        if has_access(px, py, x0, y0, bx, by):
          stack.append((moves+1, bx, by, x1, y1))
          visited.add((bx, by, x1, y1))
      
    return -1
    