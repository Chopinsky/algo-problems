'''
3426. Manhattan Distances of All Arrangements of Pieces
'''

from math import comb


class Solution:
  def distanceSum(self, m: int, n: int, k: int) -> int:
    mod = 10**9 + 7
    dist = 0
    # count of times a pair will appear in the total sums
    freq = comb(m*n-2, k-2) % mod

    # picking [yi, yj] where abs(yi-yj) == d
    for d in range(1, n):
      dist += d*(n-d)*m*m

    # picking [xi, xj] where abs(xi-xj) == d
    for d in range(1, m):
      dist += d*(m-d)*n*n

    return (dist * freq) % mod
        