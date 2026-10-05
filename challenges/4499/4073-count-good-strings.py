'''
4073-count-good-strings
'''


class Solution:
  def countGoodStrings(self, n: int) -> int:
    mod = 10**9+7
    if n <= 2:
      return 2

    def multi(a: list, b: list) -> list:
      res = []
      res.append([
        (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod, 
        (a[0][0]*b[1][0] + a[0][1]*b[1][1]) % mod,
      ])

      res.append([
        (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod,
        (a[1][0]*b[1][0] + a[1][1]*b[1][1]) % mod,
      ])

      return res

    def power_mult(n: int) -> list:
      base = [[1, 1], [1, 0]]
      res = [[1, 0], [0, 1]]

      while n > 0:
        if n&1 == 1:
          res = multi(res, base)

        base = multi(base, base)
        n >>= 1
        # print('iter:', res)

      return res

    res = power_mult(n-3)
    return (2*sum(res[0]) + 2*sum(res[1])) % mod
        