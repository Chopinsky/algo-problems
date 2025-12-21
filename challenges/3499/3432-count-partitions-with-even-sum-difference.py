'''
3432-count-partitions-with-even-sum-difference
'''

from typing import List


class Solution:
  def countPartitions(self, nums: List[int]) -> int:
    n = len(nums)
    ls = 0 
    rs = sum(nums)
    count = 0

    for i in range(n-1):
      val = nums[i]
      ls += val
      rs -= val
      # print('iter:', i, ls, rs)

      if abs(ls-rs) % 2 == 0:
        count += 1

    return count

        