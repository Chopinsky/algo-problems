'''
3190-find-minimum-operations-to-make-all-elements-divisible-by-three
'''

from typing import List


class Solution:
  def minimumOperations(self, nums: List[int]) -> int:
    return sum(1 if val%3 > 0 else 0 for val in nums)
  
        