'''
3756-concatenate-non-zero-digits-and-multiply-by-sum-ii
'''

from typing import List


mod = 10**9 + 7
top = 100001
p10 = [1]*top

for i in range(1, top):
  p10[i] = (p10[i-1]*10) % mod


class Solution:
  def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
    n = len(s)
    sums = [0]*(n+1)
    x = [0]*(n+1)
    cnt = [0]*(n+1)

    for i in range(n):
      d = int(s[i])
      sums[i+1] = sums[i] + d
      x[i+1] = (x[i]*10 + d) % mod if d > 0 else x[i]
      cnt[i+1] = cnt[i] + (1 if d > 0 else 0)

    res = []
    for l, r in queries:
      r += 1
      s0 = (sums[r] - sums[l]) % mod
      # prefix val calc: 1234 - 12*100 = 34
      x0 = (x[r] - x[l]*p10[cnt[r]-cnt[l]]) % mod
      res.append((s0*x0) % mod)
      
    return res
