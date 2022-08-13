'''
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false

Constraints:

rec1.length == 4
rec2.length == 4
-10^9 <= rec1[i], rec2[i] <= 10^9
rec1 and rec2 represent a valid rectangle with a non-zero area.
'''

from typing import List


class Solution:
  def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    x0, y0, x1, y1 = rec1
    x2, y2, x3, y3 = rec2
    
    if x2 <= x0 < x3 and y2 <= y0 < y3:
      return True
    
    if x2 < x1 <= x3 and y2 < y1 <= y3:
      return True
    
    if x0 <= x2 < x1 and y0 <= y2 < y1:
      return True
    
    if x0 < x3 <= x1 and y0 < y3 <= y1:
      return True
    
    a0, b0 = max(x0, x2), max(y0, y2)
    a1, b1 = min(x1, x3), min(y1, y3)
    
    return a0 < a1 and b0 < b1
    