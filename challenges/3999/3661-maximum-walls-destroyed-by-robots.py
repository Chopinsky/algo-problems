'''
3661-maximum-walls-destroyed-by-robots
'''

from typing import List
from bisect import bisect_left, bisect_right
from math import inf


class Solution:
  def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
    arr = sorted(zip(robots, distance))
    n = len(arr)
    walls.sort()

    def count(l: int, r: int) -> int:
      if l > r:
        return 0

      return bisect_right(walls, r) - bisect_left(walls, l)

    rem = 0
    used = count(arr[0][0] - arr[0][1], arr[0][0]-1) # to the left of the 0-th robot
    arr.append([inf, 0])

    for i in range(n):
      l, dl = arr[i]
      r, dr = arr[i+1]

      l1, r1 = l+1, min(l+dl, r-1)
      l2, r2 = max(r-dr, l+1), r-1

      left = count(l1, r1)
      right = count(l2, r2)
      total = left + right - count(max(l1, l2), min(r1, r2))

      nxt_rem = max(rem+left, used)
      nxt_used = max(rem+total, used+right)
      rem, used = nxt_rem, nxt_used

    for x in set(x for x, _ in arr):
      used += count(x, x)

    return used

        