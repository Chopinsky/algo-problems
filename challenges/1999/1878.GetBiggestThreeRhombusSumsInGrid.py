'''
You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending 
order. If there are less than three distinct values, return all of them.

Example 1:


Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211

Example 2:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)

Example 3:

Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 10^5
'''


from typing import List
from heapq import heappush, heappushpop


class Solution:
  def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
    m, n = len(grid), len(grid[0])    
    max_heap = []
    
    def other_half(x1: int, x2: int, y: int) -> int:
      total = 0
      while x1 != x2:
        total += grid[x1][y] + grid[x2][y]
        x1 += 1
        x2 -= 1
        y += 1
      
      return total + grid[x1][y]
    
    def update(val: int):
      if val in max_heap:
        return 
      
      if len(max_heap) < 3:
        heappush(max_heap, val)
      else:
        heappushpop(max_heap, val)
        
    for i in range(m):
      for j in range(n):
        left_half = grid[i][j]
        update(left_half)
        bound = min(i, m-1-i)
        
        for k in range(1, bound+1):
          if j+2*k >= n:
            break
            
          left_half += grid[i-k][j+k] + grid[i+k][j+k]
          block = left_half + other_half(i-k+1, i+k-1, j+k+1)
          # print(i, j, k, left_half, block)
          update(block)
          
    # print(max_heap, base)
    
    return sorted([val for val in max_heap], reverse=True)
  