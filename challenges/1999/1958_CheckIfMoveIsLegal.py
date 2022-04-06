'''
You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the cell (r, c) on a game board. On the board, free cells are represented by '.', white cells are represented by 'W', and black cells are represented by 'B'.

Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). However, a move is only legal if, after changing it, the cell becomes the endpoint of a good line (horizontal, vertical, or diagonal).

A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color, and the remaining cells in the middle are the opposite color (no cells in the line are free). You can find examples for good lines in the figure below:


Given two integers rMove and cMove and a character color representing the color you are playing as (white or black), return true if changing cell (rMove, cMove) to color color is a legal move, or false if it is not legal.

Example 1:


Input: board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"
Output: true
Explanation: '.', 'W', and 'B' are represented by the colors blue, white, and black respectively, and cell (rMove, cMove) is marked with an 'X'.
The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.
Example 2:


Input: board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"
Output: false
Explanation: While there are good lines with the chosen cell as a middle cell, there are no good lines with the chosen cell as an endpoint.
 

Constraints:

board.length == board[r].length == 8
0 <= rMove, cMove < 8
board[rMove][cMove] == '.'
color is either 'B' or 'W'.
'''

from typing import List


class Solution:
  def checkMove(self, b: List[List[str]], r: int, c: int, color: str) -> bool:
    target = 'W' if color == 'B' else 'B'
    m, n = len(b), len(b[0])
    
    def drift(x: int, y: int, dx: int, dy: int) -> bool:
      x0, y0 = x, y      
      while 0 <= x < m and 0 <= y < n:
        if b[x][y] != target:
          break
          
        x += dx
        y += dy

      # print(target, x0, y0, dx, dy, x, y)
      return 0 <= x < m and 0 <= y < n and b[x][y] == color and (x != x0 or y != y0)
      
    # left
    if drift(r, c-1, 0, -1):
      return True
    
    # right
    if drift(r, c+1, 0, 1):
      return True
    
    # up
    if drift(r-1, c, -1, 0):
      return True
    
    # down
    if drift(r+1, c, 1, 0):
      return True
    
    # up-left
    if drift(r-1, c-1, -1, -1):
      return True
    
    # up-right
    if drift(r-1, c+1, -1, 1):
      return True
    
    # down-left
    if drift(r+1, c-1, 1, -1):
      return True
    
    # down-right
    if drift(r+1, c+1, 1, 1):
      return True
      
    return False
        