'''
3867-sum-of-gcd-of-formed-pairs
'''

from math import gcd


class Solution:
  def gcdSum(self, nums: list[int]) -> int:
    n = len(nums)
    prefix = []
    mxi = 0

    for val in nums:
      mxi = max(mxi, val)
      prefix.append(gcd(val, mxi))

    prefix.sort()
    i, j = 0, n-1
    sums = 0

    while i < j:
      sums += gcd(prefix[i], prefix[j])
      i += 1
      j -= 1

    return sums

        