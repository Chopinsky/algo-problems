'''
3256. Maximum Value Sum by Placing Three Rooks I
'''

from typing import List
from heapq import heappush, heappushpop
import math

class Solution:
  def maximumValueSum(self, board: List[List[int]]) -> int:
    rows = []
    cand = []
    m, n = len(board), len(board[0])
    
    for x in range(m):
      row = []
      for y in range(n):
        point = (board[x][y], x, y)
        cand.append(point)
        
        if len(row) < 3:
          heappush(row, point)
        else:
          heappushpop(row, point)
      
      rows.append(row)
      
    # print(rows, cand)
    cand.sort()
    score = -math.inf
    
    def get_points(x: int, y: int) -> List:
      points = []
      idx = len(cand)-1
      
      while idx >= 0 and len(points) < 4:
        _, x0, y0 = cand[idx]
        if x0 != x and y0 != y:
          points.append(cand[idx])
        
        idx -= 1
      
      return points
    
    def get_score(point: List) -> int:
      result = -math.inf
      s, x, y = point
      points = get_points(x, y)
      n = len(points)
      # print('score:', point, points)
      
      for i in range(n-1):
        s0, x0, y0 = points[i]
        if x0 == x or y0 == y:
          continue
        
        for j in range(i+1, n):
          s1, x1, y1 = points[j]
          if x1 == x0 or x1 == x:
            continue
            
          if y1 == y0 or y1 == y:
            continue
            
          result = max(result, s+s0+s1)
      
      return result
    
    for row in rows:
      for point in row:
        score = max(score, get_score(point))
    
    return score
        