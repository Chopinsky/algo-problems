'''
4081-prime-subset-selection-ii
'''

from bisect import bisect_right


top = 1001
sv = [i for i in range(top)]
p = []
INF = float('inf')

for v0 in range(2, top):
  if sv[v0] < v0:
    continue

  p.append(v0)
  for v1 in range(v0*v0, top, v0):
    sv[v1] = v0


class Solution:
  def maxPrimeSubset(self, n: int, s: int) -> list[int]:
    if s < 2 or n < 2:
      return []

    # print('iter:', dp)
    limit = min(n, s)
    m = bisect_right(p, limit)
    if m <= 0:
      return []

    # dp[i][v] is count of primes in the subset to reach 
    # v with primes from i+ primes
    dp = [[INF]*top for _ in range(m+1)]
    dp[m][0] = 0

    for i in range(m-1, -1, -1):
      pval = p[i]
      for v in range(top):
        dp[i][v] = dp[i+1][v]
        if v >= pval and dp[i+1][v-pval] < INF:
          dp[i][v] = min(dp[i][v], dp[i+1][v-pval] + 1)

    best = -1
    for v in range(s, 0, -1):
      if dp[0][v] < INF:
        best = v
        break

    c = dp[0][best]
    rem = best
    i = 0
    res = []
    # print('init:', best, dp[0][best], dp)

    while rem > 0:
      for j in range(i, m):
        pv = p[j]
        if pv > rem:
          # out of the bound
          break

        # meeting the criteria, greedily taking
        if dp[j+1][rem-pv] == c-1:
          res.append(pv)
          rem -= pv
          c -= 1
          i = j+1
          break

    return res

        