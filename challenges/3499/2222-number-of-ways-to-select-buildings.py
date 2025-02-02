'''
2222-number-of-ways-to-select-buildings
'''

from bisect import bisect_right


class Solution:
  def numberOfWays(self, s: str) -> int:
    n = len(s)
    ones = [i for i in range(n) if s[i] == '1']
    zeros = [i for i in range(n) if s[i] == '0']
    cnt = 0

    for i in range(1, n-1):
      cand = ones if s[i] == '0' else zeros
      j = bisect_right(cand, i)
      rc = len(cand)-j
      lc = j
      cnt += lc*rc

    return cnt
        