'''
3235. Check if the Rectangle Corner Is Reachable

You are given two positive integers X and Y, and a 2D array circles, where circles[i] = [xi, yi, ri] denotes a circle with center at (xi, yi) and radius ri.

There is a rectangle in the coordinate plane with its bottom left corner at the origin and top right corner at the coordinate (X, Y). You need to check whether there is a path from the bottom left corner to the top right corner such that the entire path lies inside the rectangle, does not touch or lie inside any circle, and touches the rectangle only at the two corners.

Return true if such a path exists, and false otherwise.

Example 1:

Input: X = 3, Y = 4, circles = [[2,1,1]]

Output: true

Explanation:

The black curve shows a possible path between (0, 0) and (3, 4).

Example 2:

Input: X = 3, Y = 3, circles = [[1,1,2]]

Output: false

Explanation:


No path exists from (0, 0) to (3, 3).

Example 3:

Input: X = 3, Y = 3, circles = [[2,1,1],[1,2,1]]

Output: false

Explanation:

No path exists from (0, 0) to (3, 3).

Constraints:

3 <= X, Y <= 10^9
1 <= circles.length <= 1000
circles[i].length == 3
1 <= xi, yi, ri <= 10^9

Test cases:

6
8
[[5,4,8],[2,1,7]]
3
4
[[2,1,1]]
3
3
[[1,1,2]]
3
3
[[2,1,1],[1,2,1]]
'''

from typing import List
from math import sqrt

class Solution:
  def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
    n = len(circles)
    groups = [i for i in range(n)]

    def find(x: int) -> int:
      while groups[x] != x:
        x = groups[x]
        
      return x
    
    def union(x: int, y: int):
      gx = find(x)
      gy = find(y)
      
      if gx <= gy:
        groups[gy] = gx
      else:
        groups[gx] = gy
      
    def intersect(i: int, j: int) -> bool:
      x0, y0, r0 = circles[i]
      x1, y1, r1 = circles[j]

      dist = sqrt((x0-x1)**2 + (y0-y1)**2)
      
      return dist <= r0+r1

    def contains(i: int, x: int, y: int) -> bool:
      x0, y0, r = circles[i]
      dist = sqrt((x-x0)**2 + (y-y0)**2)
      return dist <= r
      
    def verify(dim: List[int]) -> bool:
      x0, x1, y0, y1 = dim
      
      # -- 
      if x0 <= 0 and x1 >= X:
        return True
      
      # |
      if y0 <= 0 and y1 >= Y:
        return True
      
      # -|
      if (x0 <= 0 < x1) and (y0 <= 0 < y1):
        return True
      
      # |-
      if (x0 < X <= x1) and (y0 < Y <= y1):
        return True
      
      return False
    
    marked = set()
    
    for i in range(1, n):
      c0 = contains(i, 0, 0) 
      c1 = contains(i, X, Y)
      
      if c0 and c1:
        marked.add(i)
        continue
      
      if c0 or c1:
        return False
      
      for j in range(i):
        if j in marked:
          continue
          
        if intersect(i, j):
          union(i, j)

    dim = {}
    for i in range(n):
      gn = find(i)
      x, y, r = circles[i]
      x0, x1 = x-r, x+r
      y0, y1 = y-r, y+r

      if gn not in dim:
        dim[gn] = [x0, x1, y0, y1]
      else:
        dim[gn][0] = min(dim[gn][0], x0)
        dim[gn][1] = max(dim[gn][1], x1)
        dim[gn][2] = min(dim[gn][2], y0)
        dim[gn][3] = max(dim[gn][3], y1)
      
    # print(dim)
    for d in dim.values():
      if verify(d):
        return False
    
    return True
        