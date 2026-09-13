'''
835. Image Overlap

You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

Example 1:


Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1
Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0

Constraints:

n == img1.length == img1[i].length
n == img2.length == img2[i].length
1 <= n <= 30
img1[i][j] is either 0 or 1.
img2[i][j] is either 0 or 1.
'''

from typing import List
from collections import Counter
from functools import cache


class Solution:
  def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
    n = len(img1)
    a = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
    b = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
    cnt = Counter((i - di, j - dj) for i, j in a for di, dj in b)
    return max(cnt.values()) if cnt else 0

  def largestOverlap0(self, img1: List[List[int]], img2: List[List[int]]) -> int:
    m, n = len(img1), len(img2)
    s1 = set((x, y) for x in range(m) for y in range(n) if img1[x][y] == 1)
    s2 = [(x, y) for x in range(m) for y in range(n) if img2[x][y] == 1]
    if not s1 or not s2:
      return 0

    # print('init:', s1, s2)

    @cache
    def count(dx: int, dy: int) -> int:
      return sum(1 if (x+dx, y+dy) in s1 else 0 for x, y in s2)

    def find(x0: int, y0: int) -> int:
      cnt = 0
      for x1 in range(m):
        for y1 in range(n):
          cnt = max(cnt, count(x0-x1, y0-y1))

      return cnt

    return max(
      find(0, 0),
      find(0, n-1),
      find(m-1, 0),
      find(m-1, n-1),
    )

  def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
    m, n = len(img1), len(img1[0])
    tgt = set()
    src = set()
    
    def shift_and_count(dx: int, dy: int) -> int:
      count = 0
      for i, j in src:
        x, y = i+dx, j+dy
        if 0 <= x < m and 0 <= y < n and (x, y) in tgt:
          count += 1
          
      return count
    
    for i in range(m):
      for j in range(n):
        if img1[i][j] == 1:
          src.add((i, j))
          
        if img2[i][j] == 1:
          tgt.add((i, j))

    base = len(src & tgt)
    # print(src, tgt)
    
    for dx in range(-m+1, m):
      for dy in range(-n+1, n):
        if dx == 0 and dy == 0:
          continue
          
        base = max(base, shift_and_count(dx, dy))
        
    return base
        