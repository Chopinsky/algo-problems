'''
3882-minimum-xor-path-in-a-grid
'''


class Solution:
  def minCost(self, grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    prev = [set()]*n
    curr = []

    for i, row in enumerate(grid):
      for j, val in enumerate(row):
        if i == 0 and j == 0:
          curr.append(set([val]))
          continue

        nxt = set()
        for p0 in prev[j]:
          nxt.add(p0^val)

        if curr:
          for p0 in curr[-1]:
            nxt.add(p0^val)

        curr.append(nxt)

      curr, prev = prev, curr
      curr.clear()
      # print('done:', row, prev)

    return min(prev[-1])
        