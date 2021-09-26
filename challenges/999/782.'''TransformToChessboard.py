'''
You are given an n x n binary grid board. In each move, you can swap any two rows with each other, or any two columns with each other.

Return the minimum number of moves to transform the board into a chessboard board. If the task is impossible, return -1.

A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.

Example 1:

Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation: One potential sequence of moves is shown.
The first move swaps the first and second column.
The second move swaps the second and third row.

Example 2:

Input: board = [[0,1],[1,0]]
Output: 0
Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.

Example 3:

Input: board = [[1,0],[1,0]]
Output: -1
Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.

Constraints:

n == board.length
n == board[i].length
2 <= n <= 30
board[i][j] is either 0 or 1.
'''


from typing import List


class Solution:
  '''
  actually a tricky math problem ... the core of the solution is to understand
  that in order to be able to transform into a chessboard, all rows and columns
  must all match the same pattern (or the flipped pattern), and the number of 
  pattern rows/columns must equal or at most 1 off the flipped pattern rows/columns;
  this will eliminate all boards that can't be transformed. 

  for those that *can* be transformed, we only care about the 1st (or, in fact any) 
  row/col, as it represents the steps needed to transform the board; we only need
  to know the number of the rows/cols that are out of the place, and we can switch
  them with the ones out of the place and with the opposite color; the trick is that
  for board with odd/even total rows/cols, the approach is different -- the odd row/col
  counts has a definite solution ('0101010' or '1010101', depending the number of 1s),
  but the even row/col counts could have 2 solutions, and we take the one that needs the
  least amount of steps to get ('010101' or '101010').
  '''
  def movesToChessboard(self, board: List[List[int]]) -> int:
    n = len(board)
    
    p0, p1 = 0, 0
    c0, c1 = 0, 0
    
    # init check: 1st row and 1st col
    for i in range(n):
      if board[i][0] == 1:
        c0 += 1
        p0 |= 1 << i
        
      if board[0][i] == 1:
        c1 += 1
        p1 |= 1 << i
        
    if n % 2 == 0:
      if c0 != n // 2  or c1 != n // 2:
        # print('1', n, c0, c1)
        return -1
    else:
      if (2*c0+1 != n and 2*c0-1 != n) or (2*c1+1 != n and 2*c1-1 != n):
        # print('2', n, c0, c1)
        return -1
      
    pc0, pc1 = (1<<n)-p0-1, (1<<n)-p1-1
    # print("{0:b}".format(p0), "{0:b}".format(pc0))
    # print("{0:b}".format(p1), "{0:b}".format(pc1))
    
    # follow up checks: the rest rows and cols, with pattern matching as well
    for i in range(1, n):
      cc0, cc1 = 0, 0
      pp0, pp1 = 0, 0
      
      for j in range(n):
        if board[j][i] == 1:
          cc0 += 1
          pp0 |= 1 << j

        if board[i][j] == 1:
          cc1 += 1
          pp1 |= 1 << j
          
      if (cc0 != c0 and cc0+c0 != n) or (cc1 != c1 and cc1+c1 != n):
        # print('3', i)
        return -1
      
      if (pp0 != p0 and pp0 != pc0) or (pp1 != p1 and pp1 != pc1):
        # print('4', i)
        return -1
      
    # board can be transformed, get the min swap steps
    def count(src: int, lead: int) -> int:
      nonlocal n
      steps = 0
      
      for i in range(0, n, 2):
        if ((src>>i) & 1) != lead:
          steps += 1
      
      return steps
    
    if n % 2:
      a = count(p0, 1) if c0 > n//2 else count(p0, 0)
      b = count(p1, 1) if c1 > n//2 else count(p1, 0)
    else:
      a = min(count(p0, 0), count(p0, 1))
      b = min(count(p1, 0), count(p1, 1))
    
    # print(n, a, b)
    return a + b
      
    