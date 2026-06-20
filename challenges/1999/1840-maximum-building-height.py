'''
1840-maximum-building-height
'''

from typing import List
from heapq import heappop, heappush


class Solution:
  def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
    if not restrictions:
      return n-1

    r = sorted([[1, 0]] + restrictions)
    cand = sorted([h, idx, i] for i, [idx, h] in enumerate(r))

    while cand:
      h, idx, i = heappop(cand)

      # the building site has been processed
      if h != r[i][1]:
        continue

      if i > 0:
        ldx, lh = r[i-1]
        if h + (idx-ldx) < lh:
          r[i-1][1] = h + (idx-ldx)
          heappush(cand, [r[i-1][1], r[i-1][0], i-1])

      if i < len(r)-1:
        rdx, rh = r[i+1]
        if h + (rdx-idx) < rh:
          r[i+1][1] = h + (rdx-idx)
          heappush(cand, [r[i+1][1], r[i+1][0], i+1])

    # print('p1:', max(val[1] for val in r))
    def get_tall(i: int) -> int:
      ldx, lh = r[i]
      rdx, rh = r[i+1]

      if abs(lh-rh) == abs(ldx-rdx):
        return max(lh, rh)

      # find the peak index
      k = ((ldx+rdx) + (rh-lh)) // 2

      # return the tallest building height from the peak index
      return min((k-ldx)+lh, (rdx-k)+rh)

    tall = 0
    curr = 0

    for i in range(len(r)-1):
      rdx, rh = r[i+1]

      if curr + (rdx-i) <= rh:
      # can go up all the time
        curr += (rdx-i)
        tall = max(tall, curr)
        # print('c1:', curr, tall)
      else:
        # tall is between the two sites
        r[i][1] = curr
        tall = max(tall, get_tall(i))
        curr = rh
        # print('c2:', curr, tall)

    # also check the tail height
    return max(tall, curr + (n-r[-1][0]))
