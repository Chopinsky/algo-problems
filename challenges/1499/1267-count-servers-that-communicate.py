'''
1267-count-servers-that-communicate
'''


class Solution:
  def countServers(self, grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    rows = [0]*m
    cols = [0]*n
    cnt = 0
    cand = []

    for x in range(m):
      for y in range(n):
        if grid[x][y] == 0:
          continue

        cnt += 1
        rows[x] += 1
        cols[y] += 1
        cand.append((x, y))
    
    isolated = 0
    for x, y in cand:
      if rows[x] == 1 and cols[y] == 1:
        isolated += 1

    return cnt - isolated
        