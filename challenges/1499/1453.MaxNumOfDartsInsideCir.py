'''
You have a very large square wall and a circular dartboard placed on the wall. You have been challenged to throw darts into the board blindfolded. Darts thrown at the wall are represented as an array of points on a 2D plane. 

Return the maximum number of points that are within or lie on any circular dartboard of radius r.

 

Example 1:

Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all points.

Example 2:

Input: points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
Output: 5
Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).

Example 3:

Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
Output: 1

Example 4:

Input: points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
Output: 4

Constraints:

1 <= points.length <= 100
points[i].length == 2
-10^4 <= points[i][0], points[i][1] <= 10^4
1 <= r <= 5000
'''


from typing import List


class Solution:
  def numPoints(self, points: List[List[int]], r: int) -> int:
    # points.sort()
    
    ln = len(points)
    res = 1
      
    for i in range(ln):
      for j in range(i+1, ln):
        x1, y1 = points[i]
        x2, y2 = points[j]
        
        # d == a**2, a is the half length of the line between point i, j
        d = ((x1-x2)**2 + (y1-y2)**2) / 4.0   
        if d > r*r:
          continue
          
        # find circle center
        x0 = (x1+x2) / 2.0 + (y2-y1) * (r*r-d)**0.5 / (4*d)**0.5
        y0 = (y1+y2) / 2.0 - (x2-x1) * (r*r-d)**0.5 / (4*d)**0.5
        base = r*r + 0.00001
        count = 2
        
        # count all points (except the 2 used) to the circle center
        for k in range(ln):
          if k == i or k == j:
            continue
            
          x, y = points[k]
          if (x-x0)**2 + (y-y0)**2 <= base:
            count += 1
        
        res = max(res, count)
          
    return res
  