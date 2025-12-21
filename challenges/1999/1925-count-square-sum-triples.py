'''
1925-count-square-sum-triples
'''


class Solution:
  def countTriples(self, n: int) -> int:
    cnt = 0
    cand = set()
    top = n*n

    for val in range(1, n+1):
      cand.add(val**2)

    for v0 in range(1, n):
      s0 = v0*v0
      for v1 in range(v0, n):
        s1 = v1*v1
        if s0+s1 > top:
          break

        if s0+s1 in cand:
          cnt += 1 if v0 == v1 else 2

    return cnt
        