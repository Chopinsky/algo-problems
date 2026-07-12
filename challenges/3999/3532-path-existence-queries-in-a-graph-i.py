'''
3532-path-existence-queries-in-a-graph-i
'''

from bisect import bisect_right
from typing import List


class Solution:
  def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
    walls = []
    for i in range(1, n):
      if nums[i]-nums[i-1] > maxDiff:
        walls.append(i)

    if not walls:
      return [True]*len(queries)

    ans = []
    # print('init:', walls)

    for l, r in queries:
      if l == r:
        ans.append(True)
        continue

      ldx = bisect_right(walls, l) - 1
      rdx = bisect_right(walls, r) - 1
      ans.append(ldx == rdx)

    return ans
        