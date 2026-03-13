'''
3404-count-special-subsequences
'''

from collections import defaultdict
from math import gcd
from bisect import bisect_left


class Solution:
  def numberOfSubsequences(self, nums: list[int]) -> int:
    cnt = 0
    first = defaultdict(list)
    n = len(nums)

    for i in range(n):
      for j in range(i+2, n):
        v0 = nums[i]
        v1 = nums[j]

        g = gcd(v0, v1)
        v0 //= g
        v1 //= g

        first[v0, v1].append((i, j))

    # print('init:', first)
    for (v0, v1), p0 in first.items():
      p1 = first.get((v1, v0), [])
      # print('p:', (v0, v1), p0, p1)

      for i, j in p0:
        k = bisect_left(p1, (j+2, ))
        cnt += len(p1) - k
        # print('iter:', (i, j), k, len(p1)-k)

    return cnt


        