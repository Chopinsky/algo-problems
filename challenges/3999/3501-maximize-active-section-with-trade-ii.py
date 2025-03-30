'''
3501-maximize-active-section-with-trade-ii
'''

import math
from typing import List
from bisect import bisect_right


class Solution:
  def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
    n = len(s)
    oc = s.count('1')
    seg = []
    start = 0

    for i in range(n):
      if i == n-1 or s[i] != s[i+1]:
        seg.append((start, i-start+1))
        start = i+1

    seg_ln = len(seg)
    power = 20
    rmq = [[-math.inf]*seg_ln for _ in range(power)]
    # print('init:', seg)

    for i in range(seg_ln):
      if s[seg[i][0]] == '0' and i+2 < seg_ln:
        rmq[0][i] = seg[i][1] + seg[i+2][1]

    for p in range(1, power):
      rng_ln = 1 << p
      for i in range(seg_ln - rng_ln + 1):
        rmq[p][i] = max(
          rmq[p-1][i],
          rmq[p-1][i+(rng_ln >> 1)]
        )

    def max_in_range(l: int, r: int) -> int:
      if l > r:
        return -math.inf

      p = (r-l+1).bit_length() - 1
      return max(
        rmq[p][l],
        rmq[p][r - (1<<p) + 1]
      )

    result = []

    for l, r in queries:
      ldx = bisect_right(seg, (l, math.inf)) - 1
      rdx = bisect_right(seg, (r, math.inf)) - 1

      if rdx - ldx + 1 <= 2:
        result.append(oc)
        continue
      
      def seg_size(i: int) -> int:
        if i == ldx:
          return seg[ldx][1] - (l-seg[ldx][0])

        if i == rdx:
          return r - seg[rdx][0] + 1

        return seg[i][1]

      def calc_new_sec(i: int) -> int:
        if i < 0 or i+2 >= seg_ln or s[seg[i][0]] == '1':
          return -math.inf

        return seg_size(i) + seg_size(i+2)

      ln0 = max_in_range(ldx+1, rdx-3)
      ln1 = calc_new_sec(ldx)
      ln2 = calc_new_sec(rdx-2)
      ln = max(0, ln0, ln1, ln2)
      result.append(oc + ln)

    return result
