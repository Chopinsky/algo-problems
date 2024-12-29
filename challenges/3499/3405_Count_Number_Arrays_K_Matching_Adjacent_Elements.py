'''
3405. Count the Number of Arrays with K Matching Adjacent Elements
'''

class Solution:
  def countGoodArrays(self, n: int, m: int, k: int) -> int:
    mod = 10**9+7
    if n == 1:
      return m

    if k == 0:
      return (m * pow(m-1, n-1, mod)) % mod

    if m == 1:
      return 1 if k == n-1 else 0

    if k == n-1:
      return m

    def cnr(n: int, r: int):
      if r > n:
        return 0

      val = 1
      den = 1

      for i in range(r):
        val = (val * (n-i)) % mod
        den = (den * (i+1)) % mod

      return (val * pow(den, mod-2, mod)) % mod

    return (m * pow(m-1, n-1-k, mod) * cnr(n-1, k)) % mod
         