'''
1534-count-good-triplets
'''

from typing import List
from collections import defaultdict


class Solution:
  def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
    cand = defaultdict(int)
    n = len(arr)
    count = 0

    for i in range(n-2, -1, -1):
      v0 = arr[i]
      # print('iter:', v0, cand)

      for (v1, v2) in cand:
        if abs(v0-v1) <= a and abs(v0-v2) <= c:
          count += cand[v1, v2]

      for j in range(i+1, n):
        v1 = arr[j]
        if abs(v0-v1) <= b:
          cand[v0, v1] += 1
    
    return count
        