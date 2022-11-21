'''
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:

Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:

Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.

Constraints:

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.
'''


from typing import List


class Solution:
  def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
    m, n = len(maze), len(maze[0])
    step = 0
    curr, nxt = [tuple(entrance)], []
    seen = set(curr)
    
    while curr:
      step += 1
      
      for x, y in curr:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          xx, yy = x+dx, y+dy
          if xx < 0 or xx >= m or yy < 0 or yy >= n:
            continue
            
          if (xx, yy) in seen or maze[xx][yy] == '+':
            continue
            
          if xx == 0 or xx == m-1 or yy == 0 or yy == n-1:
            return step
          
          seen.add((xx, yy))
          nxt.append((xx, yy))
    
      curr, nxt = nxt, curr
      nxt.clear()
    
    return -1
    

  def nearestExit(self, maze: List[List[str]], e: List[int]) -> int:
    h, w = len(maze)-1, len(maze[0])-1
    stack, nxt = set([(e[0], e[1])]), set()
    seen = set([(e[0], e[1])])
    dirs = [-1, 0, 1, 0, -1]
    steps = 0
    
    while stack:
      steps += 1
      # print(steps, stack, seen)
      
      for x, y in stack:        
        for i in range(4):
          x0, y0 = x+dirs[i], y+dirs[i+1]
          if x0 < 0 or x0 > h or y0 < 0 or y0 > w or maze[x0][y0] == '+':
            continue
            
          dot = (x0, y0)
          if dot in seen or dot in nxt:
            continue
            
          if x0 == 0 or y0 == 0 or x0 == h or y0 == w:
            return steps
          
          nxt.add(dot)
          seen.add(dot)
      
      stack, nxt = nxt, stack
      nxt.clear()
      
    return -1
    