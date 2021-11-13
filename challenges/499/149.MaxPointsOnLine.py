'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:

1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.
'''


from typing import List
from collections import defaultdict
import math


class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
    slopes = defaultdict(set)
    top = 1
    
    for i in range(1, len(points)):
      for j in range(i):
        x0, y0 = points[i]
        x1, y1 = points[j]
        
        if x1 == x0:
          s = math.inf
          b = x0
        else:
          s = (y1-y0) / (x1-x0)
          b = y0 - s*x0
          
        slopes[s, b].add((x0, y0))
        slopes[s, b].add((x1, y1))
        size = len(slopes[s, b])
          
        if size > top:
          top = size
          
    # print(slopes)
    return top
  