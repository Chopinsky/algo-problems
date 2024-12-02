'''
1861. Rotating the Box

You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

Example 1:

Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:

Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:

Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

Constraints:

m == box.length
n == box[i].length
1 <= m, n <= 500
box[i][j] is either '#', '*', or '.'.
'''

from typing import List


class Solution:
  def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
    m, n = len(box), len(box[0])
    res = [['.']*m for _ in range(n)]
    
    def mark_stones(x: int, y: int, cnt: int):
      if y < n:
        res[y][m-1-x] = '*'
      
      y -= 1
      while cnt > 0 and y >= 0:
        res[y][m-1-x] = '#'
        cnt -= 1
        y -= 1
    
    for x in range(m):
      curr = 0
      for y in range(n):
        if box[x][y] == '*':
          mark_stones(x, y, curr)
          curr = 0
          continue
        
        if box[x][y] == '#':
          curr += 1
          
      mark_stones(x, n, curr)
    
    return res
        
  def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
    m, n = len(box), len(box[0])
    ans = [['.']*m for _ in range(n)]
    
    def place_rocks(i, j, cnt):
      while cnt > 0 and i >= 0:
        ans[i][j] = '#'
        cnt -= 1
        i -= 1
    
    for i in range(m):
      cnt = 0
      for j in range(n):
        if box[i][j] == '.':
          continue
          
        if box[i][j] == '#':
          cnt += 1
          continue
          
        ans[j][m-1-i] = '*'
        place_rocks(j-1, m-1-i, cnt)
        cnt = 0
          
      if cnt > 0:
        place_rocks(n-1, m-1-i, cnt)
    
    return ans
    