'''
1411-number-of-ways-to-paint-n-3-grid
'''


class Solution:
  def numOfWays(self, n: int) -> int:
    mod = 10**9+7
    curr, nxt = [6, 6], []

    for _ in range(1, n):
      nxt.append((2*curr[0]+2*curr[1])%mod)
      nxt.append((2*curr[0]+3*curr[1])%mod)
      curr, nxt = nxt, curr
      nxt.clear()

    return sum(curr)%mod
        