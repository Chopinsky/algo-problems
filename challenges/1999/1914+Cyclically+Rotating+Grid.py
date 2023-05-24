'''
1914. Cyclically Rotating a Grid

You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:

A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:

Return the matrix after applying k cyclic rotations to it.

Example 1:

Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.
Example 2:
  
Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.
Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 50
Both m and n are even integers.
1 <= grid[i][j] <= 5000
1 <= k <= 10^9
'''

from typing import List


class Solution:
  def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    x0, y0 = 0, 0
    
    def rotate(x, y, m, n):
      cnt = 2*(m+n-2)
      shift = k % cnt
      if shift == 0:
        return
      
      x1, x2 = x, x+m-1
      y1, y2 = y, y+n-1
      tx, ty = x, y
      stack = [grid[x][y]]
      
      dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
      dx, dy = dirs.pop()
      td = None
      moves = 0
      
      while len(stack) < cnt:
        if x1 <= x+dx <= x2 and y1 <= y+dy <= y2:
          x += dx
          y += dy
          stack.append(grid[x][y])
          moves += 1
          
          if moves == shift:
            tx, ty = x, y
            td = [(0, -1), (-1, 0), (0, 1), (1, 0)] + dirs + [(dx, dy)]
            td = td[-5:]
          
        else:
          dx, dy = dirs.pop()
        
      # print(stack, (tx, ty), td)
      dx, dy = td.pop()
      idx = 0
      
      while idx < cnt:
        if x1 <= tx <= x2 and y1 <= ty <= y2:
          grid[tx][ty] = stack[idx]
          tx += dx
          ty += dy
          idx += 1
          
        else:
          tx -= dx
          ty -= dy
          dx, dy = td.pop()
          tx += dx
          ty += dy
    
    while m > 0 and n > 0:
      rotate(x0, y0, m, n)
      m -= 2
      n -= 2
      x0 += 1
      y0 += 1
      
    return grid
    