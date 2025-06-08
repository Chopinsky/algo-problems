'''
1128-number-of-equivalent-domino-pairs
'''

from collections import defaultdict
from typing import List


class Solution:
  def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    seen = defaultdict(int)
    pairs = 0

    for a, b in dominoes:
      a, b = min(a, b), max(a, b)
      if (a, b) in seen:
        pairs += seen[a, b]

      seen[a, b] += 1

    return pairs
        