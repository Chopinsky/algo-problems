'''
3197. Find the Minimum Area to Cover All Ones II

You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.

Return the minimum possible sum of the area of these rectangles.

Note that the rectangles are allowed to touch.

Example 1:

Input: grid = [[1,0,1],[1,1,1]]

Output: 5

Explanation:

The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
The 1 at (1, 1) is covered by a rectangle of area 1.
Example 2:

Input: grid = [[1,0,1,0],[0,1,0,1]]

Output: 5

Explanation:

The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3.
The 1 at (1, 1) is covered by a rectangle of area 1.
The 1 at (1, 3) is covered by a rectangle of area 1.

Constraints:

1 <= grid.length, grid[i].length <= 30
grid[i][j] is either 0 or 1.
The input is generated such that there are at least three 1's in grid.

Test cases:

[[0,0,0,0,0],[0,0,0,0,0],[1,1,0,1,1],[0,0,0,0,0],[0,1,1,1,1]]
[[1,0,1],[1,1,1]]
[[1,0,1,0],[0,1,0,1]]
[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,1,0,0],[0,0,1,1,0,0,1,1,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,0,0,1,0,0,1,1,1,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,1,1,0,0,1,1,0,0]]
'''

from typing import List
from functools import lru_cache

class Solution:
  '''
  this is a geometry problem: we can always divide the grid into 3 regions (and there are 6 ways of dividing
  the regions), and we can calc the area of the smallest rectangle that can cover all 1s in the region:
  1) ||
  2) |-
  3) ___
      |
  4) __
     __
     __
  5) __|
       |
  6) _|_
     ___
  '''
  def minimumSum(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    debug = False
    
    @lru_cache(None)
    def area(x0: int, y0: int, x1: int, y1: int) -> int:
      tl = None
      br = None
      # print('area:', (x0, y0), (x1, y1))
      
      for x in range(x0, x1+1):
        for y in range(y0, y1+1):
          if grid[x][y] == 0:
            continue
            
          if not tl:
            tl = [x, y]
          else:
            tl[0] = min(tl[0], x)
            tl[1] = min(tl[1], y)
            
          if not br:
            br = [x, y]
          else:
            br[0] = max(br[0], x)
            br[1] = max(br[1], y)
            
      # print('area:', (x0, y0), (x1, y1), tl, br)
      if not tl or not br:
        return 0
      
      return (br[0]-tl[0]+1) * (br[1]-tl[1]+1)
    
    def left_mid_right():
      max_area = m*n
      
      for y0 in range(0, n-2):
        a0 = area(0, 0, m-1, y0)
        if a0 == 0:
          continue
        
        for y1 in range(y0+1, n-1):
          a1 = area(0, y0+1, m-1, y1)
          if a1 == 0:
            continue
            
          a2 = area(0, y1+1, m-1, n-1)
          if a2 == 0:
            break
            
          max_area = min(max_area, a0+a1+a2)
          if debug:
            print('lmr:', (y0, y1), (a0, a1, a2))
      
      return max_area
    
    def left_top_bottom():
      max_area = m*n
      
      for y0 in range(0, n-1):
        a0 = area(0, 0, m-1, y0)
        if a0 == 0:
          continue
        
        for x0 in range(m-1):
          a1 = area(0, y0+1, x0, n-1)
          if a1 == 0:
            continue
            
          a2 = area(x0+1, y0+1, m-1, n-1)
          if a2 == 0:
            break
            
          max_area = min(max_area, a0+a1+a2)
          if debug:
            print('ltb:', (x0, y0), (a0, a1, a2))
      
      return max_area
      
    def top_left_right():
      max_area = m*n
      
      for x0 in range(m-1):
        a0 = area(0, 0, x0, n-1)
        if a0 == 0:
          continue
        
        for y0 in range(n-1):
          a1 = area(x0+1, 0, m-1, y0)
          if a1 == 0:
            continue
            
          a2 = area(x0+1, y0+1, m-1, n-1)
          if a2 == 0:
            break
            
          max_area = min(max_area, a0+a1+a2)
          if debug:
            print('tlr:', (x0, y0), (a0, a1, a2))
      
      return max_area
    
    def top_mid_bottom():
      max_area = m*n
      
      for x0 in range(m-2):
        a0 = area(0, 0, x0, n-1)
        if a0 == 0:
          continue
        
        for x1 in range(x0+1, m-1):
          a1 = area(x0+1, 0, x1, n-1)
          if a1 == 0:
            continue
            
          a2 = area(x1+1, 0, m-1, n-1)
          if a2 == 0:
            break
            
          max_area = min(max_area, a0+a1+a2)
          if debug:
            print('tmb:', (x0, x1), (a0, a1, a2))
      
      return max_area
    
    def top_bottom_right():
      max_area = m*n
      
      for y0 in range(1, n):
        a0 = area(0, y0, m-1, n-1)
        if a0 == 0:
          break
        
        for x0 in range(m-1):
          a1 = area(0, 0, x0, y0-1)
          if a1 == 0:
            continue
            
          a2 = area(x0+1, 0, m-1, y0-1)
          if a2 == 0:
            break
            
          max_area = min(max_area, a0+a1+a2)
          if debug:
            print('tbr:', (x0, y0), (a0, a1, a2))
      
      return max_area
      
    def left_right_bottom():
      max_area = m*n
      
      for x0 in range(1, m):
        a0 = area(x0, 0, m-1, n-1)
        if a0 == 0:
          break
        
        for y0 in range(n-1):
          a1 = area(0, 0, x0-1, y0)
          if a1 == 0:
            continue
            
          a2 = area(0, y0+1, x0-1, n-1)
          if a2 == 0:
            break
            
          max_area = min(max_area, a0+a1+a2)
          if debug:
            print('lrb:', (x0, y0), (a0, a1, a2))
            
      return max_area
      
    return min(
      left_mid_right(),
      left_top_bottom(),
      top_left_right(),
      top_mid_bottom(),
      top_bottom_right(),
      left_right_bottom(),
    )
    