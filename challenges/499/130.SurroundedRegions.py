'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:

Input: board = [["X"]]
Output: [["X"]]

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''


from typing import List


class Solution:
  def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    
    m, n = len(board), len(board[0])
    checked = set()
    
    def develop(i: int, j: int):
      stack = [(i, j)]
      points = set(stack)
      checked.add((i, j))
      on_boarder = False
      
      while stack:
        x, y = stack.pop()
        if x == m-1 or x == 0 or y == n-1 or y == 0:
          # print(x, y)
          on_boarder = True
          
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
            continue
          
          # print('nxt', i, j, x, y, x0, y0, checked)

          if board[x0][y0] == 'X' or (x0, y0) in checked:
            continue
            
          checked.add((x0, y0))
          points.add((x0, y0))
          stack.append((x0, y0))

      # print(i, j, points, on_boarder)
      
      if not on_boarder:
        for x, y in points:
          board[x][y] = 'X'
          
    for i in range(m):
      for j in range(n):
        if (i, j) not in checked and board[i][j] == 'O':
          develop(i, j)
        