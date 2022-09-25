'''
417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5
'''

from typing import List
from heapq import heappop, heappush


class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    m, n = len(heights), len(heights[0])
    dp = [[0]*n for _ in range(m)]
    q = []
    ans = []
    
    def spread(q, base):
      seen = set([(x, y) for _, x, y in q])
      # print(q, base)
      
      while q:
        h0, x, y = heappop(q)
        if dp[x][y] == 3:
          ans.append((x, y))
          
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or (x0, y0) in seen or heights[x0][y0] < h0:
            continue
            
          seen.add((x0, y0))
          dp[x0][y0] |= base
          heappush(q, (heights[x0][y0], x0, y0))
    
    for i in range(m):
      if i == 0:
        for j in range(n):
          dp[i][j] |= 1
          heappush(q, (heights[i][j], i, j))
          
      else:
        dp[i][0] |= 1
        heappush(q, (heights[i][0], i, 0))
        
    spread(q, 1)
    q.clear()
    
    for i in range(m):
      if i == m-1:
        for j in range(n):
          dp[i][j] |= 2
          heappush(q, (heights[i][j], i, j))
          
      else:
        dp[i][n-1] |= 2
        heappush(q, (heights[i][n-1], i, n-1))
        
    spread(q, 2)
    # print(dp)
    # print(ans)
    
    return ans
    