'''
3513-number-of-unique-xor-triplets-i
'''

from typing import List


class Solution:
  def uniqueXorTriplets(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
      return n

    cnt = 0
    while n > 0:
      n >>= 1
      cnt += 1

    return 1 << cnt 

        