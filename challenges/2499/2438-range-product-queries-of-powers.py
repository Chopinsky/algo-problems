'''
2438-range-product-queries-of-powers
'''

from typing import List


class Solution:
  def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    cand = []
    mask = 1

    while mask <= n:
      if (mask & n) > 0:
        cand.append(mask) 

      mask <<= 1

    # print('init:', cand)
    n = len(cand)
    mod = 10**9 + 7
    prefix = [cand[0]]

    for i in range(1, n):
      prefix.append((prefix[-1] * cand[i]) % mod)

    def calc(l: int, r: int) -> int:
      if l == r:
        return cand[r]

      if l == 0:
        return prefix[r]

      # print('calc', (l, r), prefix[r], prefix[l-1])
      return (prefix[r] * pow(prefix[l-1], mod-2, mod)) % mod

    ans = []
    # print('prefix:', prefix)

    for l, r in queries:
      ans.append(calc(l, r))

    return ans
        