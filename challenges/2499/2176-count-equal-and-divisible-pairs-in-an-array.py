'''
2176-count-equal-and-divisible-pairs-in-an-array
'''

from collections import defaultdict
from typing import List


class Solution:
  def countPairs(self, nums: List[int], k: int) -> int:
    pos = defaultdict(list)
    n = len(nums)
    count = 0

    for i in range(n):
      val = nums[i]
      for j in pos[val]:
        if i*j % k == 0:
          count += 1

      pos[val].append(i)

    return count 
        