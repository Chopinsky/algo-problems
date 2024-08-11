'''
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

Example 1:

Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:

Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
'''

from typing import List

class Solution:
  def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    curr = (rStart, cStart)
    count = rows * cols
    ans = []
    visited = [[False]*cols for _ in range(rows)]
    
    def add(x, y):
      if 0 <= x < rows and 0 <= y < cols and not visited[x][y]:
        visited[x][y] = True
        ans.append((x, y))
    
    def right(start, steps):
      x, y = start
      add(x, y)
      
      while y < cols:
        y += 1
        steps -= 1
        add(x, y)
        # print('right:', (x, y), steps, ans, visited)
          
        # need to turn
        if x+1 < rows and 0 <= y < cols and not visited[x+1][y]:
          break
          
        if steps == 0:
          break
      
      return (x, y)
    
    def down(start, steps):
      x, y = start
      add(x, y)
      
      while x < rows:
        x += 1
        steps -= 1
        add(x, y)
        # print('down:', (x, y), steps, ans)
          
        # need to turn
        if y-1 >= 0 and 0 <= x < rows and not visited[x][y-1]:
          break
          
        if steps == 0:
          break
      
      return (x, y)
    
    def left(start, steps):
      x, y = start
      add(x, y)
      
      while y >= 0:
        y -= 1
        steps -= 1
        add(x, y)
        # print('left:', (x, y), steps, ans)
        
        # turn
        if x-1 >= 0 and cols > y >= 0 and not visited[x-1][y]:
          break
          
        if steps == 0:
          break
      
      return (x, y)
    
    def up(start, steps):
      x, y = start
      add(x, y)
      
      while x >= 0:
        x -= 1
        steps -= 1
        add(x, y)
        # print('up:', (x, y), steps, steps)
          
        # turn
        if y+1 < cols and rows > x >= 0 and not visited[x][y+1]:
          break
          
        if steps == 0:
          break
      
      return (x, y)
    
    ln = 1
    while len(ans) < count:
      curr = right(curr, ln)
      curr = down(curr, ln)
      ln += 1
      
      curr = left(curr, ln)
      curr = up(curr, ln)
      ln += 1
      
    return ans
      
  def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    ans = []
    ans.append([rStart, cStart])
    size = 2
    x = rStart - 1
    y = cStart + 1
    
    while len(ans) < rows * cols:
      for _ in range(0, size):
        x += 1
        # print("d", x, y)
        if 0 <= x < rows and 0 <= y < cols:
          ans.append([x, y])
          
      for _ in range(0, size):
        y -= 1
        # print("l", x, y)
        if 0 <= x < rows and 0 <= y < cols:
          ans.append([x, y])
          
      for _ in range(0, size):
        x -= 1
        # print("u", x, y)
        if 0 <= x < rows and 0 <= y < cols:
          ans.append([x, y])
          
      for _ in range(0, size):
        y += 1
        # print("r", x, y)
        if 0 <= x < rows and 0 <= y < cols:
          ans.append([x, y])
      
      size += 2
      y += 1
      x -= 1
    
    return ans
  