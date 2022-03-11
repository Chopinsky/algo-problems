'''
Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares ' '.
The first player always places 'X' characters, while the second player always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.

Example 1:

Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".
Example 2:

Input: board = ["XOX"," X ","   "]
Output: false
Explanation: Players take turns making moves.
Example 3:

Input: board = ["XOX","O O","XOX"]
Output: true

Constraints:

board.length == 3
board[i].length == 3
board[i][j] is either 'X', 'O', or ' '.
'''


from typing import List


class Solution:
  def validTicTacToe(self, b: List[str]) -> bool:
    oc = sum([row.count('O') for row in b])
    xc = sum([row.count('X') for row in b])
    # print(oc, xc)
    
    if oc > xc or xc > oc+1:
      return False

    def count_wins(s: str) -> int:
      tgt = s*3
      rows, cols, diag = 0, 0, 0
      
      # rows
      for i in range(3):
        rows += 1 if b[i] == tgt else 0
      
      if rows >= 2:
        return -1
      
      # cols
      for j in range(3):
        cols += 1 if (b[0][j]+b[1][j]+b[2][j]) == tgt else 0
        
      if cols >= 2:
        return -1
        
      # diag
      diag += 1 if (b[0][0]+b[1][1]+b[2][2]) == tgt else 0
      diag += 1 if (b[0][2]+b[1][1]+b[2][0]) == tgt else 0
      
      return diag+rows+cols
    
    xw = count_wins('X')
    ow = count_wins('O')
    # print(ow, xw)
      
    if ow < 0 or xw < 0:
      return False
    
    # no one wins
    if ow == 0 and xw == 0:
      return True
    
    # 'O' wins
    if xw == 0 and (ow == 2 or ow == 1) and oc == xc:
      return True
    
    if ow == 0 and (xw == 2 or xw == 1) and oc+1 == xc:
      return True
    
    return False
  
    # return (ow == 1 and xw == 0) or (ow == 0 and xw == 1) or (ow == xw and ow == 0) or (ow == 2 and xw == 0) or (ow == 0 and xw == 2)
  