'''
3768-minimum-inversion-count-in-subarrays-of-fixed-length
'''

from typing import List
from collections import defaultdict


class Solution:
  def minInversionCount(self, nums: List[int], k: int) -> int:
    if k < 2:
      return 0

    cand = sorted(set(nums))
    pos = {val:i for i, val in enumerate(cand)}
    # print('init:', pos)

    fenwick = [0]*len(pos)
    n = len(fenwick)

    def update(val: int, delta: int):
      idx = pos[val]

      if idx == 0:
        fenwick[idx] += delta
        return

      while idx < n:
        fenwick[idx] += delta
        idx += idx & -idx

    def query(val: int) -> int:
      idx = pos[val]
      s = fenwick[0]
      # print('q:', val, idx)

      while idx > 0:
        s += fenwick[idx]
        idx -= idx & -idx

      return s

    curr = 0
    low = None
    cnt = defaultdict(int)

    for i in range(len(nums)):
      val = nums[i]

      if i < k:
        update(val, 1)
        p0 = (i+1) - query(val)
        curr += p0
        cnt[val] += 1
        if i == k-1:
          low = curr

        # print('iter-0:', val, curr, p0)

      else:
        # pop prev
        prev_val = nums[i-k]
        p0 = query(prev_val)-cnt[prev_val]
        cnt[prev_val] -= 1
        # print('update:', prev_val, p0)

        curr -= p0
        update(prev_val, -1)

        # add new
        update(val, 1)
        p1 = k - query(val)
        curr += p1
        cnt[val] += 1

        # update
        low = min(low, curr)
        # print('iter-1:', curr, low)

    return low if low is not None else 0
        