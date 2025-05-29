'''
2894-divisible-and-non-divisible-sums-difference
'''


class Solution:
  def differenceOfSums(self, n: int, m: int) -> int:
    v0 = sum(val for val in range(n+1) if val%m > 0)
    v1 = sum(val for val in range(n+1) if val%m == 0)
    return v0-v1
        