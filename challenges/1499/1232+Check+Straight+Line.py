'''
1232. Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
'''

from typing import List


class Solution:
  def checkStraightLine(self, coord: List[List[int]]) -> bool:
    n = len(coord)
    if n <= 2:
      return True
    
    coord.sort()
    x0, y0 = coord[0]
    x1, y1 = coord[1]
    
    if x0 == x1:
      return all(p[0] == x0 for p in coord)
    
    s0 = (y0-y1) / (x0-x1)
    
    for x1, y1 in coord[2:]:
      if x1 == x0:
        return False
      
      s1 = (y0-y1) / (x0-x1)
      if s1 != s0:
        return False
      
    return True
    