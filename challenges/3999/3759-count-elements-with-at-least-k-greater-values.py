'''
3759-count-elements-with-at-least-k-greater-values
'''

from typing import List
from collections import Counter


class Solution:
  def countElements(self, nums: List[int], k: int) -> int:
    c = Counter[int, int](nums)
    cand = sorted(c.keys())
    cnt = 0

    while cnt < k:
      val = cand.pop()
      cnt += c[val]

    return sum(c[val] for val in cand)
        