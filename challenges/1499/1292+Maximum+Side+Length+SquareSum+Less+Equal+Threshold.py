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
  def maxSideLength(self, mat: List[List[int]], t: int) -> int:
    m = len(mat)
    n = len(mat[0])
    rows = [[0]*n for _ in range(m)]
    cols = [[0]*n for _ in range(m)]

    for x in range(m):
      for y in range(n):
        val = mat[x][y]
        rows[x][y] = val + (0 if x == 0 else rows[x-1][y])
        cols[x][y] = val + (0 if y == 0 else cols[x][y-1])

    def rval(x0: int, x1: int, y1: int) -> int:
      return rows[x1][y1] - (0 if x0 == 0 else rows[x0-1][y1])

    def cval(y0: int, x1: int, y1: int) -> int:
      return cols[x1][y1] - (0 if y0 == 0 else cols[x1][y0-1])

    def add(x0: int, y0: int, x1: int, y1: int) -> int:
      if x1 >= m or y1 >= n:
        return 0

      return rval(x0, x1, y1) + cval(y0, x1, y1) - mat[x1][y1]

    def find_square(x0: int, y0: int) -> int:
      x1, y1 = x0, y0
      vals = add(x0, y0, x1, y1)
      ln = 0

      while x1 < m and y1 < n and vals <= t:
        ln += 1
        x1 += 1
        y1 += 1
        vals += add(x0, y0, x1, y1)

      return ln

    max_ln = 0

    for x in range(m):
      for y in range(n):
        max_ln = max(max_ln, find_square(x, y))

    return max_ln

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
    