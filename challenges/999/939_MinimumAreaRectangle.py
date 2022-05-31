'''
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

Example 1:

Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 4 * 10^4
All the given points are unique.
'''

from typing import List
import math


class Solution:
  def minAreaRect(self, points: List[List[int]]) -> int:
    cand = set((x, y) for x, y in points)
    n = len(points)
    area = math.inf
    
    for i in range(n-1):
      for j in range(i+1, n):
        x0, y0 = points[i]
        x1, y1 = points[j]
        
        if x0 == x1 or y0 == y1:
          continue
          
        if (x0, y1) in cand and (x1, y0) in cand:
          area = min(area, abs(x1-x0) * abs(y1-y0))
    
    return 0 if area == math.inf else area
  