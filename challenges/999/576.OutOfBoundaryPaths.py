'''
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent four cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:

Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow <= m
0 <= startColumn <= n
'''

from collections import defaultdict

class Solution:
  def findPaths(self, m: int, n: int, maxMove: int, sr: int, sc: int) -> int:
    moves = defaultdict(int)
    moves[(sr, sc)] = 1

    nextMoves = defaultdict(int)
    dirs = [-1, 0, 1, 0, -1]
    count = 0
    
    while maxMove > 0:
      for (x, y), move in moves.items():
        for i in range(4):
          x0, y0 = x+dirs[i], y+dirs[i+1]
          
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
            count += move
            continue
            
          nextMoves[(x0, y0)] += move
      
      moves, nextMoves = nextMoves, moves
      nextMoves.clear()
      maxMove -= 1
      
      # print(count, points, moves)
    
    return count % (10**9+7)
    