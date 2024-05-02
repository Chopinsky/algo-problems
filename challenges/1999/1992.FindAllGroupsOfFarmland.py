'''
You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.

Example 1:

Input: land = [[1,0,0],[0,1,1],[0,1,1]]
Output: [[0,0,0,0],[1,1,2,2]]
Explanation:
The first group has a top left corner at land[0][0] and a bottom right corner at land[0][0].
The second group has a top left corner at land[1][1] and a bottom right corner at land[2][2].

Example 2:

Input: land = [[1,1],[1,1]]
Output: [[0,0,1,1]]
Explanation:
The first group has a top left corner at land[0][0] and a bottom right corner at land[1][1].

Example 3:

Input: land = [[0]]
Output: []
Explanation:
There are no groups of farmland.

Constraints:

m == land.length
n == land[i].length
1 <= m, n <= 300
land consists of only 0's and 1's.
Groups of farmland are rectangular in shape.
'''

from typing import List

class Solution:
  def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
    farm = set()
    m, n = len(land), len(land[0])
    ans = []
    
    def bfs(x: int, y: int):
      dim = [x, y, 0, 0]
      
      for x0 in range(x, m):
        if land[x0][y] == 0:
          break
          
        dim[2] = max(dim[2], x0)
        for y0 in range(y, n):
          if land[x0][y0] == 0:
            break
          
          dim[3] = max(dim[3], y0)
          farm.add((x0, y0))
          
      return dim
      
    for x in range(m):
      for y in range(n):
        if (x, y) in farm or land[x][y] == 0:
          continue
          
        ans.append(bfs(x, y))
        
    return ans
      
  def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
    jumps = {}
    lands = []
    m, n = len(land), len(land[0])
    
    def mark(i: int, j: int):
      b, r = i, j
      
      while b+1 < m and land[b+1][j]:
        b += 1
      
      while r+1 < n and land[i][r+1]:
        r += 1
        
      lands.append([i, j, b, r])
      
      for x in range(i, b+1):
        jumps[x, j] = r + 1
          
      return r + 1
    
    i, j = 0, 0
    
    while i < m:
      while j < n:
        # print(i, j)
        # the land is already marked, skip
        if (i, j) in jumps:
          j = jumps[i, j]
          continue

        # check the land
        if land[i][j]:
          j = mark(i, j)
        else:
          j += 1
        
      i += 1
      j = 0
      
    # print(jumps)
    return lands
  