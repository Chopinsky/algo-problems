'''
You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

Example 1:

Input: board = ["E23","2X2","12S"]
Output: [7,1]
Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]
Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]

Constraints:

2 <= board.length == board[i].length <= 100
'''


from typing import List


class Solution:
  def pathsWithMaxScore(self, board: List[str]) -> List[int]:
    n = len(board)
    mod = 1_000_000_007
    stack, nxt = set([(n-1, n-1)]), set()
    
    path = [[[0, 0] for _ in range(n)] for _ in range(n)]
    path[n-1][n-1] = [0, 1]
    
    def update(x: int, y: int) -> bool:
      if board[x][y] == 'X':
        return False
      
      updated = False
      for dx, dy in [(1, 0), (0, 1), (1, 1)]:
        x0, y0 = x+dx, y+dy
        if x0 >= n or y0 >= n or board[x0][y0] == 'X' or path[x0][y0][1] == 0:
          continue

        point = path[x0][y0][0] + (0 if (x == 0 and y == 0) else int(board[x][y]))
        
        if point == path[x][y][0]:
          path[x][y][1] = (path[x][y][1] + path[x0][y0][1]) % mod
          updated = True

        elif point > path[x][y][0]:
          path[x][y][0] = point
          path[x][y][1] = path[x0][y0][1]
          updated = True

      return updated
    
    for p0 in range(2, n+1):
      updated = False

      for p1 in range(1, p0+1):
        # row to left
        x, y = n-p0, n-p1
        updated |= update(x, y)
          
        if p0 == p1:
          continue
        
        # column up
        updated |= update(y, x)

      if not updated:
        break

    # for r in path:
    #   print(r)
    
    return path[0][0]
  