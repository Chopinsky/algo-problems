'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:

1 <= points.length <= 1000
-10^6 <= xi, yi <= 10^6
All pairs (xi, yi) are distinct.
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    n = len(points)
    arr = list(range(n))
    
    def find(x: int) -> int:
      while arr[x] != x:
        x = arr[x]
        
      return x
        
    def dist(i: int, j: int) -> int:
      x0, y0 = points[i]
      x1, y1 = points[j]
      
      return abs(x0-x1) + abs(y0-y1)
    
    d = []
    for i in range(n-1):
      for j in range(i+1, n):
        d.append((dist(i, j), i, j))
        
    d.sort()
    ans, cnt = 0, 0
    # print(d)
    
    for d0, i, j in d:
      ri, rj = find(i), find(j)
      if ri == rj:
        continue
        
      ans += d0
      cnt += 1
      
      if ri <= rj:
        arr[rj] = ri
      else:
        arr[ri] = rj
        
      if cnt == n-1:
        break
    
    return ans
        
        
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    n = len(points)
    cand = []
    groups = [i for i in range(n)]
    score, edges = 0, 0
    
    def find(x: int) -> int:
      while groups[x] != x:
        x = groups[x]
        
      return x
    
    def union(x: int, y: int):
      x0, y0 = find(x), find(y)
      if x0 < y0:
        groups[y0] = x0
      else:
        groups[x0] = y0
    
    for i in range(n-1):
      x0, y0 = points[i]
      for j in range(i+1, n):
        x1, y1 = points[j]
        heappush(cand, (abs(x0-x1)+abs(y0-y1), i, j))
        
    # print(cand)
    while cand and edges < n-1:
      s, i, j = heappop(cand)
      idx, jdx = find(i), find(j)
      # print(i, idx, j, jdx, s)
      
      if idx == jdx:
        continue
      
      union(idx, jdx)
      score += s
      edges += 1
      
    return score
      