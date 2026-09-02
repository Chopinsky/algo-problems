'''
3622-check-divisibility-by-digit-sum-and-product
'''

class Solution:
  def checkDivisibility(self, n: int) -> bool:
    ds = 0
    dp = 1

    for d in str(n):
      ds += int(d)
      dp *= int(d)

    return n % (ds+dp) == 0
        