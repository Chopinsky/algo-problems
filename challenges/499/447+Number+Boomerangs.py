'''
447. Number of Boomerangs

You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

Example 1:

Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: 2
Example 3:

Input: points = [[1,1]]
Output: 0

Constraints:

n == points.length
1 <= n <= 500
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.
'''

from typing import List
from collections import defaultdict
from functools import lru_cache

class Solution:
  def numberOfBoomerangs(self, points: List[List[int]]) -> int:
    total, n = 0, len(points)
    counter = defaultdict(int)
    
    @lru_cache(None)
    def dist(i: int, j: int):
      x0, y0 = points[i]
      x1, y1 = points[j]
      
      return abs(x0-x1)**2 + abs(y0-y1)**2
    
    def count(i: int):
      c = 0
      counter.clear()
      
      for j in range(n):
        if i == j:
          continue
        
        d = dist(min(i, j), max(i, j))
        counter[d] += 1
      
      # print(points[i], counter)
      for c0 in counter.values():
        if c0 < 2:
          continue
          
        c += c0*(c0-1)
      
      return c
    
    for i in range(n):
      total += count(i)
    
    return total
        