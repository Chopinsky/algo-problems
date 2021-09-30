'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''

class Solution:
  def longestIncreasingPath(self, mat: List[List[int]]) -> int:
    h, w = len(mat), len(mat[0])
    if h == 1 and w == 1:
      return 1

    points = []
    for i in range(h):
      for j in range(w):
        points.append((mat[i][j], i, j))

    points = sorted(points, key=itemgetter(0), reverse=True)
    # print(points)

    dp = [[1 for _ in range(w)] for _ in range(h)]
    dirs = [-1, 0, 1, 0, -1]
    ans = 1

    for _, p in enumerate(points):
      # print(p, type(p))
      x, y = p[1], p[2]

      for i in range(4):
        x0, y0 = x+dirs[i], y+dirs[i+1]
        if x0 < 0 or x0 >= h or y0 < 0 or y0 >= w:
          continue

        if mat[x0][y0] <= mat[x][y]:
          continue

        # print(x, y, x0, y0)
        dp[x][y] = max(dp[x][y], 1+dp[x0][y0])

        if dp[x][y] > ans:
          ans = dp[x][y]

    # print(dp)
    return ans
