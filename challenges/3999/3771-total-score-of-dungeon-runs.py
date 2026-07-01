'''
3771-total-score-of-dungeon-runs
'''

from typing import List
from bisect import bisect_left


class Solution:
  def totalScore(self, hp: int, damage: List[int], req: List[int]) -> int:
    n = len(damage)

    # the damage is accumulating, so use prefix to calc all damages
    # at or before index-i
    prefix = [0]*(n+1)
    for i in range(n):
      prefix[i+1] = prefix[i] + damage[i]

    # print('init', prefix)
    res = 0
    for i in range(n):
      target = req[i] + prefix[i+1] - hp

      # the index that meets the target could be after the current
      # index or at index-n, so cap at (i+1) for easier calculation
      idx = min(i+1, bisect_left(prefix, target))

      # count how many score(j) that contains index i this point
      # can appear in with larger than the requirements hp left
      res += i + 1 - idx

    return res
