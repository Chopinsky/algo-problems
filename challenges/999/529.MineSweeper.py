'''
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

Example 1:

Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

Example 2:

Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 50
board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
click.length == 2
0 <= clickr < m
0 <= clickc < n
board[clickr][clickc] is either 'M' or 'E'.
'''


from typing import List


class Solution:
  def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    x, y = click
    if board[x][y] != 'M' and board[x][y] != 'E':
      return board
    
    if board[x][y] == 'M':
      board[x][y] = 'X'
      return board
    
    h, w = len(board), len(board[0])
    seen = set([(x, y)])
    stack = [(x, y)]
    dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    
    def count(x: int, y: int) -> int:
      nonlocal h, w
      c = 0
      
      for dx, dy in dirs:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= h or y0 < 0 or y0 >= w:
          continue
          
        if board[x0][y0] == 'M':
          c += 1
      
      return c
    
    while stack:
      x, y = stack.pop()
      
      # find how many mines are in the neighborhood
      c = count(x, y)
      if c > 0:
        board[x][y] = str(c)
        continue
        
      # a blank cell, add adjacent ones for later checks
      board[x][y] = 'B'
      
      # a blank cell, add adjacent ones
      for dx, dy in dirs:
        x0, y0 = x+dx, y+dy
        
        # out of the bound
        if x0 < 0 or x0 >= h or y0 < 0 or y0 >= w or (x0, y0) in seen:
          continue
        
        # not an unrevealed cell
        if board[x0][y0] != 'M' and board[x0][y0] != 'E':
          continue
          
        seen.add((x0, y0))
        stack.append((x0, y0))
    
    return board