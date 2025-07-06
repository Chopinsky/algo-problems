'''
594-longest-harmonious-subsequence
'''

from typing import List
from collections import Counter


class Solution:
  def findLHS(self, nums: List[int]) -> int:
    vals = Counter(nums)
    cand = sorted(vals)
    long = 0

    for i in range(1, len(cand)):
      if cand[i]-cand[i-1] > 1:
        continue

      long = max(long, vals[cand[i]]+vals[cand[i-1]])

    return long
        