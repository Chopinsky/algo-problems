'''
1138. Alphabet Board Path

On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"

Constraints:

1 <= target.length <= 100
target consists only of English lowercase letters.
'''


class Solution:
  def alphabetBoardPath(self, target: str) -> str:
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
    pos = {}
    x, y = 0, 0
    res = ''
    
    for i in range(6):
      for j in range(len(board[i])):
        pos[board[i][j]] = (i, j)
    
    # print(pos)
    def get_moves(sx, sy, tx, ty):
      dx = tx-sx
      dy = ty-sy
      
      if dx == 0 and dy == 0:
        return ''
        
      vert = ''
      hor = ''
      
      if dx != 0:
        vert = ('U' if dx < 0 else 'D') * abs(dx)
        
      if dy != 0:
        hor = ('L' if dy < 0 else 'R') * abs(dy)
        
      return vert + hor
    
    last = ''
    for ch in target:
      append = ''
      if ch != last:
        if last == 'z':
          res += 'U'
          x, y = pos['u']
          x0, y0 = pos[ch]
        elif ch == 'z':
          append = 'D'
          x0, y0 = pos['u']
        else:
          x0, y0 = pos[ch]
          
        res += get_moves(x, y, x0, y0)
        x, y = x0, y0
        
      res += append + '!'
      last = ch
    
    return res
  