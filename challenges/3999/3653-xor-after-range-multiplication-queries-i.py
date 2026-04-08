'''
3653-xor-after-range-multiplication-queries-i
'''

from typing import List


class Solution:
  def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
    mod = 10**9 + 7

    def update(l: int, r: int, k: int, v: int):
      i = l
      while i <= r:
        nums[i] = (nums[i] * v) % mod
        i += k

    for q in queries:
      update(*q)

    # print('done:', nums)
    val = nums[0]
    for v0 in nums[1:]:
      val ^= v0

    return val
        