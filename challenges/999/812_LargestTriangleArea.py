'''
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
 

Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
'''

from itertools import combinations
from typing import List


class Solution:
  def largestTriangleArea(self, points: List[List[int]]) -> float:
    area = 0
    for p in combinations(points, 3):
      [ax, ay], [bx, by], [cx, cy] = p
      area = max(area, abs(ax*by+bx*cy+cx*ay-ay*bx-by*cx-cy*ax) / 2.0)
      
    return area
      
    