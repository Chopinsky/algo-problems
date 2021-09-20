'''
You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

Example 1:

Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.

Example 2:

Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.

Constraints:

2 <= points.length <= 10^5
points[i].length == 2
-10^8 <= xi, yi <= 10^8
0 <= k <= 2 * 10^8
xi < xj for all 1 <= i < j <= points.length
xi form a strictly increasing sequence.
'''


from typing import List
from collections import deque
from heapq import heappop, heappush


class Solution:
  def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
    q = deque([])
    ans = None
    # print(points)
    
    for x, y in points:
      # pop all points that no longer fit into the window
      while q and x-q[0][1] > k:
        q.popleft()
        
      # sum x+y and diff y-x
      s = y+x
      d = y-x
      
      # calculate the max value based on the current point
      # (x, y), the eq is essentially: 
      #     y + x + max([y0-x0 for (x0, y0) in allowed window])
      # and max(y0-x0) is maintained by `q`
      if q:
        if ans == None:
          ans = s + q[0][0]
        else:
          ans = max(ans, s + q[0][0])
          
      # maintain the mono-decrease queue, such that the
      # q[0] will be the point prior to the next examined
      # point and with the largest `y-x` value
      while q and d > q[-1][0]:
        q.pop()
        
      # add the current point to the queue, part of the 
      # mono-queue procedure
      q.append((d, x))
    
    return ans
  
  
  def findMaxValueOfEquation0(self, points: List[List[int]], k: int) -> int:
    minus = []
    xvals = sorted(set([i for i, _ in points]), reverse=True)
    # print(xvals)
    
    idx = 0
    n = len(points)
    ans = None
    
    while xvals and idx < len(points):
      x = xvals.pop()
        
      # remove past points
      while minus and minus[0][1] < x:
        heappop(minus)
      
      # add next points
      while idx < n and points[idx][0] - x <= k:
        x0, y0 = points[idx]
        if minus:
          if ans == None:
            ans = x0 + y0 - minus[0][0]
          else:
            ans = max(ans, x0 + y0 - minus[0][0])
        
        heappush(minus, (x0-y0, x0))
        idx += 1
        
      # print(x, minus, ans)
    
    return ans
  