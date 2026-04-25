'''
3464-maximize-the-distance-between-points-on-a-square
'''

from typing import List
from bisect import bisect_left


class Solution:
  def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
    low, high= 1, 4*side//k
    res = low
    s = side

    def pos(x: list[int]):
      # left side
      if x[0] == 0:
        return 4*s - x[1]

      # top side
      if x[1] == side:
        return 3*s - x[0]
        
      return x[0] + x[1]

    arr = [pos(x) for x in points]
    arr.sort()
    # print(A)

    def check(dist: int):
      for i in range(len(arr)):
        curr = arr[i]
        for _ in range(k-1):
          # find the next point in arr with
          # dist >= mid
          idx = bisect_left(arr, curr+dist)
          if idx >= len(arr):
            return False

          curr = arr[idx]

        # check head and tail dist, if still 
        # greater than mid, then done 
        if (arr[i]+4*s) - arr[idx] >= dist:
          return True

      return False

    while low <= high:
      mid = (low + high) // 2
      if check(mid):
        low = mid + 1
        res = mid
      else:
        high = mid - 1

    return res
    