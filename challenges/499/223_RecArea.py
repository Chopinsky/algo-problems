'''
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Example 1:

Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45
Example 2:

Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16

Constraints:

-10^4 <= ax1 <= ax2 <= 10^4
-10^4 <= ay1 <= ay2 <= 10^4
-10^4 <= bx1 <= bx2 <= 10^4
-10^4 <= by1 <= by2 <= 10^4
'''


class Solution:
  def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    a = (ax2-ax1) * (ay2-ay1)
    b = (bx2-bx1) * (by2-by1)
    
    if by2 <= ay1 or by1 >= ay2 or bx2 <= ax1 or bx1 >= ax2:
      return a + b
    
    cx1, cx2 = max(ax1, bx1), min(ax2, bx2)
    cy1, cy2 = max(ay1, by1), min(ay2, by2)
    
    return a + b - abs(cx2-cx1) * abs(cy2-cy1)
    

  def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    a0 = (ax2-ax1) * (ay2-ay1)
    a1 = (bx2-bx1) * (by2-by1)
    
    x0, y0 = max(ax1, bx1), max(ay1, by1)
    x1, y1 = min(ax2, bx2), min(ay2, by2)
    
    if x0 <= x1 and y0 <= y1:
      a2 = (x1-x0) * (y1-y0)
    else:
      a2 = 0
      
    return a0 + a1 - a2
        