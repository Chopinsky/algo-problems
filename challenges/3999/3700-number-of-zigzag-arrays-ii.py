'''
3700-number-of-zigzag-arrays-ii
'''

mod = 10**9 + 7

class Matrix(list):
  def __matmul__(a, b):
    ln = len(b[0])
    c = [[0] * ln for _ in a]

    for i, row in enumerate(a):
      for k, v in enumerate(row):
        c[i] = [(cv+v*bv) % mod for cv, bv in zip(c[i], b[k])]

    return Matrix(c)

  def __pow__(a, e: int):
    n = len(a)
    ans = Matrix([[+(i == j) for j in range(n)] for i in range(n)])
    base = a

    while e > 0:
      if e&1 > 0:
        ans = ans @ base

      base = base @ base
      e >>= 1

    return ans


class Solution:
  def zigZagArrays(self, n: int, l: int, r: int) -> int:
    k = r-l+1
    m1 = Matrix([[+(i < j) for j in range(k)] for i in range(k)])
    m2 = Matrix([[k-1-max(i, j) for j in range(k)] for i in range(k)])

    pairs, rem = divmod(n-1, 2)
    a = m2 ** pairs
    # print('init:', m1, m2)

    if rem > 0:
      a = a @ m1

    return sum(sum(row) for row in a) * 2 % mod
        