'''
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example 1:

Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:

Input: board = [["."]]
Output: 0

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
'''


from typing import List


class Solution:
  def countBattleships(self, board: List[List[str]]) -> int:
    m, n = len(board), len(board[0])
    count = 0
    
    for i in range(m):
      for j in range(n):
        if board[i][j] == '.':
          continue
          
        checked = False
        for dx, dy in [(-1, 0), (0, -1)]:
          x, y = i+dx, j+dy
          if x < 0 or x >= m or y < 0 or y >= n or board[x][y] == '.':
            continue
            
          checked = True
          break
          
        if not checked:
          count += 1
          
    return count

    
  def countBattleships0(self, board: List[List[str]]) -> int:
    checked = set()
    m, n = len(board), len(board[0])
    count = 0
    
    for i in range(m):
      for j in range(n):
        if (i, j) in checked or board[i][j] == '.':
          continue
        
        count += 1
        checked.add((i, j))
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
          x, y = i+dx, j+dy
          if x < 0 or x >= m or y < 0 or y >= n or board[x][y] == '.':
            continue
          
          while 0 <= x < m and 0 <= y < n and board[x][y] == 'X':
            checked.add((x, y))
            x, y = x+dx, y+dy
              
          break
            
    return count
        