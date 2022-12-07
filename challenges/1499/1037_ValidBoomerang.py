'''
1037. Valid Boomerang

Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false

Constraints:

points.length == 3
points[i].length == 2
0 <= xi, yi <= 100
'''

from typing import List
import math


class Solution:
  def isBoomerang(self, points: List[List[int]]) -> bool:
    x0, y0 = points[0]
    pt = set([(x0, y0)])
    diag = set()
    
    for x, y in points[1:]:
      if (x, y) in pt:
        return False
      
      if y == y0:
        d = math.inf
      else:
        d = (x-x0) / (y-y0)
        
      if d in diag:
        return False

      diag.add(d)
      pt.add((x, y))

    # print(pt)
    return True
  