'''
3785-minimum-swaps-to-avoid-forbidden-values
'''

from collections import Counter
from typing import List


class Solution:
  def minSwaps(self, a: List[int], f: List[int]) -> int:
    n = len(a)
    fa = Counter(a)
    ff = Counter(f)

    for v, c in fa.items():
      if v not in ff:
        continue

      if c > n-ff[v]:
        return -1

    cnt = 0 
    matching = Counter()
    maxi = 0

    for i in range(n):
      if a[i] == f[i]:
        cnt += 1
        matching[a[i]] += 1
        maxi = max(maxi, matching[a[i]])

    return max(maxi, (cnt+1)//2)
        