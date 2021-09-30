'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20

'''


class Solution:
  def generateMatrix(self, n: int) -> List[List[int]]:
    m = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    x, y = 0, 0
    d = 0
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    while num <= n*n:
      m[x][y] = num
      num += 1
        
      x0, y0 = x+dirs[d][0], y+dirs[d][1]
      if x0 < 0 or x0 >= n or y0 < 0 or y0 >= n or m[x0][y0] != 0:
        d += 1
        d = d % 4
        x0, y0 = x+dirs[d][0], y+dirs[d][1]
        
      x, y = x0, y0
    
    return m
    
