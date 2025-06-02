'''
1295-find-numbers-with-even-number-of-digits
'''

from typing import List


class Solution:
  def findNumbers(self, nums: List[int]) -> int:
    cnt = 0

    for val in nums:
      ln = len(str(val))
      if ln % 2 == 0:
        cnt += 1

    return cnt
        