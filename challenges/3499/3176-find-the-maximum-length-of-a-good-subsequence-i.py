'''
3176-find-the-maximum-length-of-a-good-subsequence-i
'''

from collections import defaultdict
from typing import List


class Solution:
  def maximumLength(self, nums: List[int], k: int) -> int:
    curr = defaultdict(int)

    for val in nums:
      nxt = curr.copy()
      # print('iter:', val, curr)

      for key, ln in curr.items():
        last, rem = key
        if last == val:
          nxt[val, rem] = max(nxt[val, rem], 1+ln)

        elif rem > 0:
          nxt[val, rem-1] = max(nxt[val, rem-1], 1+ln)

      nxt[val, k] = max(nxt[val, k], 1)
      curr = nxt

    return max(curr.values())
