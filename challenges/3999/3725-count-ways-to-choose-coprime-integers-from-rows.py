'''
3725-count-ways-to-choose-coprime-integers-from-rows
'''

from typing import List
from collections import Counter
from math import gcd


class Solution:
  '''
  iterate on all gcd values with ways to reach it from 
  picking values from previous rows
  '''
  def countCoprime(self, mat: List[List[int]]) -> int:
    mod = 10**9 + 7
    cnt = Counter(mat[0])

    for row in mat[1:]:
      nxt = Counter()
      for v1 in row:
        for v0, c in cnt.items():
          g = gcd(v0, v1)
          nxt[g] = (nxt[g] + c) % mod

      cnt = nxt

    return cnt[1]
        