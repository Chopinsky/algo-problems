'''
2843-count-symmetric-integers
'''


class Solution:
  def countSymmetricIntegers(self, low: int, high: int) -> int:
    def count(limit: int) -> int:
      if limit < 10:
        return 0

      cnt = 0
      for v0 in range(1, 10):
        val = 10*v0 + v0
        if val > limit:
          break

        cnt += 1

      for v0 in range(1000, min(limit+1, 10000)):
        s0 = str(v0)
        v1 = int(s0[0]) + int(s0[1])
        v2 = int(s0[2]) + int(s0[3])
        if v1 == v2:
          cnt += 1

      return cnt

    return count(high) - count(low-1)
