'''
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:

The path starts from the upper left cell (0, 0).
The path ends at the bottom-right cell (m - 1, n - 1).
The path only ever moves down or right.
The resulting parentheses string formed by the path is valid.
Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.

Example 1:

Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.
Example 2:

Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is either '(' or ')'.
'''

from typing import List


class Solution:
  def hasValidPath(self, grid: List[List[str]]) -> bool:
    m, n = len(grid), len(grid[0])
    if grid[0][0] == ')' or grid[-1][-1] == '(':
      return False

    if (m+n-1) % 2 > 0:
      return False
    
    stack = [(0, 0, 1)]
    visited = set()
    
    while stack:
      x, y, s = stack.pop()
      for dx, dy in [(0, 1), (1, 0)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
          continue
          
        ns = s + (-1 if grid[x0][y0] == ')' else 1)
        
        # more close parentheses than open ones, illegal
        if ns < 0:
          continue
          
        # won't have enough close parentheses
        if ns > (m-1-x0) + (n-1-y0):
          continue
        
        if x0 == m-1 and y0 == n-1:
          if ns == 0:
            return True
          
          continue
          
        if (x0, y0, ns) in visited:
          continue
          
        visited.add((x0, y0, ns))
        stack.append((x0, y0, ns))
    
    return False
  