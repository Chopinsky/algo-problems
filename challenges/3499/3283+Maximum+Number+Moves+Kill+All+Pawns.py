'''
3283. Maximum Number of Moves to Kill All Pawns

There is a 50 x 50 chessboard with one knight and some pawns on it. You are given two integers kx and ky where (kx, ky) denotes the position of the knight, and a 2D array positions where positions[i] = [xi, yi] denotes the position of the pawns on the chessboard.

Alice and Bob play a turn-based game, where Alice goes first. In each player's turn:

The player selects a pawn that still exists on the board and captures it with the knight in the fewest possible moves. Note that the player can select any pawn, it might not be one that can be captured in the least number of moves.
In the process of capturing the selected pawn, the knight may pass other pawns without capturing them. Only the selected pawn can be captured in this turn.
Alice is trying to maximize the sum of the number of moves made by both players until there are no more pawns on the board, whereas Bob tries to minimize them.

Return the maximum total number of moves made during the game that Alice can achieve, assuming both players play optimally.

Note that in one move, a chess knight has eight possible positions it can move to, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

Example 1:

Input: kx = 1, ky = 1, positions = [[0,0]]

Output: 4

Explanation:

The knight takes 4 moves to reach the pawn at (0, 0).

Example 2:

Input: kx = 0, ky = 2, positions = [[1,1],[2,2],[3,3]]

Output: 8

Explanation:

Alice picks the pawn at (2, 2) and captures it in two moves: (0, 2) -> (1, 4) -> (2, 2).
Bob picks the pawn at (3, 3) and captures it in two moves: (2, 2) -> (4, 1) -> (3, 3).
Alice picks the pawn at (1, 1) and captures it in four moves: (3, 3) -> (4, 1) -> (2, 2) -> (0, 3) -> (1, 1).
Example 3:

Input: kx = 0, ky = 0, positions = [[1,2],[2,4]]

Output: 3

Explanation:

Alice picks the pawn at (2, 4) and captures it in two moves: (0, 0) -> (1, 2) -> (2, 4). Note that the pawn at (1, 2) is not captured.
Bob picks the pawn at (1, 2) and captures it in one move: (2, 4) -> (1, 2).

Constraints:

0 <= kx, ky <= 49
1 <= positions.length <= 15
positions[i].length == 2
0 <= positions[i][0], positions[i][1] <= 49
All positions[i] are unique.
The input is generated such that positions[i] != [kx, ky] for all 0 <= i < positions.length.
'''

from typing import List
from functools import lru_cache

class Solution:
  def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    src = (kx, ky)
    positions.append(src)
    dist = []
    n = len(positions)
    target = (1<<n) - 1
    dic = {(x, y): idx for idx, (x, y) in enumerate(positions)}
    
    def bfs(src):
      d = [0]*n
      curr = [src]
      nxt = []
      seen = set(curr)
      dist = 1
      cnt = n-1
      
      while curr and cnt > 0:
        for pos in curr:
          x0, y0 = pos
          for dx, dy in moves:
            x1, y1 = x0+dx, y0+dy
            if x1 < 0 or x1 >= 50 or y0 < 0 or y1 >= 50:
              continue
              
            if (x1, y1) in seen:
              continue
              
            seen.add((x1, y1))
            nxt.append((x1, y1))
            
            if (x1, y1) in dic:
              idx = dic[x1, y1]
              d[idx] = dist
              cnt -= 1
          
        curr, nxt = nxt, curr
        nxt.clear()
        dist += 1
        
      # print('dist:', src, d)
      return d
        
    for pos in positions:
      dist.append(bfs(tuple(pos)))
      
    def is_alice(mask: int):
      val = bin(mask)[2:]
      return (val.count('1') % 2) == 1
    
    @lru_cache(None)
    def dp(i: int, mask: int):
      if mask >= target:
        return 0
      
      base = -1
      for j in range(n-1):
        # already taken
        if ((1<<j) & mask) > 0:
          continue
          
        s = dist[i][j] + dp(j, mask|(1<<j))
        if base < 0:
          base = s
          continue
          
        if is_alice(mask):
          base = max(base, s)
        else:
          base = min(base, s)
        
      return base
      
    return dp(n-1, 1<<(n-1), True)
      