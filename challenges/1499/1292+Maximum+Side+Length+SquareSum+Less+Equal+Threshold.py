'''
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

Example 1:

Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 300
0 <= mat[i][j] <= 10^4
0 <= threshold <= 10^5
'''

from typing import List


class Solution:
  def maxSideLength(self, mat: List[List[int]], th: int) -> int:
    m, n = len(mat), len(mat[0])
    if m == 1:
      return 1 if any(mat[0][j] <= th for j in range(n)) else 0
    
    if n == 1:
      return 1 if any(mat[i][0] <= th for i in range(m)) else 0
    
    rec = [[0 for _ in range(n)] for _ in range(m)]
    cols = [0] * n
    # print('size:', m, n)
    
    def get_sq_sum(x: int, y: int, ln: int) -> bool:
      if ln <= 0 or rec[x][y] <= th:
        return True
      
      x0, y0 = x-ln+1, y-ln+1
      if x0 < 0 or y0 < 0:
        return False
      
      tl = 0 if (x0 == 0 or y0 == 0) else rec[x0-1][y0-1]
      tr = 0 if x0 == 0 else rec[x0-1][y]
      bl = 0 if y0 == 0 else rec[x][y0-1]
      br = rec[x][y]
      
      return (br-bl-tr+tl) <= th

    def check_side(ln: int) -> bool:
      if ln <= 0:
        return True
      
      if ln > m or ln > n:
        return False
      
      for x in range(ln-1, m):
        for y in range(ln-1, n):
          if get_sq_sum(x, y, ln):
            return True
          
      return False
      
    for x in range(m):
      rows = 0
      for y in range(n):
        cols[y] += mat[x][y]
        rows += mat[x][y]
        
        rec[x][y] = (rec[x-1][y-1] if (x > 0 and y > 0) else 0) + cols[y] + rows - mat[x][y]
    
    l, r = 0, 1+min(m, n)
    size = 0
    
    while l <= r:
      mid = (l + r) // 2
      # print('check:', (l, r), mid)
      
      if check_side(mid):
        size = max(size, mid)
        l = mid + 1
      else:
        r = mid - 1
        
    return size
    
  def maxSideLength0(self, mat: List[List[int]], th: int) -> int:
    m, n = len(mat), len(mat[0])
    if m == 1:
      return 1 if any(mat[0][j] <= th for j in range(n)) else 0
    
    if n == 1:
      return 1 if any(mat[i][0] <= th for i in range(m)) else 0
    
    rec = [[0 for _ in range(n)] for _ in range(m)]
    cols = [0] * n
    size = 0
    # print('size:', m, n)
    
    def find_sq(x: int, y: int) -> int:
      if mat[x][y] > th:
        return 0
      
      x0, y0 = x, y
      sq_sum = 0
      side = 0
      
      while x0 >= 0 and y0 >= 0 and sq_sum <= th:
        tl = 0 if x0 == 0 or y0 == 0 else rec[x0-1][y0-1]
        tr = 0 if x0 == 0 else rec[x0-1][y]
        bl = 0 if y0 == 0 else rec[x][y0-1]
        br = rec[x][y]
        
        sq_sum = br - bl - tr + tl
        if sq_sum <= th:
          side = x-x0+1
          
        x0 -= 1
        y0 -= 1
      
      return side
    
    for x in range(m):
      rows = 0
      for y in range(n):
        cols[y] += mat[x][y]
        rows += mat[x][y]
        
        rec[x][y] = (rec[x-1][y-1] if (x > 0 and y > 0) else 0) + cols[y] + rows - mat[x][y]
        
        if rec[x][y] <= th:
          # print('full', (x, y))
          size = max(size, 1+min(x, y))
        else:
          size = max(size, find_sq(x, y))

    return size
  