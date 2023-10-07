'''
1401. Circle and Rectangle Overlapping

You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.

Example 1:

Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).
Example 2:

Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false
Example 3:

Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true

Constraints:

1 <= radius <= 2000
-10^4 <= xCenter, yCenter <= 10^4
-10^4 <= x1 < x2 <= 10^4
-10^4 <= y1 < y2 <= 10^4
'''

from math import sqrt


class Solution:
  def checkOverlap(self, radius: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    if x1 <= xc <= x2 and y1 <= yc <= y2:
      return True
    
    if x1 <= xc <= x2:
      return abs(y1-yc) <= radius or abs(y2-yc) <= radius
    
    if y1 <= yc <= y2:
      return abs(x1-xc) <= radius or abs(x2-xc) <= radius
    
    def get_dist(x, y):
      return sqrt((x-xc)**2 + (y-yc)**2)
    
    d0 = get_dist(x1, y1)
    d1 = get_dist(x1, y2)
    d2 = get_dist(x2, y1)
    d3 = get_dist(x2, y2)
    
    return d0 <= radius or d1 <= radius or d2 <= radius or d3 <= radius
        