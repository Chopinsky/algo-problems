'''
3577-count-the-number-of-computer-unlocking-permutations
'''

from typing import List


class Solution:
  def countPermutations(self, complexity: List[int]) -> int:
    n = len(complexity)
    c0 = complexity[0]
    if c0 != min(complexity) or complexity.count(c0) > 1:
      return 0

    mod = 10**9 + 7
    res = 1
    n -= 1

    while n > 0:
      res = (res * n) % mod
      n -= 1

    return res
        