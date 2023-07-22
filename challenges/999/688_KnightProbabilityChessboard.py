'''
688. Knight Probability in Chessboard

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.

Example 1:

Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
Example 2:

Input: n = 1, k = 0, row = 0, column = 0
Output: 1.00000

Constraints:

1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n - 1
'''

from collections import defaultdict


class Solution:
  def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    prob = 1
    if k == 0:
      return prob
    
    curr, nxt = defaultdict(int), defaultdict(int)
    curr[row, column] = 1
    delta = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        
    while k > 0 and prob > 0:
      oc, ic = 0, 0
      
      for (x, y), cnt in curr.items():
        # print((x, y), cnt)
        for dx, dy in delta:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= n or y0 < 0 or y0 >= n:
            oc += cnt
          else:
            ic += cnt
            nxt[x0, y0] += cnt
            
      total = oc+ic
      if total == 0:
        prob = 0
      else:
        prob *= ic / total
      
      curr, nxt = nxt, curr
      nxt.clear()
      k -= 1
    
    return prob
        

  def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    if k == 0:
      return 1
    
    moves = [(-1, 2), (1, 2), (-2, 1), (2, 1), (-2, -1), (2, -1), (-1, -2), (1, -2)]
    curr, nxt = {(row, column): 1}, {}
    p0 = 1
    
    while k > 0 and p0 > 0:
      out_cnt = 0
      in_cnt = 0
      
      for x0, y0 in curr:
        for dx, dy in moves:
          x1, y1 = x0+dx, y0+dy
          if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n:
            out_cnt += curr[x0, y0]
          else:
            nxt[x1, y1] = nxt.get((x1, y1), 0) + curr[x0, y0]
            in_cnt += curr[x0, y0]

      curr, nxt = nxt, curr
      nxt.clear()
      # print(in_cnt, out_cnt, curr, p0)
      
      p0 *= in_cnt / (in_cnt + out_cnt)
      k -= 1
    
    return p0
    