'''
An image is represented by a binary matrix with 0 as a white pixel
and 1 as a black pixel. The black pixels are connected, i.e., there 
is only one black region. Pixels are connected horizontally and 
vertically. Given the location (x, y) of one of the black pixels, 
return the area of the smallest (axis-aligned) rectangle that 
encloses all black pixels.

For example, given the following image:
[
  "0010",
  "0110",
  "0100"
]

and x = 0, y = 2,

Return 6.
'''

from typing import List


class Solution:
  def smallest_rectangle(self, arr: List[str], x: int, y: int) -> int:
    m, n = len(arr), len(arr[0])

    def check(i: int, is_row: bool) -> bool:
      if is_row:
        if i >= m or i < 0:
          return False

        for j in range(n):
          if arr[i][j] == '1':
            return True

        return False

      else:
        if i >= n or i < 0:
          return False

        for j in range(m):
          if arr[j][i] == '1':
            return True

        return False

    def search(s: int, e: int, last: int, dirs: int, is_row: bool) -> int:
      while s < e:
        m = (s + e) // 2

        if check(m, is_row):
          last = m
          if dirs > 0:
            s = m+1
          else:
            e = m-1

        else:
          if dirs > 0:
            e = m-1
          else:
            s = m+1
      
      return s if check(s, is_row) else last

    l = search(0, y, y, -1, False)
    r = search(y, n, y, 1, False)
    u = search(0, x, x, -1, True)
    b = search(x, m, x, 1, True)

    return (r-l+1) * (b-u+1)

  def smallest_rectangle0(self, arr: List[str], x: int, y: int) -> int:
    l, r, u, b = y, y, x, x
    # print(l, r, u, b)
    q = [(x, y)]
    seen = set(q)
    m, n = len(arr), len(arr[0])

    while q:
      x, y = q.pop()
      l = min(l, y)
      r = max(r, y)
      u = min(u, x)
      b = max(b, x)

      for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or (x0, y0) in seen:
          continue
        
        if arr[x0][y0] != '1':
          continue

        seen.add((x0, y0))
        q.append((x0, y0))

    # print(l, r, u, b)
    return (r-l+1) * (b-u+1)


s = Solution()
t = [
  [["0010", "0110", "0100"], 0, 2, 6],
]

for arr, x, y, ans in t:
  print('\n========\nTest Case:', arr, x, y)
  print('Expected:', ans)
  print('Result  :', s.smallest_rectangle(arr, x, y))
