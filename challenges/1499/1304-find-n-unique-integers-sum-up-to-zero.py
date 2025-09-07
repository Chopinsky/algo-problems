'''
1304-find-n-unique-integers-sum-up-to-zero
'''

from typing import List


class Solution:
  def sumZero(self, n: int) -> List[int]:
    pairs = n // 2
    res = []
    for i in range(pairs):
      res.append(i+1)
      res.append(-i-1)

    if n%2 == 1:
      res.append(0)
      
    return res

