'''
A group of two or more people wants to meet and minimize 
the total travel distance. You are given a 2D grid of 
values 0 or 1, where each 1 marks the home of someone in 
the group. The distance is calculated using Manhattan Distance, 
where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

The point (0,2) is an ideal meeting point, as the total travel 
distance of 2+2+2=6 is minimal. So return 6.
'''

from typing import Tuple, List, Dict
from collections import defaultdict


class Solution:
  def best_meeting_point(self, points: List[Tuple[int, int]]) -> int:
    n = len(points)

    xdx, ydx = defaultdict(int), defaultdict(int)
    for x, y in points:
      xdx[x] += 1
      ydx[y] += 1

    # the `search` function will determine the optimal point in the 
    # coordinates array such that the total distant won't shrink anymore
    def search(count: Dict[int, int]) -> int:
      pos = sorted(count)
      if len(pos) == 1:
        return 0

      lc, rc = count[pos[0]], n-count[pos[0]]
      ld, rd = 0, sum((p-pos[0]) * count[p] for p in pos[1:])

      # optimal solution already, moving to the right will increase the 
      # total distance of {ld+rd}
      if lc >= rc:
        return ld + rd

      # shifting the pivot point to the right, updating the total {dist}
      # in the meantime; break when {dist} will start rising again, i.e.
      # when lc >= rc, where for every 1 point to the right, we will add
      # more distances than the substracted distances. 
      dist = ld + rd
      for i in range(1, len(pos)):
        p = pos[i]
        diff = (p - pos[i-1]) * (lc - rc)
        if diff >= 0:
          break

        dist += diff

        # now moving count[p] points from right side to the left side
        # and continue the search
        lc += count[p]
        rc -= count[p]

      return dist

    return search(xdx) + search(ydx)


s = Solution()
t = [
  [[(0, 0), (0, 4), (2, 2)], 6]
]

for pts, ans in t:
  print('\n============\nTest Case:', pts)
  print('Expected:', ans)
  print('Gotten  :', s.best_meeting_point(pts))
