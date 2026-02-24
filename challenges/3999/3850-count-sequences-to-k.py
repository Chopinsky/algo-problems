'''
3850-count-sequences-to-k
'''

from functools import cache


class Solution:
  def countSequences(self, nums: list[int], k: int) -> int:
    @cache
    def factors(val: int) -> tuple[list[int], int]:
      res = [0, 0, 0]
      while val%2 == 0:
        res[0] += 1
        val //= 2

      while val%3 == 0:
        res[1] += 1
        val //= 3

      while val%5 == 0:
        res[2] += 1
        val //= 5

      return res, val

    tgt, rem = factors(k)
    if rem > 1:
      return 0

    n = len(nums)
    suffix = [[0, 0, 0] for _ in range(n)]

    for i in range(n-1, -1, -1):
      curr, rem = factors(nums[i])
      if rem > 1:
        return 0

      for j in range(3):
        suffix[i][j] = curr[j] + (0 if i == n-1 else suffix[i+1][j])

    # print('init:', tgt, suffix)

    @cache
    def dp(i: int, c2: int, c3: int, c5: int) -> int:
      if i >= n:
        return 1 if c2 == tgt[0] and c3 == tgt[1] and c5 == tgt[2] else 0

      s2, s3, s5 = suffix[i]
      if s2+c2 < tgt[0] or s3+c3 < tgt[1] or s5+c5 < tgt[2]:
        return 0

      curr, _ = factors(nums[i])

      # skip
      seq0 = dp(i+1, c2, c3, c5)

      # mult
      seq1 = dp(i+1, c2+curr[0], c3+curr[1], c5+curr[2])

      # div
      seq2 = dp(i+1, c2-curr[0], c3-curr[1], c5-curr[2])

      return seq0 + seq1 + seq2

    return dp(0, 0, 0, 0)
        