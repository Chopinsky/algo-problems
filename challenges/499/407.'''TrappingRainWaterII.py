'''
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small pounds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:

Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 10^4
'''


from typing import List
from heapq import heappush, heappop


class Solution:
  def trapRainWater(self, mat: List[List[int]]) -> int:
    if not mat or not mat[0]:
      return 0
    
    h, w = len(mat), len(mat[0])
    if h == 1 or w == 1:
      return 0
    
    count = 0
    seen = [[0] * w for _ in range(h)]
    q = []
            
    # add all border points to the queue, and we will start from
    # the smallest one inwards until visiting all points
    for j in range(w):
      heappush(q, (mat[0][j], 0, j))
      heappush(q, (mat[h-1][j], h-1, j))
      seen[0][j] = 1
      seen[h-1][j] = 1
      
    for i in range(1, h-1):
      heappush(q, (mat[i][0], i, 0))
      heappush(q, (mat[i][w-1], i, w-1))
      seen[i][0] = 1
      seen[i][w-1] = 1
      
    # print(q)
    
    while q:
      height, i, j = heappop(q)
      for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        # only check unseen points
        if 0 <= x < h and 0 <= y < w and not seen[x][y]:
          if height > mat[x][y]:
            count += height - mat[x][y]

          # add the point to the min-queue, use the height that
          # trapps the water, i.e. the larger one
          heappush(q, (max(mat[x][y], height), x, y))
          seen[x][y] = 1
    
    return count
    