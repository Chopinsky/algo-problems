'''
2154-keep-multiplying-found-values-by-two
'''

from typing import List


class Solution:
  def findFinalValue(self, nums: List[int], original: int) -> int:
    s = set(nums)
    while original in s:
      original <<= 1

    return original
        