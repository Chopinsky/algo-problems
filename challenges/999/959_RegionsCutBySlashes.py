from binhex import LINELEN
'''
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

Example 1:


Input: grid = [" /","/ "]
Output: 2
Example 2:


Input: grid = [" /","  "]
Output: 1
Example 3:


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.

Constraints:

n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.
'''


from typing import List

class Solution:
  def regionsBySlashes(self, grid: List[str]) -> int:
    n = len(grid)
    g = [i for i in range(4*n*n)]
    
    def find(x):
      while g[x] != x:
        x = g[x]
        
      return x
    
    def union(x, y):
      r0, r1 = find(x), find(y)
      if r0 <= r1:
        g[r1] = r0
      else:
        g[r0] = r1
        
    def key(i, j, k):
      return 4*(i*n + j) + k
        
    for i in range(n):
      for j in range(n):
        ch = grid[i][j]
        k0 = key(i, j, 0)
        k1 = key(i, j, 1)        
        k2 = key(i, j, 2)
        k3 = key(i, j, 3)
        
        if ch == '/' or ch == ' ':
          union(k0, k3)
          union(k1, k2)
          
        if ch == '\\' or ch == ' ':
          union(k0, k1)
          union(k2, k3)

        if i > 0:
          ku = key(i-1, j, 2)
          union(k0, ku)
            
        if j > 0:
          kl = key(i, j-1, 1)
          union(k3, kl)

        if j < n-1:
          kr = key(i, j+1, 3)
          union(k1, kr)

        if i < n-1:
          kd = key(i+1, j, 0)
          union(k2, kd)
          
    uniq_groups = set()
    # print(g)

    for i in range(len(g)):
      uniq_groups.add(find(i))
    
    return len(uniq_groups)
    